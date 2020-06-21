package com.neurosurgery.hypophysis.model;

import lombok.Data;

import java.io.Serializable;

@Data
public class RequestHeaderVo implements Serializable {
    private int id;
    private String type, value;
    @Override
    public String toString() {
        return this.type + "=" + this.value;
    }
}