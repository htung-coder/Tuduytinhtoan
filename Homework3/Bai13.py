A=int(input("Nhap so nguyen duong A: "))
while A<=0:
    A=int(input("Nhap lai so nguyen duong A: "))
else:
    s=0
    n=0
    while s+(1/(n+1))<A:
        n+=1
        s+=1/n
    print(f"So n nho nhat can tim la: {n+1}.")
    