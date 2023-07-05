import operator
i = input("Expression ").replace(" ","")
op = {
"+": operator.add,
"-": operator.sub,
"/": operator.truediv,
"*": operator.mul}
z = ""
x = ""
y = ""

for _ in i:
    if _ in op:
        y += _
    elif bool(y) is True:
        z += _
    else:
        x += _

sol = op[y]
print(float(sol(int(x),int(z))))