package com.neurosurgery.hypophysis.utils;

import java.util.*;
import java.lang.Math;
import java.util.stream.Collectors;

import groovy.lang.IntRange;
import groovy.lang.Range;
import org.apache.commons.lang3.RandomUtils;
import org.apache.commons.lang3.RandomStringUtils;
import org.apache.commons.lang3.StringUtils;
import org.springframework.util.CollectionUtils;

/**
 * 生成几乎所有模式的字符集
 * <p>
 * ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
 * <p>
 * 一般情况下，中文不会与数字和字母合用
 * <p>
 * 由于汉字覆盖2万多个区间，而数字和字母覆盖区间不到100
 * <p>
 * 一旦混合生成，随机数平均分布情况下将会极不均衡
 * <p>
 * TODO 使用Set的自然随机、解决全局平均分布、混合平衡分布、放回与不放回抽样的问题
 * <p>
 * ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
 *
 * @author 市三女中的生理卫生男老师, February 01,2016
 */

public class RandomUtil {

    private static final Range<Integer> NUMBER_RANGE = new IntRange(48, 57), UPPER_CASE_RANGE = new IntRange(65, 90), LOW_CASE_RANGE = new IntRange(97, 122), CHINESE_RANGE = new IntRange(19968, 40891);

    private static final String NUMBER_PATTERN = ".*\\d.*", UPPER_CASE_PATTERN = ".*[A-Z].*", LOW_CASE_PATTERN = ".*[a-z].*", CHINESE_PATTERN = ".*#.*";

    /**
     * 构造方法，解析字符串模式
     *
     * @param randomExpressionRules 随机模式
     *
     *                  <pre>
     *                                                                                                                                                                                                                                                                                                                                    直接赋值：A1		= "A1"
     *                                                                                                                                                                                                                                                                                                                                    固定长度随机字符：A0{5}	= "Z89YU"
     *                                                                                                                                                                                                                                                                                                                                    包含排除字符：Aa0#{3}eoc6	= "B3k"
     *                                                                                                                                                                                                                                                                                                                                               </pre>
     */


    /**
     * 返回指数密度分布的随机数
     *
     * @param range 随机数取值范围[1->range]
     */
    public static double exponentialDensity(double range) {
        // 取对数
        range = Math.log(range);
        // 对数后平均分布
        range *= 1 - Math.random();
        // 再取指数
        range = Math.exp(range);
        // 实现1-range的指数分布
        return range;
    }

    /**
     * 生成单位随机数
     *
     * @param randomExpressionRules 随机模式
     *                              <p>
     *                              直接赋值：A1		= "A1"
     *                              <p>
     *                              固定长度随机字符：A0{5}	= "Z89YU"
     * @return 生成的随机数(字符串)
     */

    public static String randomGenerator(RandomExpressionRule... randomExpressionRules) {
        StringBuffer sb = new StringBuffer();
        // pat:Aa0#{3}eoc6
        for (RandomExpressionRule randomExpressionRule : randomExpressionRules) {
            sb.append(randomGenerator(randomExpressionRule));
        }
        return sb.toString();
    }

    public static String randomGenerator(RandomExpressionRule expressionRule) {
        // 用{}将字符串分隔开
        Collection<Character> excludedChars = CollectionUtils.arrayToList(expressionRule.exclude.toCharArray());
        Collection<Character> includedChars = getIncludedChars(expressionRule.pattern);

        includedChars.removeAll(excludedChars);
        return RandomStringUtils.random(15, StringUtils.join(includedChars, ""));
    }

    /**
     * 生成数字、字母、中文所对应的编码区域
     *
     * @param pattern 随机模式
     * @return 以数组形式返回编码区间
     */
    private static Collection<Character> getIncludedChars(String pattern) {

        Collection<Integer> indexRange = new HashSet<Integer>();

        if (pattern.matches(NUMBER_PATTERN)) {
            indexRange.addAll(NUMBER_RANGE);
        }
        if (pattern.matches(UPPER_CASE_PATTERN)) {
            indexRange.addAll(UPPER_CASE_RANGE);
        }
        if (pattern.matches(LOW_CASE_PATTERN)) {
            indexRange.addAll(LOW_CASE_RANGE);
        }
        if (pattern.matches(CHINESE_PATTERN)) {
            indexRange.addAll(CHINESE_RANGE);
        }
        return indexRange.stream().map(e -> (char) e.intValue()).collect(Collectors.toList());
    }

    /**
     * 返回集合中任意元素
     */
    public <T> T getRandomObject(List<T> list) {
        return list.get(RandomUtils.nextInt(0, list.size()));
    }


    public <T> T getRandomObject(T... array) {
        return array[RandomUtils.nextInt(0, array.length)];
    }

    /**
     * 标准随机数表达式类
     * <p>
     * 随机数生成器表达式有三个部分：
     * <p>
     * pattern：随机数生成类型：任意大写字母/任意小写字母/任意数字/#代表中文
     * <p>
     * number：生成的随机数长度
     * <p>
     * exclude：随机数中排除的字符
     */
    private static class RandomExpressionRule {
        private String pattern, number, exclude = "";

        public String getPattern() {
            return pattern;
        }

        public void setPattern(String pattern) {
            this.pattern = pattern;
        }

        public String getNumber() {
            return number;
        }

        public void setNumber(String number) {
            this.number = number;
        }

        public String getExclude() {
            return exclude;
        }

        public void setExclude(String exclude) {
            this.exclude = exclude;
        }
    }

    public static RandomExpressionRule expressionRule(String pattern, String number, String exclude) {
        RandomExpressionRule randomExpressionRule = new RandomExpressionRule();
        randomExpressionRule.pattern = pattern;
        randomExpressionRule.number = number;
        randomExpressionRule.exclude = exclude;
        return randomExpressionRule;
    }

    public static RandomExpressionRule expressionRule(String pattern, String number) {
        return expressionRule(pattern, number, "");
    }
}
