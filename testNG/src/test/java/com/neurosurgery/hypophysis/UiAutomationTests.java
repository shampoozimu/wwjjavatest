package com.neurosurgery.hypophysis;


import com.alibaba.fastjson.JSONObject;
//import macaca.client.MacacaClient;
import static org.hamcrest.Matchers.containsString;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.testng.AbstractTestNGSpringContextTests;

import org.testng.Assert;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;



@SpringBootTest
public class UiAutomationTests extends AbstractTestNGSpringContextTests {
//    MacacaClient driver = new MacacaClient();
//
//
//    //mvn clean test  -Dpriority=99 -Dproject=openapi,seller
////    https://www.cnblogs.com/melody-emma/p/5033270.html
//    @BeforeSuite
//    public void exec() throws Exception {
//        JSONObject porps = new JSONObject();
//        porps.put("autoAcceptAlerts", true);
//        porps.put("browserName", "chrome");
//        porps.put("platformName", "desktop"); // android or ios
//        porps.put("javascriptEnabled", true);
//        porps.put("platform", "ANY");
//        JSONObject desiredCapabilities = new JSONObject();
//        desiredCapabilities.put("desiredCapabilities", porps);
//        driver.initDriver(desiredCapabilities).setWindowSize(1280, 800)
//                .get("https://macacajs.github.io/");
//    }
//
//    @Test
//    public void test_case_1() throws Exception {
//        driver
//                .elementById("kw")
//                .sendKeys("macaca");
//
//        driver.elementById("su")
//                .click();
//
//        String html = driver.source();
//
////        Assert.assertEquals(html, containsString("macaca"));
//    }
//
//    @Test
//    public void test_case_2() throws Exception {
//        System.out.println("test case #2");
//    }
//
//    @AfterSuite
//    public void tearDown() throws Exception {
//        driver.quit();
//    }

}
