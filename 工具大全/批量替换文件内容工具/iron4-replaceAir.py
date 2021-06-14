
from fileT import *
import time
# 正则 -- 替换后的值 ,
pts = """
\.lang3--'.lang4'
"""
if __name__ == '__main__':
    #路径
    modPath = r"D:\workspace\idea\gd-cts-gcp-udap\Codes\Backend\gd-cts-gcp-udap-apollo-dispatcher\src\main\java\org\apache\commons\lang4"
    ptns = getPatterns(pts, "--")

    #文件名
    for file in listPath(modPath,".*\.java"):
        ctx = readFile(file)
        ctx = replaceByPatterns(ctx,ptns)
        print(ctx)
        writeFile(file,ctx)











