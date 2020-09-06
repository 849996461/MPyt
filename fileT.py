
import os
from os import path
import re

filePath = r"D:\Game\Grim Dawn\Grim Dawn\mods\FCZ\database\records\skills\devotion"

fileList = []

fileFilter = ".*"

def listPath():
    pass



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



def replaceFile(fp:str,pattern,replace):
    with open(fp,'r',encoding="utf-8") as file:
        ctx = file.read()
    ctxRe = re.sub(pattern, replace, ctx)
    with open(fp, 'w', encoding="utf-8") as file:
        file.write(ctxRe)
        file.flush()



tempFile = r'D:\Game\Grim Dawn\Grim Dawn\mods\FCZ\database\records\skills\devotion\tier1_17d.dbr'



if __name__ == '__main__':
    for file in listPath(filePath,1):
        replaceFile(file,'skillExperienceLevels.*','skillExperienceLevels,0;10000;20000;35000;55000;80000;120000;170000;300000;350000;400000;450000;500000;600000;750000;900000;1200000;1500000;2000000;2500000;3000000,')



