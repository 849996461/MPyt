

from MPyt.fileT import *


# 唯一参数
ptn = """
naval_strike_attack\s+?=\s+?(\d+\.?\d+)--float(g1)*10
air_superiority\s+?=\s+?(\d+\.?\d+)--float(g1)*10
build_cost_ic\s+?=\s+?(\d+\.?\d+)--float(g1)*10
manpower\s+?=\s+?(\d+\.?\d+)--float(g1)*5
air_bombing\s+?=\s+?(\d+\.?\d+)--float(g1)*10
air_ground_attack\s+?=\s+?(\d+\.?\d+)--float(g1)*10
fuel_consumption\s+?=\s+?(\d+\.?\d+)--float(g1)*5
"""


if __name__ == '__main__':

    path = "./temp.txt"
    readFile(path)
    ptns = getPatterns(ptn,'--')
    ctx = readFile(file)
    ctx = replaceByPatterns(ctx,ptns)
    print(ctx)
    # writeFile(file,ctx)
