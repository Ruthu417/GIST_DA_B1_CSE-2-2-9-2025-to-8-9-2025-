# some functions on the no.s
def is_prime(n):
    fc=0
    for v in range(1,n+1):
        if n%v==0:
            fc+=1
    if fc==2:
        return True
    else:return False
       
#is_prime(13)
def is_perfect(n):
    #sum of the factors=n(itself)-->6=1+2+3
    fs=0
    for v in range(1,n):
        if n%v==0:
            fs+=v
    if fs==n:
        return True
    else:
        return False
    
#is_perfect(6)
def is_even(n):
    if n%2 is 0:
        return True
    else:return False
    
#is_even(5)
        