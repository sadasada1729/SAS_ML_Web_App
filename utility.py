def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)
    except ValueError:
        return False
    else:
        return True

def isfloat(s):  # 浮動小数点数値を表しているかどうかを判定
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True