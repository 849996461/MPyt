
import os
from os import path
import re
import time


#递归查找文件 , 文件名支持正则
def listPath(fp:str , fileFilter:str,depth = 10,fileList = [])->[str]:
    dir = ''
    fileName = ''
    if depth < 0:
        return fileList
    if path.exists(fp):
        dir, fileName = path.split(fp)
    else:
        return fileList
    if path.isdir(fp):
        for i in os.listdir(fp):
            listPath(f"{fp}\\{i}",fileFilter,depth-1,fileList)
    elif path.isfile(fp) :
        if re.match(fileFilter,fileName,flags=re.I):
            fileList.append(fp)
    return fileList

def getTime():
    return time.strftime("%Y%m%d-%H%M%S", time.localtime())

#写入文件
def writeFile(filePath:str,ctx:str,bak=False):
    if bak and path.isfile(filePath):
        dir,file = path.split(filePath)
        fileName , etx = path.splitext(file)
        dir = dir if dir else '.'
        writeFile(f"{dir}/{fileName}_{getTime()}_bak{etx}",readFile(filePath))
        print(f"成功写入文件{file}")

    with open(filePath, 'w', encoding="utf-8") as file:
        file.write(ctx)
        file.flush()

def readFile(filePath:str) -> str:
    with open(filePath, 'r', encoding="utf-8") as file:
        ctx = file.read()
        file.close()
        return ctx

#替换文件
def replaceFile(fp:str,pattern,replace:str):
    with open(fp,'r',encoding="utf-8") as file:
        ctx = file.read()
        writeFile(fp+"_bak", ctx)
    ctxRe = re.sub(pattern, replace, ctx)
    writeFile(fp,ctxRe)


def getPatterns(s:str,split:str):
    return { temp[0]:temp[1] for ptn in s.split("\n") if ptn and len(temp:=ptn.split(split)) > 1 }


def replaceByPatterns(ctx:str,ptnSplits:dict, log = False):
    # 代码
    eva:str
    for ptn, eva in ptnSplits.items():
        findList = reversed(list(re.finditer(ptn, ctx)))
        for i in findList:
            print(f" 替换前的值 = {ctx[i.start(0):i.end(0)]}" ,end= "  -- ")
            if  eva.find("g1") == -1:
                sub = str(eval(eva))
            else:
                dict = {var.group(): i.group(int(var.group(1))) for var in re.finditer(r"g(\d+)", eva)}
                sub = str(eval(eva,dict))
            ctx = ctx[:i.start(0)] + sub + ctx[i.end(0):]
            print(f" 替换后的值 = {ctx[i.start(0):i.start(0)+len(sub)]}")
    return ctx




tempFile = r'D:\Game\Grim Dawn\Grim Dawn\mods\FCZ\database\records\skills\devotion\tier1_17d.dbr'



if __name__ == '__main__':
    paths = r"""
        C:\Users\84999\Documents\Paradox Interactive\Hearts of Iron IV\mod\temp\common\technologies\air_doctrine.txt
        C:\Users\84999\Documents\Paradox Interactive\Hearts of Iron IV\mod\temp\common\technologies\infantry.txt
        C:\Users\84999\Documents\Paradox Interactive\Hearts of Iron IV\mod\temp\common\technologies\land_doctrine.txt
        C:\Users\84999\Documents\Paradox Interactive\Hearts of Iron IV\mod\temp\common\technologies\naval_doctrine.txt
    """
    filePath = [path.strip() for path in re.split("\n",paths) if path.strip()]
    print(filePath)
    # listPath(filePath, 1)
    for file in filePath:
        replaceFile(file,'(?si)XOR.*?{.*?}','')



