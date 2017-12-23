def calculateInverse(num):
    print("hello")


def eeaPrep(a, b, d):
    if d%gcd(a, b) != 0:
        return 0
    
    if a == 0 or b == 0:
        return 0

    swap = False
    aNeg = False
    bNeg = False

    if a < 0:
        a = -a
        aNeg = True

    if b < 0:
        b = -b
        bNeg = True
    
    if a < b:
        a, b = b, a
        swap = True
    
    x, y = extendedEuclidianAlgorithm(1, 0, 0, 1, a, b)

    if aNeg:
        x = -x
    if bNeg:
        y= -y
    if swap:
        x, y = y, x
    return (x, y)

def extendedEuclidianAlgorithm(x1, x2, y1, y2, a, b):
    if b == 0:
        return x1, y1
    q = int(a/b)
    x1, x2 = x2, x1-q*x2
    y1, y2 = y2, y1-q*y2
    a, b = b, a%b
    print(x1, x2, y1, y2, a, b)
    return extendedEuclidianAlgorithm(x1, x2, y1, y2, a, b)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


a = 100
b = 60

print(eeaPrep(a, b, 20))
