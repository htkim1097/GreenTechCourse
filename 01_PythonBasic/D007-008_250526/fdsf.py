def main():
    d = { 1:100, 2:200 }
    lst = [ {1:100}, {2:200, 3:300} ]
    dd = {1: 100 }
    now = {}
    now[1] = 100

    if now in lst:
        print("ttt")
        print(lst[lst.index(now)])

    for i in d:
        i = 99

    print(d)

    print(dd.popitem()[1])




main()
