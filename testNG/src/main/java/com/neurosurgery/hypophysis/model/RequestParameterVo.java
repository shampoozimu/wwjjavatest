package com.neurosurgery.hypophysis.model;


import lombok.Data;

import java.io.Serializable;

@Data
public class RequestParameterVo implements Serializable {
    private int id;
    private String name,value;
    @Override
    public String toString() {
        return this.name + "=" + this.value;
    }
}