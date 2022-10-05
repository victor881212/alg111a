import random
#cn取k個
rancnk=[]
def c(n,k):
    li1=[]
    fin=[]
    for i in range(0,n):
        li1.append(i)
    
    li2=li1
    for i in range(0,k):
        fin.append(li2.pop(random.randint(0,len(li2)-1)))
    fin.sort()
    return fin

def pcnk(n,k):
    for i in range(n*100):
        a=c(n,k)
        if a not in rancnk:
            rancnk.append(a)
    rancnk.sort()
    return rancnk
print(pcnk(10,3))