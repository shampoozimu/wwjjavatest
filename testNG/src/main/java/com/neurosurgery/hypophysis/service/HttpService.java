package com.neurosurgery.hypophysis.service;

import com.neurosurgery.hypophysis.utils.TestRecord;
import org.springframework.stereotype.Service;


@Service
public class HttpService {

    public void exec(TestRecord testRecord) {
        testRecord.execute();
    }
}
