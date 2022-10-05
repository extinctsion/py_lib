if __name__ == '__main__':
    arr = []
    N = int(input())
    for _ in range (N):
        cmd, *nums = input().split()
        num = list(map(int,nums))
        if cmd == "insert":
            arr.insert(num[0],num[1])
        elif cmd == "print":
            print(arr)
        elif cmd == "remove":
            arr.remove(num[0])
        elif cmd == "append":
            arr.append(num[0])
        elif cmd == "sort":
            arr.sort()
        elif cmd == "pop":
            arr.pop()
        elif cmd == "reverse":
            arr.reverse()
