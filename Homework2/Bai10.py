x0, y0=map(float, input("Nhập tâm đường tròn: ").split())
r=float(input("Nhập bán kính đường tròn: "))
x, y=map(float, input("Nhập điểm A: ").split())
d=((x-x0)**2+(y-y0)**2)**0.5
if d==r:
    print(f"Điểm A({x},{y}) thuộc đường tròn.")
else:
    print(f"Điểm A({x},{y}) không thuộc đường tròn.")
    