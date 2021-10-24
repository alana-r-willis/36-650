def Pal(st, x, y) :
    if (x == y):
        return True
    if (st[x] != st[y]) :
        return False
    if (x < y + 1) :
        return Pal(st, x + 1, y - 1);
 
    return True
 
def isPalindrome(st) :
    n = len(st)
    if (n == 0) :
        return True
     
    return Pal(st, 0, n - 1);
 
 
st = "kayak"
if (isPalindrome(st)) :
    print ("Yes")
else :
    print ("No")