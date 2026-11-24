print("Nhập vào dãy số nguyên, nhập -1 để thoát ra:")
n=int(input())
if n==-1:
    print("Không có số nào được nhập.")
else:
    max=n
    min=n
    while True:
        n=int(input())
        if n==-1:
            break
        elif n>max:
            max=n
        elif n<min:
            min=n
print("Số lớn nhất: ", max)
print("Số nhỏ nhất: ",min)

