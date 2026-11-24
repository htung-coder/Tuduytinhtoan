a=int(input("Nhap so nguyen duong a: "))
s=0
while a<=0:
    a=int(input("Nhap lai so nguyen duong a: "))
else:
    for i in range(1,a):
        if a%i==0:
            s+=i
    if s==a:
        print(f"{a} la so hoan hao.")
    else:
        print(f"{a} khong la so hoan hao.")
        