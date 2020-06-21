package com.neurosurgery.hypophysis.service;

import com.neurosurgery.hypophysis.mapper.AffixMapper;
import com.neurosurgery.hypophysis.mapper.CaseMapper;
import com.neurosurgery.hypophysis.mapper.ProjectMapper;
import com.neurosurgery.hypophysis.model.*;
import com.neurosurgery.hypophysis.utils.OrthogonalUtil;
import com.neurosurgery.hypophysis.utils.TestRecord;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

@Service
public class ProviderService {
    @Autowired
    private ProjectMapper projectMapper;
    @Autowired
    private AffixMapper affixMapper;
    @Autowired
    private CaseMapper caseMapper;
    @Autowired
    ExpectedService expectedService;


    //    数据库格式转换成TestRecord列表
    public List<Object> testRecordProvider(String priority, String project) {

        List testRecordList = new ArrayList();
        ProjectPo projectPo = projectMapper.findProjectByPriorityAndName(priority, project);

        projectPo.getAffixVoList().stream().filter(affix -> affix.getType() == 0).forEach(prefix -> this.prefix(prefix));

        for (SuitePo suitePo : projectPo.getSuitePoList()) {
            for (CasePo casePo : suitePo.getCasePoList()) {
                //case级别必须大于project
                // 例如：project级别为stage(2),只能执行stage和product（3）的case
                // qa（3）级别的case忽略
                if (casePo.getPriority() >= projectPo.getPriority()) {
                    for (StepPo stepPo : casePo.getStepPoList()) {
                        if (stepPo.getEquivalenceVos().isEmpty()) {
                            testRecordList.add(new TestRecord(expectedService, projectPo, suitePo, casePo, stepPo));
                        } else {
//                            生成等价类
                            Map<String, String[]> orthogonal = stepPo.getEquivalenceVos().stream().collect(Collectors.toMap(EquivalenceVo::getName, equivalenceVo -> equivalenceVo.getValue().split(",")));
                            Collection<Map<String, String>> result = new OrthogonalUtil().simple(orthogonal);
                            result.forEach(r -> {
                                TestRecord testRecord = new TestRecord(expectedService, projectPo, suitePo, casePo, stepPo);
                                testRecord.setEquivalence(r);
                                testRecordList.add(testRecord);
                            });
                        }
                    }
                }
            }
        }
        return testRecordList;
    }

    //输入：affixVo对应单个case，包含多个step
    private void prefix(AffixVo affixVo) {
//        一个affixVo对应多个affixLog:context包含多个key-value对
        Collection<AffixLog> affixLogs = affixMapper.findAffixLogsByCaseAndConfig(affixVo.getAffix());

        //TODO
        //临时解决方案
        //任一终止时间在当前时间之前，就要重新执行affix对应的case
        CaseModule caseModule = caseMapper.findCaseModuleById(affixVo.getCaseId());
        caseModule.getStepPoList().forEach(step -> {
            TestRecord testRecord = new TestRecord(expectedService, caseModule, step);
            testRecord.execute();
        });

//        TODO
//        业务逻辑：查找最近一条前置记录
//        如果没有记录或者已超时，则重新生成token，并存入数据库，写入最终时间
//        如果记录未超时，则直接将该记录的key和value记录到templateutil.context中

//        if (affixLogs.stream().noneMatch(af -> af.getEnd().after(Calendar.getInstance().getTime()))) {
////            任一终止时间在当前时间之前，就要重新执行affix对应的case
//            CaseModule caseModule = caseMapper.findCaseModuleById(affixVo.getCaseId());
//            caseModule.getStepPoList().forEach(step -> {
//                TestRecord testRecord = new TestRecord(expectedService, caseModule, step);
//                testRecord.execute();
//                TestRecord.templateUtil.context.forEach((name, value) -> {
//                            affixMapper.insertAffixLog(affixVo.getAffix(), name, value, affixVo.getTimeout());
//                        }
//                );
//            });
//        }else{
//
//        }
    }
}
