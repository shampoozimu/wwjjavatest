package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.util.List;

@Data
public class SuitePo extends SuiteVo {
    private List<CasePo> casePoList;
}
