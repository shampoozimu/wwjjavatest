package com.neurosurgery.hypophysis.mapper;

import com.neurosurgery.hypophysis.model.StepPo;
import org.apache.ibatis.annotations.*;
import org.apache.ibatis.mapping.FetchType;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface StepMapper {
    //step必须有序
    @Results({
            @Result(property = "requestHeaderVoSet", column = "id", one = @One(select = "com.neurosurgery.hypophysis.mapper.RequestHeaderMapper.findRequestHeadersByStep", fetchType = FetchType.LAZY)),
            @Result(property = "requestParameterVoSet", column = "id", many = @Many(select = "com.neurosurgery.hypophysis.mapper.RequestParameterMapper.findRequestParametersByStep", fetchType = FetchType.LAZY)),
            @Result(property = "contextVoSet", column = "id", many = @Many(select = "com.neurosurgery.hypophysis.mapper.ContextMapper.findContextsByStep", fetchType = FetchType.LAZY)),
            @Result(property = "expectedVo", column = "id", one = @One(select = "com.neurosurgery.hypophysis.mapper.ExpectedMapper.findExpectedByStep", fetchType = FetchType.LAZY)),
            @Result(property = "equivalenceVos", column = "id", many = @Many(select = "com.neurosurgery.hypophysis.mapper.EquivalenceMapper.findEquivalencesByStep", fetchType = FetchType.LAZY))
    })
    @Select("SELECT step.id,api.name,number,method_type.name method,content_type.name contentType,api.path,api" +
            ".cookies,request_body.value body FROM step  LEFT JOIN api ON step.api = api.id   LEFT JOIN method_type " +
            "ON step.method = method_type.id  LEFT JOIN content_type ON step.content_type = content_type.id  LEFT " +
            "JOIN request_body ON step.id = request_body.step_id   WHERE case_id = #{case_id} order by number asc")
    List<StepPo> findStepsByCase(Integer case_id);
}

