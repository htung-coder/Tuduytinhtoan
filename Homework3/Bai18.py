n=int(input("Nhập số nguyên dương n: "))
while n<=0:
    n=int(input("Nhập lại số nguyên dương n: "))
else:
    a=n
    while a%3==0:
        a//=3
    if a==1:
        print(f"{n} là số dạng 3^k.")
    else:
        print(f"{n} không phải là số dạng 3^k.")
            