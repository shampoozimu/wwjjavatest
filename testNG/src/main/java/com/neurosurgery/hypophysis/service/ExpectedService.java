package com.neurosurgery.hypophysis.service;

import com.alibaba.fastjson.JSON;
import org.apache.commons.lang3.StringUtils;
import org.bson.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * 预期值组件
 *
 * @author 市三女中的生理卫生男老湿, December 01, 2015
 */

@Service
public class ExpectedService {
    @Autowired
    private MongoTemplate mongoTemplate;

    //express形式：
    //mongo:collectionName:{"name":1,"type":10}
    public String generate(String express) {
        String result = null;
        String[] db = express.split(":");
        switch (db[0]) {
            case "mongo":
                result = this.mongo(express);
                break;
            case "mysql":
                break;
            default:
                result = express;
                break;
        }
        return result;
    }

    //express形式：
    //collectionName:{"name":1,"type":10}
    private String mongo(String express) {
        String[] db = express.split(":");
        String collectionName = db[0];
//生成查询条件
        Criteria criteria = new Criteria();
        Query query = new Query();
        for (Map.Entry<String, Object> qs : JSON.parseObject(db[1]).entrySet()) {
            String v = qs.getValue().toString();
            query.addCriteria(criteria.and(qs.getKey()).is(StringUtils.isNumeric(v) ? Double.valueOf(v) : v));
        }
//        生成查询结果
        Collection<Document> documents = mongoTemplate.find(query, Document.class, collectionName);
        String[] docArray = documents.stream().map(doc -> doc.toJson()).collect(Collectors.toList()).toArray(new String[documents.size()]);
        return String.format("[%s]", String.join(",", docArray));
    }
}
