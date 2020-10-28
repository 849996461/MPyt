

import re
import numpy as np

def readList() -> list:
    with open("../../temp.txt", 'r', encoding="utf-8") as file:
        arr = file.read().split("\n")
    for idx,line in enumerate(arr):
        arr[idx] = list(line.split("[\s\t]+"))
    return arr



def bigTunderline(s:str)->str:
    res = ''
    for c in s:
        if c.isupper():
            c = '_'+c
        c = c.upper()
        res+=c
    return res

def createSqlField(name:str,type:str):
    realType = ''
    isNull = 'DEFAULT NULL'
    if name.lower() == 'id':
        isNull = "NOT NULL"
    if type.lower() == "integer":
        realType = 'decimal(11,0)'
    elif type.lower() == "string":
        realType = 'varchar(63)'
    elif type.lower() == "date":
        realType = 'datetime'
    elif type.lower() == "long":
        realType = 'decimal(19,0)'
    res = f'`{name}` {realType} {isNull} ,'
    return res

def createSqlHead(tableName:str,content:str) -> str:
    res = f'CREATE TABLE `{bigTunderline(tableName)}` (\n{content} PRIMARY KEY (`ID`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    return res


def mysqlToracle(sql:str,schema:str):
    #
    res = ''

    #获取表名
    tableName = re.search("CREATE TABLE `(\w+)` \(",sql).group(1).upper()
    res += f"CREATE TABLE \"{schema}\".\"{tableName.upper()}\" (\n"

    #获取字段名
    id = None
    for field ,type , isNull in re.findall("`(\w+)` (.+?) (.+?),",sql):
        #处理类型
        if type.startswith('varchar'):
            type = type.replace("varchar","VARCHAR2")
        if type.startswith('int') or type.startswith('decimal'):
            type = re.sub(r"int|decimal","NUMBER",type)
        if type.startswith('datetime'):
            type = type.replace("datetime","DATE")

        #处理not null
        if isNull != "NOT NULL":
            isNull = ''
        else:
            if not id:
                id = field
        res+= f"\"{field.upper()}\" {type} {isNull},\n"

    res+= f"CONSTRAINT {tableName} PRIMARY KEY({id}) \n )"
    return res


if __name__ == '__main__':
    with open("../../temp.txt", "r", encoding="utf-8") as file:
        print(mysqlToracle(file.read(),"TERMINAL"))

