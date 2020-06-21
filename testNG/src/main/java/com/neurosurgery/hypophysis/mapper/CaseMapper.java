package com.neurosurgery.hypophysis.mapper;

import com.neurosurgery.hypophysis.model.CaseModule;
import com.neurosurgery.hypophysis.model.CasePo;
import org.apache.ibatis.annotations.*;
import org.apache.ibatis.mapping.FetchType;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface CaseMapper {
    @Results(id = "steps", value = {
            @Result(property = "stepPoList", column = "id", many = @Many(select = "com.neurosurgery.hypophysis.mapper.StepMapper.findStepsByCase", fetchType = FetchType.LAZY))
    })
    //case可以无序  排序为了报表美观
    @Select("select id, name,number,priority from casee where suite_id = #{suite} order by number asc")
    List<CasePo> findCasesBySuite(Integer suite);

    @Results(id = "module", value = {
            @Result(property = "stepPoList", column = "id", many = @Many(select = "com.neurosurgery.hypophysis" +
                    ".mapper.StepMapper.findStepsByCase", fetchType = FetchType.LAZY)),
            @Result(property = "suiteVo", column = "suite_id", one = @One(select = "com.neurosurgery.hypophysis" +
                    ".mapper.SuiteMapper.findSuiteById", fetchType = FetchType.LAZY)),
            @Result(property = "projectVo", column = "{id=project_id,priority=priority}", one = @One(select = "com" +
                    ".neurosurgery.hypophysis.mapper.ProjectMapper.findProjectByPriorityAndId", fetchType = FetchType.LAZY))
    })
    @Select("select casee.id, casee.name,casee.number,suite_id,project_id,priority from casee inner join suite on " +
            "suite_id = suite.id where casee.id = #{id}")
    CaseModule findCaseModuleById(Integer id);
}

