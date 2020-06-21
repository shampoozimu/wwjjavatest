package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;
import java.util.List;

@Data
public class SuiteVo implements Serializable {
    protected int number;
    protected String name;
}
