import sys
from functions import add, sub , mul , div

n1 = int(sys.argv[1])
operator = sys.argv[2]
n2 = int(sys.argv[3]) 

if operator == '+':
    r = add(n1,n2)
if operator == '-':
    r = sub(n1,n2)
if operator == 'x':
    r = mul(n1,n2)
if operator == '/':
    r = div(n1,n2)

print r 