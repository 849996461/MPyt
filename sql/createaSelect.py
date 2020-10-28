import re

#唯一参数
sql = """
CREATE TABLE `t_common_dictionary` (
  `ID` decimal(19,0) NOT NULL,
  `VENDOR_ID` decimal(19,0) DEFAULT NULL,
  `VENDOR_NAME` varchar(32) DEFAULT NULL,
  `DEVICETYPE_ID` decimal(19,0) DEFAULT NULL,
  `NE_TYPE` varchar(32) DEFAULT NULL,
  `CMD_` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


def getTableName():
    return re.search("(?i)create table `(\w+)`",sql).group(1).upper()


def getSelectAll():
    tableName = getTableName()
    field: str
    for field in re.findall("(?m)`(\w+)`.*,", sql):
        prop = field.lower()
        i: re.Match
        for i in reversed(list(re.finditer("_(\w)",prop))):
            prop = prop[:i.start()] + i.group(1).upper() + prop[i.end():]
        prop = prop.replace("_","")
        print(f"{tableName}.{field} as {prop} , ")


if __name__ == '__main__':
    getSelectAll()
