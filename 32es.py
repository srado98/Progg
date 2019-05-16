import sys

def szampiramis(n):
    RStr = ""
    n+=1
    for i in range(1,n):
        for j in range(n-i):
            RStr += " "
        for j in range(1,i):
            RStr+= str(j)
        for i in range(i,0,-1):
            RStr+=str(i)
        RStr+= "\n"
    return RStr

def usage():
    print("Használat: ./32es.py szám")
    exit(1)

def main():
    argc=len(sys.argv)
    if (argc < 2):
        usage()
    n=0
    try:
        n= int(sys.argv[1])
    except:
        usage()
    try:
        with open("piramis.txt", "w+") as f:
            f.write(szampiramis(n))
    except:
        print("Fájlkezelési hiba")
        exit(2)
main()