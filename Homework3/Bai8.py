a, b=map(int, input("Nhap so nguyen duong a va b: ").split())
while a<=0 or b<=0:
    a, b=map(int, input("Nhap lai so nguyen duong a va b: ").split())
else:
    if a>b:
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                print(i, end=" ")
    else:
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                print(i, end=" ")
        