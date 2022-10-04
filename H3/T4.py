# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec2bin(value):
    res = ""
    v=abs(value)
    neg = True if value<0 else False
    while(v>1):
        res+=str(v%2)
        v=int(v/2)
    res+="1-" if neg else "1"
    res=res[::-1]
    return res

while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        print("Wrong input, integer number expected")
        continue
    print(dec2bin(n))
    break