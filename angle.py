import math
def main():
    ab = int(input())
    bc = int(input())
    ac = math.sqrt(ab*ab + bc*bc)
    ad = dc = ac/2
    A  = math.asin(bc/ac)
    bd = math.sqrt(ab * ab + ad*ad -2*ab*ad*math.cos(A))
    B=(ab*ab + bd*bd - ad*ad)/(2*ab*bd)
    ABD = math.acos(B)*180/math.pi
    print(round(ABD),end='')
main()
