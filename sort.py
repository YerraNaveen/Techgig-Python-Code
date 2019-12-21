import sys
def main():

    inputFile = open("input.txt", 'r')
    lineList = inputFile.readlines()
    lineList.sort()
    outputFile = open("output.txt",'w')
    print(lineList,"",file= outputFile)

    outputFile.close()
main()
