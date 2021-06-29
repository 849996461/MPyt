import re


class Column:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type


class Table:

    def __init__(self, tableName: str):
        self.columns = []
        self.tableName = tableName

    def __str__(self):
        return "123"


sql = """
create table O_REPORT_COMMON 
(
   ID                   NUMBER               not null,
   STAT_DATE            DATE,
   TIME_DIMENSION       NUMBER,
   TYPE_DIMENSION       NUMBER,
   SYS_NAME             VARCHAR2(64),
   USER_NAME            VARCHAR2(64),
   MANAGER_NAME         VARCHAR2(64),
   MANAGER_IP           VARCHAR2(64),
   NE_NAME              VARCHAR2(64),
   DEVICE_TYPE          VARCHAR2(64),
   VENDOR               VARCHAR2(64),
   CMD_TOTAL            NUMBER,
   NE_NUM               NUMBER,
   NE_FAIL_NUM          NUMBER,
   NE_ALWAYS_FAIL_NUM   NUMBER,
   NE_SUCCESS_RATE      NUMBER(1,5),
   CONNECT_TIMES        NUMBER,
   FAIL_TIMES           NUMBER,
   SUCCESS_RATE         NUMBER(1,5),
   QUIT_ACTIVE_TIMES    NUMBER,
   QUIT_PASSIVE_TIMES   NUMBER,
   FAIL_DETAIL          VARCHAR2(64),
   FAIL_WEIGHT          NUMBER(1,5),
   constraint PK_O_REPORT_COMMON primary key (ID)
);
"""

"""
创建table
"""


def readOracleSql(sql: str) -> Table:
    t = Table(re.search(r"create table `?(\w+)`?", sql).group(1).upper())
    columns = []
    for column, type, _ in re.findall(r"(?m)^\s+([A-Z]\w+)\s+(\w+(\(.+\))?)", sql):
        columns.append(Column(column, type))
    t.columns = columns
    return t


if __name__ == '__main__':
   print(readOracleSql(sql))
