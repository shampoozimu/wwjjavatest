package com.neurosurgery.hypophysis.mapper;


import com.neurosurgery.hypophysis.model.ContextVo;
import com.neurosurgery.hypophysis.model.ExpectedVo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
@Mapper
public interface ExpectedMapper {
    @Select("SELECT value,step_id FROM expected WHERE step_id = #{step}")
    ExpectedVo findExpectedByStep(@Param("step") Integer step);
}

