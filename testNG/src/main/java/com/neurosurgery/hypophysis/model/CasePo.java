package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;
import java.util.List;

@Data
public class CasePo implements Serializable {
    protected short number,priority;
    protected String name;
    protected List<StepPo> stepPoList;
}