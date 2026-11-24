n=int(input("Nhap chieu cao tam giac can: "))
while n<=0:
    n=int(input("Nhap lai chieu cao duong: "))
else:
    for i in range(1,n+1):
        if i==1:
            print(" " * (n-i) + "*")
        elif i==n:
            print("*" * (2*i-1))
        else:
            ngoai= " " * (n-i)
            trong= " " * (2*i-3)
            print(ngoai + "*" + trong + "*")
