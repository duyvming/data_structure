#https://blog.csdn.net/u014745194/article/details/72783257       原创

#插入排序
def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        for i in range(j, 0, -1):
            if(alist[i] < alist[i-1]):
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    insert_sort(alist)
    print("新列表为：%s" % alist)