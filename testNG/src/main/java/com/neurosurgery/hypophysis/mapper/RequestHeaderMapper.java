package com.neurosurgery.hypophysis.mapper;


import com.neurosurgery.hypophysis.model.RequestHeaderVo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
@Mapper
public interface RequestHeaderMapper {

    @Select("SELECT (SELECT name FROM header_type WHERE id = type) type,value FROM request_header WHERE step_id = #{step}")
    Set<RequestHeaderVo> findRequestHeadersByStep(@Param("step") Integer step);
}

