package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;

@Data
public class ExpectedVo implements Serializable {
    private int id;
    private String value;
}