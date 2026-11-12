a, b, m=map(float, input("Nhập phương trình một: ").split())
c, d, n=map(float, input("Nhập phương trình hai: ").split())
D=a*d-b*c
Dx=m*d-n*b
Dy=a*n-c*m
if D!=0:
    x=Dx/D
    y=Dy/D
    print(f"Hệ phương trình có nghiệm là: ({x:.2f};{y:.2f}).")
else:
    if Dx==0 and Dy==0:
        print("Hệ phương trình có vô số nghiệm.")
    elif Dx!=0 or Dy!=0:
        print("Hệ phương trình vô nghiệm.")
        