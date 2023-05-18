def Increment(n):
    try:
        return int(n)+1
    except:
        raise ValueError('Invalid Input - Vinit')
n='34'
print(Increment(n))