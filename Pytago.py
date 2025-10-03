import math

side = input ("chọn cạnh cần tính: ")
if side == "a":
    b = float(input( " b ="))
    c = float(input( " c ="))
    a = math.sqrt (c**2 -b**2)
    print(f"độ dài cạnh a là {a}")
elif side == "b":
     a = float(input( " a ="))
     c = float(input( " c ="))
     b = math.sqrt (c**2 -a**2)
     print(f"độ dài cạnh b là {b}")
elif side == "c":
     a = float(input( "a ="))
     b = float(input( "b ="))
     c = math.sqrt(a**2 + b**2)
     print(f"độ dài cạnh c là {c}")
