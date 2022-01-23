import re
def Isvalid(number):
    total_sum = 0
    for i, num in enumerate(reversed(number)):
        num = int(num) 
        if i % 2 == 1:
            num = num*2
            if num >= 10:
                total_sum += num//10 + num%10
            else:
                total_sum += num
        else:
            total_sum += num
    return total_sum % 10 == 0

def cardtype(N):
    a=int(N[0]) ; b=int(N[0:2])
    if b>49 and b<56:return"**MasterCard**"
    if b==34 or b==37:return "**America Express**"
    if b in [60,62,64,65]:return "**Discover**"
    if a==4:return "**VISA**"


nc="5465407274645021"
print(Isvalid(nc), cardtype(nc)) 