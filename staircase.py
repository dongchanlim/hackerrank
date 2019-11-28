def staircase(n):
    ls = [" " for i in range(n)]
    for i in range(len(ls)):
        ls[len(ls)-i-1] = "#"
        print(*ls, sep = "")

if __name__ == '__main__':
    n = int(input(""))
    staircase(n)
    
def staircase(n):
    ls = []
    for i in range(n):
        print(" " * (n-1-i) + "#" * (i))
        
staircase(10)