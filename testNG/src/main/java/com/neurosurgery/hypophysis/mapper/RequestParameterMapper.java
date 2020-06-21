package com.neurosurgery.hypophysis.mapper;


import com.neurosurgery.hypophysis.model.RequestParameterVo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Set;

@Repository
@Mapper
public interface RequestParameterMapper {

    @Select("SELECT name,value FROM request_parameter WHERE step_id  = #{step}")
    Set<RequestParameterVo> findRequestParametersByStep(@Param("step") Integer step);
}

