import sys

VPython=sys.version_info[0]==2          # This check if python's version is 2.x
if VPython:
    input=raw_input  

factors=lambda n:[x for x in range(1,n+1) if not n%x]
isprime=lambda n: len(factors(n))==2
primefactors = lambda n: list(filter(isprime, factors(n)))

def PrimeFactorize(n):
    f=primefactors(n)
    if isprime(n):
        return str(n)
    else:
        return f"{f[0]} * {PrimeFactorize(n/f[0])}"

def main():
    print("Enter the numbers in the prompt or type 'quit' to exit")
    while True:
        print(">>>", end='')
        num=input()
        if num=='quit':
            break
        try:
            num=int(num)
            print(PrimeFactorize(num))
        except:
            print("Please insert an int number")
            continue
        

if __name__=="__main__":
    main()