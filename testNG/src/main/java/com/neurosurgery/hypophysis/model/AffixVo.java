package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;

@Data
public class AffixVo implements Serializable {
    private int affix, number, caseId;
    private short type,timeout;
}
