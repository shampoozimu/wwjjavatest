package com.neurosurgery.hypophysis.utils;

import java.util.*;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.stream.Stream;

import org.apache.commons.lang3.StringUtils;

/**
 * 集合加工类
 *
 * @author 市三女中的生理卫生男老师,December 01, 2015
 */
public class CollectionUtil {
    /**
     * <pre>
     * 字符串转换成队列
     * 该函数主要为导入数据驱动工作流而设计
     * 验车流程按照这个队列依次完成
     * </pre>
     *
     * @param strFlows
     *            工作流字符串 （预约确认>验车派单>验车单变更>交车结案）
     * @return ConcurrentLinkedQueue [预约确认,验车派单,验车单变更,交车结案]
     */
    public static ConcurrentLinkedQueue<String> workFlow2Queue(String strFlows) {
        if (null == strFlows) {
            return null;
        }
        ConcurrentLinkedQueue<String> queueFlows = new ConcurrentLinkedQueue<String>();
        queueFlows.addAll(Arrays.asList(StringUtils.split(strFlows, '>')));
        return queueFlows;
    }

    /**
     * @param strMap
     *            key与value用":"分隔 多个entrySet用";"分隔
     */
    public static Map<String, String> string2Map(String strMap) {
        Map<String, String> map = new HashMap<String, String>();
        Stream.of(strMap.split(";")).forEach(es -> map.put(es.split(":")[0], es.split(":")[1]));
        return map;
    }
}