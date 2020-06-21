package com.neurosurgery.hypophysis.mapper;


import com.neurosurgery.hypophysis.model.ContextVo;
import com.neurosurgery.hypophysis.model.RequestHeaderVo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
@Mapper
public interface ContextMapper {

    @Select("SELECT name,value,step_id FROM context WHERE step_id = #{step}")
    Set<ContextVo> findContextsByStep(@Param("step") Integer step);
}

