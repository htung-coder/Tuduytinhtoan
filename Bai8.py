ten=input("Ten chu ho: ")
cstt=int(input("Chi so thang truoc: "))
cstn=int(input("Chi so thang nay: "))
sd=cstn-cstt
tien=0
if sd>400:
    tien=sd*3460*1.08
elif sd>300:
    tien=(sd-300)*3350*1.08
    tien+=(100*2998+100*2380+50*2050+50*1984)*1.08
elif sd>200:
    tien=(sd-200)*2998*1.08
    tien+=(100*2380+50*2050+50*2050)*1.08
elif sd>100:
    tien=(sd-100)*2380*1.08
    tien+=(50*2050+50*1984)*1.08
elif sd>50:
    tien=(sd-50)*2050*1.08
    tien+=50*1984*1.08
else:
    tien=sd*1984*1.08
print(f"Ho va ten: {ten}")
print("Tien phai tra la:",round(tien))


