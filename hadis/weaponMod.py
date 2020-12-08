from MPyt.fileT import *
from os import path
pts = """
(?s)"WeaponEnchantmentTrait".{,600}RarityLevels--
"""
if __name__ == '__main__':
    # 唯一参数
    modPath = r"D:\Game\Hadis\Hades\Content\Scripts"
    ptns = getPatterns(pts, "--")
    files = listPath(modPath + "", "TraitData.lua")
    print(f"文件数量为 = {len(files)}")
    for file in files:
        p , f = path.split(file)
        print(f"文件名为 = {f}")
        ctx = readFile(file)
        ctx = replaceByPatterns(ctx, ptns)
        # writeFile(file, ctx)
