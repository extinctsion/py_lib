if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    # set removes the replications and list() converts the map into list

    # arr.sort sorts the numbers
    arr.sort()
    # arr[-2] prints the second last element of the list
    print(arr[-2])
    
