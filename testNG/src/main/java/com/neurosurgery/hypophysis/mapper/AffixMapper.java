package com.neurosurgery.hypophysis.mapper;

import com.neurosurgery.hypophysis.model.AffixVo;
import com.neurosurgery.hypophysis.model.AffixLog;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.Collection;
import java.util.List;

@Repository
@Mapper
public interface AffixMapper {
    @Select("SELECT number,pa.case_id,TYPE,ac.id affix,timeout FROM project_affix pa INNER JOIN affix_config ac ON pa" +
            ".case_id = ac.case_id AND project_id = #{project_id} AND priority = #{priority} order by number asc")
    List<AffixVo> findAffixesByProjectAndPriority(@Param("project_id") Short project_id, @Param("priority") Short
            priority);

    @Select("SELECT affix,MAX(end) end FROM affix_log INNER JOIN affix_config ON affix = affix_config.id WHERE affix " +
            "= #{config} GROUP  BY NAME")
    Collection<AffixLog> findAffixLogsByCaseAndConfig(Integer config);

    @Insert({"insert into affix_log(affix, name,value,end) values(#{affix},#{name}, #{value},timestampadd(hour,#{time},current_timestamp))"})
//    @Options(useGeneratedKeys = true, keyProperty = "id")
    void insertAffixLog(Integer affix, String name, String value,Short time);
}

