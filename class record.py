def main():
    n = int(input())
    '''s1 = input()
    m1 = int(input())
    sub1 = sub1 + m1
    m2 = int(input())
    sub2 = sub2 + m2
    m3 =int(input())
    sub3 = sub3 + m3
    m4 = int(input())
    sub4 = sub4 + m4
    m5 = int(input())
    sub5 = sub5 + m5
    print(sub1/2)'''
    s1 = input().split() 
    s2 = input().split()
    for i in range(1,6):
        s1[i] = float(s1[i])
        s2[i] = float(s2[i])
    m1 =(s1[1]+s2[1])/n
    m2 = (s1[2]+s2[2])/n
    m3 = (s1[3]+s2[3])/n
    m4 = (s1[4]+s2[4])/n
    m5 = (s1[5]+s2[5])/n
    print("{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format(m1,m2,m3,m4,m5),end='')
main()

