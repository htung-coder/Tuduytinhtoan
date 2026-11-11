a, b, c=map(int, input().split())
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print(f"Dien tich tam giac la: {s:.1f}")
else:
    print("Khong phai 3 canh cua tam giac.")