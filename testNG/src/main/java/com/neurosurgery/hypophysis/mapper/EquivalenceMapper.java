package com.neurosurgery.hypophysis.mapper;


import com.neurosurgery.hypophysis.model.EquivalenceVo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
@Mapper
public interface EquivalenceMapper {

    @Select("select name,value from equivalence where step_id = #{step}")
    Set<EquivalenceVo> findEquivalencesByStep(@Param("step") Integer step);
}

