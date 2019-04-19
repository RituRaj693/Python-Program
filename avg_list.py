n = int(input('enter the size of list'))
list = []
for i in range (0,n):
    elem = int(input('enter the element'))
    list.append(elem)
avg = sum(list)/n
print('average of list',round(avg,2))



