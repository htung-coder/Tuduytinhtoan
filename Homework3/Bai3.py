a=int(input("Nhap so nguyen duong a: "))
while a<=0:
    a=int(input("Nhap lai so a nguyen duong: "))
else:
    for i in range(1,11):
        m=a*i
        print(f"{a}x{i}={m}")
