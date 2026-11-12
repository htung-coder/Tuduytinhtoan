a, b, c=map(float, input().split())
if a==0:
    print("Nhập lại a khác 0.")
else:
    delta=b**2-4*a*c
    if delta<0:
        print("Phương trình vô nghiệm.")
    elif delta==0:
        x=-b/(2*a)
        print(f"Phương trình có nghiệm kép x1=x2={x:.2f}.")
    else:
        x1=(-b+delta**0.5)/(2*a)
        x2=(-b-delta**0.5)/(2*a)
        print(f"Phương trình có 2 nghiệm phân biệt x1={x1:.2f} và x2={x2:.2f}.")
        