import itertools
def main():
    aa = input().strip().split()
    bb = input().strip().split()
    bb.append(9)
    cc = list(itertools.product(aa,bb))
    '''for i in range (0, len(cc)):
        if(i == (len(cc)-1)):
            print(cc[i], end="")
        else:
            print(cc[i], end=" ")'''
    for i in range(len(cc)):
        print(cc[i],end='')
        if(i!=len(cc)-1):
            print(" ",end='')
    #print(cc)
main()