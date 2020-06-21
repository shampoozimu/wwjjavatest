package com.neurosurgery.hypophysis.model;

import lombok.Data;
import java.util.List;

@Data
public class ProjectPo extends ProjectVo {
    private List<SuitePo> suitePoList;
    private List<AffixVo> affixVoList;
}
