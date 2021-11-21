f = input('Put the file address here')
f = open (fr"{f}",'r')

pn = 0
tags = ["while","for","def","if","elif","else","try","except"]
ln = 0
lines = []

#for when there's a problem 
def problem():
    print("There is a problem in line number " + str(ln))
    global pn
    pn += 1

for i in f:
    lines.append(i.strip())

#for finding dangling parentheses
for l in f:
    p = 0
    ln += 1
    for w in l:
        for c in w:
            if c == "(":
                p += 1
            elif c == ")":
                p -= 1
    if p > 0:
        print("There are " + str(p) + " missing )")
        problem()
    elif p < 0:
        print("There are " + str(0 - p) + " missing (")
        problem()

#for finding missing :
ln = 0
for a in lines:
    ln +=1
    for t in tags:
        if a.split()[0] == t:
            if a.split()[-1][-1] != ":":
                print("There is a missing : for your " + t)
                problem()
    #for finding missing str()
    if a[:5] == "print":
        try:
            d = float(a)
        except:
            d = str(a)
        try:
            d = int(a)
        except:
            d = str(a)
        if isinstance(d,float):
            problem()
        if isinstance(d,int):
            problem()

if pn == 0:
    print("There are no problems")
