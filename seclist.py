a = []
n = int(input('enter the lenghth of list'))
for i in range(1,n):
    b = int(input('enter tyhe element of list :'))
    a.append(b)
a.sort()
print('second largest numbaer',a[n-2])
