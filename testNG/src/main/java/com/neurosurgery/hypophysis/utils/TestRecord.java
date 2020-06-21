package com.neurosurgery.hypophysis.utils;

import static com.neurosurgery.hypophysis.model.DefaultValue.*;

import com.neurosurgery.hypophysis.model.*;

import com.neurosurgery.hypophysis.service.ExpectedService;
import io.restassured.RestAssured;
import io.restassured.config.EncoderConfig;
import io.restassured.config.SSLConfig;
import io.restassured.response.Response;
import io.restassured.response.ValidatableResponse;
import io.restassured.specification.RequestSpecification;
import lombok.extern.slf4j.Slf4j;
import org.springframework.util.StringUtils;
import org.testng.Assert;

import java.util.HashMap;
import java.util.Map;

@Slf4j
public class TestRecord implements ITestRecord {

    private static final String HTTPS_PERFIX = "https";
    public static TemplateUtil templateUtil = new TemplateUtil();

    private ProjectVo projectVo;
    private SuiteVo suiteVo;
    private CasePo casePo;
    private StepPo stepPo;
    private String respinseBody = null;
    private ExpectedService expectedService;

    private Map<String, String> vars = new HashMap<>();

    private String domain, url, method;

    public TestRecord(ExpectedService expectedService, ProjectPo projectPo, SuitePo suitePo, CasePo casePo, StepPo stepPo) {
        this.expectedService = expectedService;
        this.projectVo = projectPo;
        this.suiteVo = suitePo;
        this.casePo = casePo;
        this.stepPo = stepPo;
        this.init();
    }

    public TestRecord(ExpectedService expectedService, CaseModule caseModule, StepPo stepPo) {
        this.expectedService = expectedService;
        this.stepPo = stepPo;
        this.casePo = caseModule;
        this.suiteVo = caseModule.getSuiteVo();
        this.projectVo = caseModule.getProjectVo();
        this.init();
    }

    private void init() {
        this.url = this.stepPo.getPath();
        this.method = this.stepPo.getMethod();
//        vars是testrecord内部变量，作用域仅限testrecord
//        初始化时拷贝所有projectvo的值
//        初始化后，外部可对其进行修改，比如注入等价类，任何操作都不会影响projectPo
//        execute前将已经完全装配成型的vars注入给templateUtil.vars以供数据绑定
        this.vars.putAll(this.projectVo.getParameterMap());
//        因为有前后置跨域跨服务的问题，所以采用合并的方式
        templateUtil.context.putAll(this.projectVo.getContextMap());
    }

    public void setEquivalence(Map<String, String> equivalence) {
        this.vars.putAll(equivalence);
    }

    @Override
    public void execute() {
        templateUtil.addVars(this.vars);
        log.info("Suite:{};Case:{};Step:{}", suiteVo.getName(), casePo.getName(), stepPo.getNumber());
        RestAssured.config = RestAssured.config().encoderConfig(EncoderConfig.encoderConfig().defaultContentCharset("UTF-8"));
        RequestSpecification requestSpecification = RestAssured.given();


        this.domain = templateUtil.vars.get("domain");

        if (stepPo.isCookies()) {
            requestSpecification.cookies(templateUtil.cookie);
        }

        stepPo.getRequestHeaderVoSet().forEach(header -> {
            String type, value;
            type = header.getType();
            value = templateUtil.dataBinding(header.getValue());
            requestSpecification.header(type, value);
            log.info("HEADER:type:{};value:{}", type, value);
        });
        // 设置request Content-Type
        requestSpecification.contentType(stepPo.getContentType());
        log.info("Content-Type:{}", stepPo.getContentType());
        // 请求参数
        switch (stepPo.getContentType()) {
            case "text/plain":
            case "application/x-www-form-urlencoded":
                this.stepPo.getRequestParameterVoSet().forEach(param -> {
                    String name, value;
                    name = param.getName();
                    value = templateUtil.dataBinding(param.getValue());
                    requestSpecification.param(name, value);
                    log.info("PARAMETER:type:{};value:{}", name, value);
                });
                break;
            case "application/json":
            case "text/xml":
                String body = templateUtil.dataBinding(this.stepPo.getBody());
                requestSpecification.body(body);
                log.info("BODY:{}", body);
                break;
            default:
                throw new IllegalArgumentException("Content-Type输入不合法");
        }

        if (this.domain.startsWith(HTTPS_PERFIX)) {
            requestSpecification.config((RestAssured.config().sslConfig(new SSLConfig().relaxedHTTPSValidation())));
        }
        String method = stepPo.getMethod(), url = this.domain + this.url;
        Response response = requestSpecification.request(method, url);


        log.info("REQUEST:method:{};url:{}", method, url);
        this.respinseBody = response.body().asString();
        response.print();
        response.body().asString();
        ValidatableResponse validatableResponse = response.then();
        validatableResponse.statusCode(STATUS_CODE);

        templateUtil.cookie.putAll(response.cookies());


        if (stepPo.getExpectedVo() != null && !StringUtils.isEmpty(stepPo.getExpectedVo().getValue())) {
            String actual = response.getBody().asString().trim();
            String expected = stepPo.getExpectedVo().getValue().trim();
            Assert.assertTrue(new JsonUtils(actual).contains(this.expectedService.generate(expected)));
        }

        stepPo.getContextVoSet().forEach(context -> {
            String[] contextValues = context.getValue().split("\\.", 2);
            switch (contextValues[0]) {
                case "html":
                    templateUtil.context.put(context.getName(), response.htmlPath().getString(context.getValue()));
                    break;
                case "body":
                    templateUtil.context.put(context.getName(), response.path(contextValues[1]).toString());
                    break;
                case "cookies":
                    break;
                default:
                    throw new IllegalArgumentException("Context输入不合法");
            }
        });
    }

    public String getDetails() {
        StringBuffer testRecordDetails = new StringBuffer();
        testRecordDetails.append("method:");
        testRecordDetails.append(this.stepPo.getMethod());
        testRecordDetails.append(";");
        testRecordDetails.append("Content-Type:");
        testRecordDetails.append(this.stepPo.getContentType());
        testRecordDetails.append(";");
        testRecordDetails.append("url:");
        testRecordDetails.append(this.stepPo.getPath());
        testRecordDetails.append("<br>:");
        testRecordDetails.append("headers:<br>");
        for (RequestHeaderVo requestHeaderVo : this.stepPo.getRequestHeaderVoSet()) {
            testRecordDetails.append(requestHeaderVo.getType());
            testRecordDetails.append(":");
            testRecordDetails.append(requestHeaderVo.getValue());
            testRecordDetails.append("<br>");
        }
        testRecordDetails.append("parameters:<br>");
        for (RequestParameterVo requestParameterVo : this.stepPo.getRequestParameterVoSet()) {
            testRecordDetails.append(requestParameterVo.getName());
            testRecordDetails.append(":");
            testRecordDetails.append(requestParameterVo.getValue());
            testRecordDetails.append("<br>");
        }
        testRecordDetails.append("body:<br>");
        testRecordDetails.append(this.stepPo.getBody());
        testRecordDetails.append("<br>");
        testRecordDetails.append("response:<br>");
        testRecordDetails.append(this.respinseBody);
        testRecordDetails.append("<br>");
        testRecordDetails.append("Context:<br>");
        for (ContextVo contextVo : this.stepPo.getContextVoSet()) {
            testRecordDetails.append(contextVo.getName());
            testRecordDetails.append(":");
            testRecordDetails.append(contextVo.getValue());
            testRecordDetails.append("<br>");
        }
        testRecordDetails.append("Expected:<br>");
        if (stepPo.getExpectedVo() != null) {
            testRecordDetails.append(this.stepPo.getExpectedVo().getValue());
        }
        testRecordDetails.append("<br>");
//        }
        return testRecordDetails.toString();
    }

    public ProjectVo getProjectVo() {
        return this.projectVo;
    }

    public SuiteVo getSuite() {
        return this.suiteVo;
    }

    public CasePo getCase() {
        return this.casePo;
    }

    public StepPo getStep() {
        return this.stepPo;
    }
}
