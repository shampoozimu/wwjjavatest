package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;
import java.util.List;

@Data
public class CaseModule extends CasePo{
    private SuiteVo suiteVo;
    private ProjectVo projectVo;
}