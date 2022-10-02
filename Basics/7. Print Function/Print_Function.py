# A Simple Code to show the use of Print Function
if __name__ == '__main__':
    n = int(input())
    i=1
    while(i<=n):
        # The end="" avoids the newline produced after print
        print(i,end="")
        i+=1