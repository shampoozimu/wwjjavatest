package com.neurosurgery.hypophysis.config;

import com.alibaba.druid.pool.DruidDataSource;
import lombok.Data;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;

import javax.sql.DataSource;
import java.sql.SQLException;

/**
 * @ProjectName zhaxinle
 * @Author: zeroJun
 * @Date: 2018/8/16 16:49
 * @Description: 主数据源配置类
 */
@Data
@Configuration
@ConfigurationProperties(prefix = "cingulate.datasource.druid")
@MapperScan(basePackages = "com.neurosurgery.hypophysis.mapper", sqlSessionFactoryRef = "cingulateSqlSessionFactory")
public class CingulateDataBaseConfig {
//    private String filters = "stat";
//    private String url = "jdbc:mysql://rm-m5eu4m6a4rugr22fcno.mysql.rds.aliyuncs.com/api_test?characterEncoding=utf-8&useSSL=false&serverTimezone=UTC";
//    private String username = "api_test";
//    private String password = "xpkpCJvFuzZHCiaA";
//    private String driverClassName = "com.mysql.cj.jdbc.Driver";
//    private int initialSize =1;
//    private int minIdle =1;
//    private int maxActive =10;
//    private long maxWait = 6000;
//    private long timeBetweenEvictionRunsMillis = 6000;
//    private long minEvictableIdleTimeMillis = 30000;
//    private String validationQuery = "SELECT 'x'";
//    private boolean testWhileIdle =true;
//    private boolean testOnBorrow =  false;
//    private boolean testOnReturn =false;
//    private boolean poolPreparedStatements = false;
//    private int maxPoolPreparedStatementPerConnectionSize = 20;

    private String filters;
    private String url;
    private String username;
    private String password;
    private String driverClassName;
    private int initialSize;
    private int minIdle;
    private int maxActive;
    private long maxWait;
    private long timeBetweenEvictionRunsMillis;
    private long minEvictableIdleTimeMillis;
    private String validationQuery;
    private boolean testWhileIdle;
    private boolean testOnBorrow;
    private boolean testOnReturn;
    private boolean poolPreparedStatements;
    private int maxPoolPreparedStatementPerConnectionSize;

    // 主数据源使用@Primary注解进行标识
    @Primary
    @Bean(name = "cingulateDataSource")
    public DataSource cingulateDataSource() throws SQLException {
        DruidDataSource druid = new DruidDataSource();
        // 监控统计拦截的filters
        druid.setFilters(filters);

        // 配置基本属性
        druid.setDriverClassName(driverClassName);
        druid.setUsername(username);
        druid.setPassword(password);
        druid.setUrl(url);

        //初始化时建立物理连接的个数
        druid.setInitialSize(initialSize);
        //最大连接池数量
        druid.setMaxActive(maxActive);
        //最小连接池数量
        druid.setMinIdle(minIdle);
        //获取连接时最大等待时间，单位毫秒。
        druid.setMaxWait(maxWait);
        //间隔多久进行一次检测，检测需要关闭的空闲连接
        druid.setTimeBetweenEvictionRunsMillis(timeBetweenEvictionRunsMillis);
        //一个连接在池中最小生存的时间
        druid.setMinEvictableIdleTimeMillis(minEvictableIdleTimeMillis);
        //用来检测连接是否有效的sql
        druid.setValidationQuery(validationQuery);
        //建议配置为true，不影响性能，并且保证安全性。
        druid.setTestWhileIdle(testWhileIdle);
        //申请连接时执行validationQuery检测连接是否有效
        druid.setTestOnBorrow(testOnBorrow);
        druid.setTestOnReturn(testOnReturn);
        //是否缓存preparedStatement，也就是PSCache，oracle设为true，mysql设为false。分库分表较多推荐设置为false
        druid.setPoolPreparedStatements(poolPreparedStatements);
        // 打开PSCache时，指定每个连接上PSCache的大小
        druid.setMaxPoolPreparedStatementPerConnectionSize(maxPoolPreparedStatementPerConnectionSize);

        return druid;
    }

    // 创建该数据源的事务管理
    @Primary
    @Bean(name = "cingulateTransactionManager")
    public DataSourceTransactionManager cingulateTransactionManager() throws SQLException {
        return new DataSourceTransactionManager(cingulateDataSource());
    }

    // 创建Mybatis的连接会话工厂实例
    @Primary
    @Bean(name = "cingulateSqlSessionFactory")
    public SqlSessionFactory cingulateSqlSessionFactory(@Qualifier("cingulateDataSource") DataSource cingulateDataSource) throws Exception {
        final SqlSessionFactoryBean sessionFactory = new SqlSessionFactoryBean();
        sessionFactory.setDataSource(cingulateDataSource);  // 设置数据源bean
//        sessionFactory.setMapperLocations(new PathMatchingResourcePatternResolver()
//                .getResources(CingulateDataBaseConfig.MAPPER_LOCATION));  // 设置mapper文件路径

        return sessionFactory.getObject();
    }
}
