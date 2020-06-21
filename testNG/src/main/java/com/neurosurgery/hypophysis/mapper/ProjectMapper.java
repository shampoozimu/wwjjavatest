package com.neurosurgery.hypophysis.mapper;

import com.neurosurgery.hypophysis.model.ProjectPo;
import com.neurosurgery.hypophysis.model.ProjectVo;
import org.apache.ibatis.annotations.*;
import org.apache.ibatis.mapping.FetchType;
import org.springframework.stereotype.Repository;

@Repository
@Mapper
public interface ProjectMapper {
    @Results(id = "suites", value = {
//            @Result(property = "id", column = "id"),
            //users映射List<User> users，many=@Many是调用关联查询方法，"id"是关联查询条件，FetchType.LAZY是延迟加载
//            由于只调用parametermap，不会显式触发getParameterVo方法，所以需要Eager
            @Result(property = "parameterMap", column = "{project_id=id,priority=priority}", many = @Many(select =
                    "com.neurosurgery.hypophysis.mapper.ParameterMapper.findParametersByProjectAndPriority",
                    fetchType = FetchType.LAZY)),
            @Result(property = "suitePoList", column = "id", many = @Many(select = "com.neurosurgery.hypophysis.mapper.SuiteMapper.findSuitesByProject", fetchType = FetchType.LAZY)),
            @Result(property = "affixVoList", column = "{project_id=id,priority=priority}", many = @Many(select =
                    "com.neurosurgery.hypophysis.mapper.AffixMapper.findAffixesByProjectAndPriority", fetchType = FetchType.LAZY))
    })
    @Select("select id,name,(select id from priority where name = #{priority}) priority from project where name = #{name}")
    ProjectPo findProjectByPriorityAndName(@Param("priority") String priority, @Param("name") String name);

    @Results(id = "param", value = {
//            @Result(property = "id", column = "id"),
            //users映射List<User> users，many=@Many是调用关联查询方法，"id"是关联查询条件，FetchType.LAZY是延迟加载
//            由于只调用parametermap，不会显式触发getParameterVo方法，所以需要Eager
            @Result(property = "parameterMap", column = "{project_id=id,priority=priority}", many = @Many(select =
                    "com" +
                    ".neurosurgery.hypophysis.mapper.ParameterMapper.findParametersByProjectAndPriority", fetchType = FetchType.LAZY))
    })
    @Select("select id,name,#{priority} priority from project where id = #{id}")
    ProjectVo findProjectByPriorityAndId(@Param("id") Short id, @Param("priority") Short priority);
}

