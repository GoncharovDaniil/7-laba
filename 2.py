if __name__ == '__main__':
    lst = tuple(list(map(float, input("Введите элементы списка: ").split())))
    res=0
print(lst)
for i in lst:
    if lst.index(i) % 2 != 0:
        res += i
print("1)""%.2f" % res)
idx=[i for i,j in enumerate(lst) if j<0]
m = (sum(lst[idx[0]+1:idx[-1]]))
print("2)""%.2f" % m)