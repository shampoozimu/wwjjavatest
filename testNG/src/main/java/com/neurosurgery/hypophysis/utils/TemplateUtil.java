package com.neurosurgery.hypophysis.utils;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


/**
 * 对字符串或外部文本进行处理，参数绑定等
 *
 * @author 市三女中的生理卫生男老师, November 24,2015
 */
public class TemplateUtil {
    // 判断数字正则
    public static final String NUMBER_PATTERN = "^[-+]?((\\d+)([.](\\d+))?)$";
    // 匹配$花括号的内容
    public static final String BETWEEN_$BRACES = "\\$\\{(.*?)\\}";
    // 匹配小括号的内容
    public static final String BETWEEN_BRACKET = "(.*?)\\((.*?)\\)";
    // 环境变量
    public Map<String, String> vars = new HashMap<>(), context = new HashMap<>(), cookie = new HashMap<>();


    public void addVars(Map<String, String> mapVars) {
        mapVars.forEach((k, v) -> this.vars.put(k, this.dataBinding(v)));
    }

    /**
     * 从json串中查找出包含${}的字符串(替换变量)
     * <p>
     * 将该字符串交由getDataBindingValue处理
     *
     * @param origin 原始字符串(整个模板文档(jsonRequest)，不是某个value)
     * @return 处理后的输出字符串
     */
    public String dataBinding(String origin) {
        StringBuffer bindingCallosum = new StringBuffer();
        // group(0)取值包含${}的整个字符串，group(1)取值${}内部字符串
        // 匹配替换，全都包含${}
        Pattern pattern = Pattern.compile(BETWEEN_$BRACES);
        Matcher matcher = pattern.matcher(origin);
        while (matcher.find()) {
            // group(1)取${}内部变量名
            // 替换整个${}标记
            matcher.appendReplacement(bindingCallosum, getDataBindingValue(matcher.group(1)));
        }
        matcher.appendTail(bindingCallosum);
        return bindingCallosum.toString();
    }

    /**
     * 数据绑定方法
     *
     * @param key total_price：从上下文环境中，取total_price对应的value
     *            <p>
     *            vars.domain：从初始环境变量中，取domain对应的value
     *            <p>
     *            random.A0.5.6C：生产成5位大小写字母和数字混合的随机数，排除6和C
     */
    private String getDataBindingValue(String key) {
        String[] contexts = key.split("\\.");
        switch (contexts[0]) {
            case "random":
                return RandomUtil.randomGenerator(RandomUtil.expressionRule(contexts[1], contexts[2], contexts.length < 4 ? "" : contexts[3]));
            case "vars":
                return this.vars.get(contexts[1]);
            default:
                return this.context.get(key);
        }
    }
}
