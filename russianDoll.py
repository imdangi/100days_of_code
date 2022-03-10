# Russian Doll Problem using .... recursion

def russDoll(n):
    if n==1:
        return(f"Doll is completely opened , value of doll {n}")
    else:
        print(f"Doll no {n}")
        return(russDoll(n-1))

n=int(input("Enter the number of dolls in Russian Dolls"))
print(russDoll(n))