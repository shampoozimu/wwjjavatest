package com.neurosurgery.hypophysis.mapper;

import com.neurosurgery.hypophysis.mapper.provider.ParameterSqlProvider;
import com.neurosurgery.hypophysis.model.ParameterVo;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Set;

@Repository
@Mapper
public interface ParameterMapper {

    @SelectProvider(type = ParameterSqlProvider.class, method = "findParametersByProjectAndPriority")
    Set<ParameterVo> findParametersByProjectAndPriority(@Param("project_id") Short project, @Param("priority") Short
            priority);
}

