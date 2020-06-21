package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;
import java.sql.Date;

@Data
public class AffixLog implements Serializable {
    private int affix;
    private Date end;
}
