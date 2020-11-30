import re

#唯一参数
sql = """
CREATE TABLE `T_ORDER_CMD` (
  `CMD_EXECUTED_ID` decimal(19,0) NOT NULL DEFAULT '0',
  `TASK_ID` decimal(19,0) DEFAULT NULL,
  `NE_ID` decimal(19,0) DEFAULT NULL,
  `BATCH_NUM` decimal(9,0) DEFAULT NULL,
  `CMD_SEQ` decimal(9,0) DEFAULT NULL,
  `CMD_` varchar(8191) DEFAULT NULL,
  `REMARK_` varchar(1024) DEFAULT NULL,
  `LINE_NUM` decimal(9,0) DEFAULT NULL,
  `SOURCE_` decimal(1,0) DEFAULT NULL COMMENT '1、DT文件\r\n            2、人工输入',
  `DISPATCHER_TIME` datetime DEFAULT NULL,
  `COST_` decimal(9,0) DEFAULT NULL,
  `CMD_DISPATCHER_STATUS` decimal(1,0) DEFAULT NULL COMMENT '1、等待下发\r\n            2、下发中\r\n            3、下发完成\r\n            ',
  `RESULT_` decimal(1,0) DEFAULT NULL COMMENT '1、正常\r\n            2、异常',
  `DESCR_` varchar(512) DEFAULT NULL,
  `SESSION_ID` varchar(36) DEFAULT NULL,
  `BREAK_POINT` decimal(1,0) DEFAULT NULL,
  `EXCEPTION_CONTINUE` decimal(1,0) DEFAULT NULL COMMENT '1、执行错误继续  2、执行错误中断',

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


def getTableName():
    return re.search("(?i)create table `(\w+)`",sql).group(1).upper()


def getSelectAll():
    tableName = getTableName()

    field: str
    fList = list()
    pList = list()
    #获取所有属性
    for field in re.findall("(?m)`(\w+)`.*,", sql):
        prop = field.lower()
        i: re.Match
        for i in reversed(list(re.finditer("_(\w)",prop))):
            prop = prop[:i.start()] + i.group(1).upper() + prop[i.end():]
        prop = prop.replace("_","")
        pList.append(prop)
        fList.append(field)
    print('<insert id="batchSave" parameterType="java.util.List">')
    print(f"\tINSERT INTO {tableName} (")
    for i,v in enumerate(fList):
        print(f"\t\t`{v}`{','if i!=len(fList)-1 else ''}")
    print(
"""\t)
\tvalues
\t<foreach collection="list" item="item" separator="," index="index">
\t(""")
    for i,v in enumerate(pList):
        print(f"\t\t#{{item.{v}}}{','if i!=len(fList)-1 else ''}")
    print(
"""\t)
\t</foreach>
</insert>
"""
    )


if __name__ == '__main__':
    getSelectAll()
