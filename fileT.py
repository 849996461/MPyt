
import os
from os import path
import re



fileList = []

fileFilter = ".*"



#递归查找文件 , 文件名支持正则
def listPath(fp:str , depth:int)->[str]:
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
            listPath(f"{fp}\\{i}",depth-1)
    elif path.isfile(fp) :
        if re.match(fileFilter,fileName,flags=re.I):
            fileList.append(fp)
    return fileList

#写入文件
def writeFile(filePath:str,ctx:str):
    with open(filePath, 'w', encoding="utf-8") as file:
        file.write(ctx)
        file.flush()

#替换文件
def replaceFile(fp:str,pattern,replace:str):
    with open(fp,'r',encoding="utf-8") as file:
        ctx = file.read()
        writeFile(fp+"_bak", ctx)
    ctxRe = re.sub(pattern, replace, ctx)
    writeFile(fp,ctxRe)



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



