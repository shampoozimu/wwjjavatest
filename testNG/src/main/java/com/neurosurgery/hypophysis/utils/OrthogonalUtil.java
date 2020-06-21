package com.neurosurgery.hypophysis.utils;

import org.apache.commons.lang3.RandomUtils;

import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;


public class OrthogonalUtil {
    public Collection simple(Map<String, String[]> table) {
        Collection<Map<String, String>> result = new HashSet<>();

        table.forEach((k, v) -> {
            for (String element : v) {
                Map<String, String> record = new HashMap<>();
                table.forEach((k1, v1) -> {
                    record.put(k1,v1[RandomUtils.nextInt(0,v1.length)]);
                });
                record.put(k, element);
                result.add(record);
            }
        });
        return result;
    }
//
//    public void demo() {
//        Map<String, String[]> demoData = new HashMap<String, String[]>();
//        demoData.put("first", new String[]{"0", "1", "2"});
//        demoData.put("secend", new String[]{"c", "d", "q"});
//        demoData.put("third", new String[]{"$", "……", "！"});
//        simple(demoData);
//    }
}
