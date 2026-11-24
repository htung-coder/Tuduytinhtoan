n=int(input("Nhap so nguyen duong n: "))
s=0
while n<=0:
    n=int(input("Nhap lai so nguyen duong n: "))
else:
    if n==1:
        print("Khong co so nguyen duong k nao thoa man.")
    else:
        s=0
        k=0
        while s+(k+1)<n:
            k+=1
            s+=k
    print(f"De S(k) lon nhat nhung nho hon {n} thi k={k}.")

