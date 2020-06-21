package com.neurosurgery.hypophysis.mapper.provider;

import org.apache.ibatis.jdbc.SQL;

import java.util.Map;

public class ParameterSqlProvider {

    /**
     * 方式2：也可以根据官方提供的API来编写动态SQL。
     */
    public String findParametersByProjectAndPriority(Map<String, Object> para) {
        return new SQL() {
            {
                SELECT("name","value");
                FROM("parameter");
                WHERE("project_id = " + para.get("project_id"), "priority = " + para.get("priority"));
            }
        }.toString();
    }
}
