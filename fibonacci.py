#algoritme primer fibonacci

n = 2
x = 1
y = 1

while n<1000:
    tmp = x
    x = y + x
    y = tmp
    print("Volta n.",n,":",x)
    n+=1
