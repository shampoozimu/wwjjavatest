package com.neurosurgery.hypophysis.mapper;

import com.neurosurgery.hypophysis.model.SuitePo;
import com.neurosurgery.hypophysis.model.SuiteVo;
import org.apache.ibatis.annotations.*;
import org.apache.ibatis.mapping.FetchType;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface SuiteMapper {
    @Results(id = "cases", value = {
            @Result(property = "casePoList", column = "id", many = @Many(select = "com.neurosurgery.hypophysis.mapper.CaseMapper.findCasesBySuite", fetchType = FetchType.LAZY))
    })
//          suite按照number排序
    @Select("select id,number,name from suite where project_id = #{project} order by number asc")
    List<SuitePo> findSuitesByProject(Integer project);

    @Select("select number,name from suite where id = #{id}")
    SuiteVo findSuiteById(Integer id);
}

