import sys

sys.setrecursionlimit(100000)

VPython=sys.version_info[0]==2          # This check if python's version is 2.x
if VPython:
    input=raw_input  

def Fibonacci(occurence:int)->int:
    
    '''
        This function will return the Fibonacci Sequence until the given element

        input: occurence -> number of elements that will be showed
    '''

    lisFib=[0]
    while len(lisFib)<occurence:
        if len(lisFib)==1:
            lisFib.append(1)
        else:
            lisFib.append(lisFib[-1]+lisFib[-2])
    lisFib=[str(i) for i in lisFib]
    return (', '.join(lisFib))



def main():
    print("In the shell below Enter the number of elements that should be show or enter quit to exit")

    while True:
        print(">>>", end="")
        entry=input()
        if entry=="quit":
            break
        if not entry.isdigit():
            print("Please insert a number")
        else:
            print(Fibonacci(int(entry)))


if __name__=="__main__":
    main()