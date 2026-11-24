a=int(input("Nhap so nguyen duong a: "))
while a<=0:
    a=int(input("Nhap lai so nguyen duong a: "))
else:
    for i in range(1,a+1):
        if a%i==0:
            print(i, end=" ")
