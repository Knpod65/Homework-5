import random
mlist=[]
rlist=[]
A=(input("1st: "))
mlist.append(A)
B=(input("2st: "))
mlist.append(B)
C=(input("3rd: "))
mlist.append(C)
D=(input("4th: "))
mlist.append(D)
for i in range(24):
    random.shuffle(mlist)
    E=int(mlist[0]+mlist[1]+mlist[2]+mlist[3])
    rlist.append(E)
print("[",A," ,",B," ,",C," ,",D,"], the largest formed number is",max(rlist))