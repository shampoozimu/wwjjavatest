package com.neurosurgery.hypophysis.model;


import lombok.Data;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

@Data
public class ProjectVo implements Serializable {
    protected int id;
    protected byte priority;
    protected Map<String, String> contextMap = new HashMap<String, String>(), parameterMap;

    public void setParameterMap(Set<ParameterVo> parameterVoSet) {
        this.parameterMap = parameterVoSet.stream().collect(Collectors.toMap(ParameterVo::getName, ParameterVo::getValue));
    }
}
