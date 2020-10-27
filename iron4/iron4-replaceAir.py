
from MPyt.fileT import *
import time
pts = """
naval_strike_attack\s+?=\s+?(\d+\.?\d+)--float(g1)*10
air_superiority\s+?=\s+?(\d+\.?\d+)--float(g1)*10
build_cost_ic\s+?=\s+?(\d+\.?\d+)--float(g1)*10
manpower\s+?=\s+?(\d+\.?\d+)--float(g1)*5
air_bombing\s+?=\s+?(\d+\.?\d+)--float(g1)*10
air_ground_attack\s+?=\s+?(\d+\.?\d+)--float(g1)*10
fuel_consumption\s+?=\s+?(\d+\.?\d+)--float(g1)*5
"""
if __name__ == '__main__':
    # 唯一参数
    modPath = r"C:\Users\84999\Documents\Paradox Interactive\Hearts of Iron IV\mod\adorable_heart193"
    ptns = getPatterns(pts, "--")

    for file in listPath(modPath+"/common/units/equipment",".*air.*"):
        ctx = readFile(file)
        ctx = replaceByPatterns(ctx,ptns)
        writeFile(file,ctx)









