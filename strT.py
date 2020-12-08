
import re

#不包含 idx 当前字符
def getLastNLine(content:str,idx:int,num:int)->str:
    if idx >= len(content):return
    temp = content[:idx]
    regex = "(?s)(\n?[^\n]*){"+str(num)+"}$"
    return re.search(regex,temp).group().strip()

