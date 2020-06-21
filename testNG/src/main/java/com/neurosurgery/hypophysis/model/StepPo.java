package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;
import java.util.Collection;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

@Data
public class StepPo implements Serializable {
    private int number;
    private String name, method, contentType, body, path;
    private boolean cookies;
    private Set<RequestHeaderVo> requestHeaderVoSet;
    private Set<RequestParameterVo> requestParameterVoSet;
    private Set<ContextVo> contextVoSet;
    private ExpectedVo expectedVo;
    private Collection<EquivalenceVo> equivalenceVos;
}