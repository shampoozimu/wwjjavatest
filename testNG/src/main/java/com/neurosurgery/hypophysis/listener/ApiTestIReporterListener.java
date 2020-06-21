package com.neurosurgery.hypophysis.listener;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.ResourceCDN;
import com.aventstack.extentreports.Status;
import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import com.aventstack.extentreports.reporter.configuration.ChartLocation;

import com.aventstack.extentreports.reporter.configuration.Theme;
import com.neurosurgery.hypophysis.utils.TestRecord;
import org.testng.*;
import org.testng.xml.XmlSuite;

import java.util.*;

public class ApiTestIReporterListener implements IReporter {

    private ExtentReports extentReports;
    private int suiteNumber = -1, caseNumber = -1;

    @Override
    public void generateReport(List<XmlSuite> xmlSuites, List<ISuite> suites, String outputDirectory) {
//        本类型自动化测试，通过provider驱动，每次只有一个suite
//        出于扩展性考虑，用for循环遍历
        for (ISuite suite : suites) {
            init(suite.getParameter("project"), suite.getParameter("priority"));

            Map<String, ISuiteResult> result = suite.getResults();
            for (ISuiteResult iSuiteResult : result.values()) {
                List<ITestResult> iTestResults = new ArrayList<ITestResult>();
                ITestContext context = iSuiteResult.getTestContext();
//                因为testng.iTestResults不提供getAllTests()功能
//               将所有用例整合到一个iTestResults列表，并通过suite/case/step进行逐级排序
                iTestResults.addAll(context.getFailedTests().getAllResults());
                iTestResults.addAll(context.getSkippedTests().getAllResults());
                iTestResults.addAll(context.getPassedTests().getAllResults());
                iTestResults.sort(new Comparator<ITestResult>() {
                    @Override
                    public int compare(ITestResult r1, ITestResult r2) {
                        TestRecord testRecord1 = (TestRecord) r1.getParameters()[0];
                        TestRecord testRecord2 = (TestRecord) r2.getParameters()[0];
                        if (testRecord1.getSuite().getNumber() != testRecord2.getSuite().getNumber()) {
                            return testRecord1.getSuite().getNumber() - testRecord2.getSuite().getNumber();
                        } else if (testRecord1.getCase().getNumber() != testRecord2.getCase().getNumber()) {
                            return testRecord1.getCase().getNumber() - testRecord2.getCase().getNumber();
                        } else {
                            return testRecord1.getStep().getNumber() - testRecord2.getStep().getNumber();
                        }
                    }
                });
                ExtentTest[] extentTests = new ExtentTest[3];
                for (ITestResult iTestResult : iTestResults) {
//                所有case逐条插入reportstestNG\target\surefire-reports
                    addSuitesToReports(iTestResult, extentTests);
                }
//                这一段不知所云
                for (String s : Reporter.getOutput()) {
                    extentReports.setTestRunnerOutput(s);
                }
                extentReports.flush();
            }
        }
    }

    private void init(String project, String priority) {
        this.suiteNumber = -1;
        this.caseNumber = -1;
        ExtentHtmlReporter htmlReporter = new ExtentHtmlReporter(String.format("target/surefire-reports/ExtentReports_%s.html", project));
        htmlReporter.config().setResourceCDN(ResourceCDN.EXTENTREPORTS);
        htmlReporter.config().setDocumentTitle("自动化测试报告");
        htmlReporter.config().setReportName(String.format("测试环境：%s  项目：%s", priority, project));
        htmlReporter.config().setChartVisibilityOnOpen(true);
        htmlReporter.config().setTestViewChartLocation(ChartLocation.TOP); //图表位置
        htmlReporter.config().setTheme(Theme.STANDARD);
        htmlReporter.config().setCSS(".node.level-1  ul{ display:none;} .node.level-1.active ul{display:block;}");

        extentReports = new ExtentReports();
        extentReports.attachReporter(htmlReporter);
        extentReports.setReportUsesManualConfiguration(true);
    }

    private void addSuitesToReports(ITestResult iTestResult, ExtentTest[] extentTests) {
        TestRecord testRecord = (TestRecord) iTestResult.getParameters()[0];
        if (testRecord.getSuite().getNumber() != this.suiteNumber) {
            // 如果suitenumber！=testrecore.suite.number
//                说明本testRecord是新的Suite，故应该添加新node
//                否则不添加新node，传入case的还是上一条Suite的node
            extentTests[0] = extentReports.createTest(testRecord.getSuite().getName()).assignCategory(testRecord.getSuite().getName()); //显示方法名称
            //                修改堆栈信息
//                TODO 改成堆栈形式
            this.suiteNumber = testRecord.getSuite().getNumber();
//                suite改变后，需要重置caseNumber，
// 避免前后casenumber都是1的情况，误以为同一条case
            this.caseNumber = -1;
        }
        this.addCaseToSuites(iTestResult, extentTests);
    }

    private void addCaseToSuites(ITestResult iTestResult, ExtentTest[] extentTests) {
        TestRecord testRecord = (TestRecord) iTestResult.getParameters()[0];
        if (testRecord.getCase().getNumber() != this.caseNumber) {
            // 如果casenumber！=testrecore.case.number
//                说明本testRecord是新的Case，故应该添加新node
//                否则不添加新node，传入step的还是上一条Case的node
            extentTests[1] = extentTests[0].createNode(testRecord.getCase().getName()).assignCategory(testRecord.getSuite().getName());//显示Case名称
            this.caseNumber = testRecord.getCase().getNumber();
        }
        this.addStepToCase(iTestResult, extentTests);
    }

    private void addStepToCase(ITestResult iTestResult, ExtentTest[] extentTests) {
        TestRecord testRecord = (TestRecord) iTestResult.getParameters()[0];
        extentTests[2] = extentTests[1].createNode(testRecord.getStep().getName()).assignCategory(testRecord.getStep().getName());//显示Case名称

        for (String group : iTestResult.getMethod().getGroups()) {
            extentTests[2].assignCategory(group); //根据group
        }

        if (iTestResult.getThrowable() != null) {
            extentTests[2].log(Status.ERROR, testRecord.getDetails() + iTestResult.getThrowable()); //异常案例，显示log到报告
        } else {
            Status s = Status.ERROR;
            switch (iTestResult.getStatus()) {
                case 1:
                    s = Status.PASS;
                    break;
                case 2:
                    s = Status.FAIL;
                    break;
                case 3:
                    s = Status.SKIP;
                    break;
                default:
                    s = Status.ERROR;
                    break;
            }
            extentTests[2].log(s, testRecord.getDetails());
        }

        extentTests[2].getModel().setStartTime(getTime(iTestResult.getStartMillis()));
        extentTests[2].getModel().setEndTime(getTime(iTestResult.getEndMillis()));
        extentTests[2].getModel().setDescription("测试案例执行！");
    }

    private Date getTime(long millis) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(millis);
        return calendar.getTime();
    }
}