package com.neurosurgery.hypophysis;

import com.neurosurgery.hypophysis.service.HttpService;
import com.neurosurgery.hypophysis.service.ProviderService;
import com.neurosurgery.hypophysis.utils.TestRecord;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.testng.AbstractTestNGSpringContextTests;
import org.testng.ITestContext;
import org.testng.annotations.*;

import java.lang.reflect.Method;
import java.util.Iterator;


@SpringBootTest
//@MapperScan(basePackages = {"com.neurosurgery.hypophysis.mapper"})
public class ApiAutomationTests extends AbstractTestNGSpringContextTests {
    private String priority, project;

    @Autowired
    HttpService httpService;
    @Autowired
    ProviderService providerService;


    @Parameters({"priority", "project"})
    @BeforeSuite
    public void initParameters(String priority, String project) {
        this.priority = priority;
        this.project = project;
    }


    @Test(dataProvider = "provider")
    public void exec(TestRecord testRecord) {
        httpService.exec(testRecord);
    }

    @DataProvider(name = "provider")
    public Iterator<Object> provider(ITestContext iTestContext, Method method) {
        return providerService.testRecordProvider(this.priority, this.project).iterator();
    }
}
