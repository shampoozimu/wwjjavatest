package com.neurosurgery.hypophysis.utils;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

import java.util.Map;

public class JsonUtils {
    private JSONObject jsonObject;
    private JSONArray jsonArray;

    public JsonUtils(String jsonString) {
        this.jsonObject = JSON.parseObject(jsonString);
    }

    public JsonUtils(JSONObject jsonObject) {
        this.jsonObject = jsonObject;
    }

    public JsonUtils(JSONArray jsonArray) {
        this.jsonArray = jsonArray;
    }

    public boolean contains(String strSubset) {
        Object jsonSubSet = JSON.parse(strSubset);
        if (jsonSubSet instanceof JSONObject) {
            return this.contains((JSONObject) jsonSubSet);
        } else if (jsonSubSet instanceof JSONArray) {
            return this.contains((JSONArray) jsonSubSet);
        } else {
            throw new ClassCastException(String.format("无法转换成JSON：%s", strSubset));
        }
    }

    private boolean contains(JSONObject subset) {
        boolean result = true;
        for (Map.Entry<String, Object> entry : subset.entrySet()) {
            if (this.jsonObject.containsKey(entry.getKey())) {
                if (entry.getValue() instanceof JSONObject) {
                    result &= new JsonUtils(this.jsonObject.getJSONObject(entry.getKey())).contains(subset.getJSONObject(entry.getKey()));
                } else if (entry.getValue() instanceof JSONArray) {
                    result &= new JsonUtils(this.jsonObject.getJSONArray(entry.getKey())).contains(subset.getJSONArray(entry.getKey()));
                } else if (entry.getValue() instanceof Object) {
                    result &= this.jsonObject.get(entry.getKey()).equals(entry.getValue());
                } else {
                    result &= this.jsonObject.get(entry.getKey()) == entry.getValue();
                }
            } else {
                return false;
            }
        }
        return result;
    }

    /**
     * 判断subset是否⊆this.jsonArray
     *
     * @param subset 被包含的数组
     * @return ⊆:true/⊊:false
     */
    private boolean contains(JSONArray subset) {
        return subset.stream().allMatch(element -> this.included(element));
    }

    /**
     * 判断element是否∈this.jsonArray
     *
     * @param element 数组中的元素
     * @return ∈:true/∉:false
     */
    private boolean included(Object element) {
        boolean result = false;
        for (Object superElement : this.jsonArray) {
            if (element instanceof JSONArray) {
                result |= new JsonUtils((JSONArray) superElement).contains((JSONArray) element);
            } else if (element instanceof JSONObject) {
                result |= new JsonUtils((JSONObject) superElement).contains((JSONObject) element);
            } else if (element instanceof Object) {
                result |= superElement.equals(element);
            } else {
                result |= superElement == element;
            }
        }
        return result;
    }
}
