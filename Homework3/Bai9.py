a=int(input("Nhap so nguyen duong a: "))
s=a**0.5
while a<=0:
    a=int(input("Nhap lai so nguyen duong a: "))
else:
    if s.is_integer():
        print(f"{a} la so chinh phuong.")
    else:
        print(f"{a} khong la so chinh phuong.")
