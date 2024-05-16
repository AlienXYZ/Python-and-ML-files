import random
import math
teamlist=[]
n=int(input("Total number of teams/players : "))
q=int(input("Number of teams/players playing in every match : "))
num=math.factorial(n)
den1=math.factorial(n-q)
den2=math.factorial(q)
den3=math.factorial(n-q-q)
c=num/(den1*den2)
d=den1/(den2*den3)
for i in range(n):
    print("Name of team ",i+1," : ",end="")
    a=input()
    while a in teamlist:
        print("Same name cannot be entered. Enter new name for team ",i+1," : ",end="")
        a=input()
    teamlist.append(a)
teamlistloop=teamlist.copy()
m=0
while m<c:
    teamlist=teamlistloop.copy()
    a1=[]
    matchlist=[]
    for i in range(q):
        t=random.choice(teamlist)
        a1.append(t)
        teamlist.remove(t)
    a1.sort()
    matchlist.append(a1)
    m=1
    while m<c:
        a2=[]
        for i in range(q):
            t=random.choice(teamlist)
            a2.append(t)
            teamlist.remove(t)
        a2.sort()
        if a2 in matchlist:
            for element in a2:
                teamlist.append(element)
            continue
        matchlist.append(a2)
        m=m+1
        for element in a1:
            teamlist.append(element)
        a1=a2.copy()
        e=0
        a3=[]
        while e<d:                      #if there is no 'new' match possible with teams left in the teamlist, then we need to discard that complete matchlist and start over again
            z=random.sample(teamlist,q) #there will be [(n-q) choose (q)] combinations among teams in teamlist and so we need to check for each of the combination
            z.sort()                    #hence 'e' is number of matches that we randomly are selecting now from remaining n-q teams in teamlist, that already exists in matchlist
            if z not in a3:             #if e becomes [(n-q) choose (q)] i.e 'd', then it means that ALL possible matches selected from n-q teams already exist in the matchlist and no new combination is possible
                if z in matchlist:      #this would mean that we would not get the desired 'complete' output and hence we need to discard the complete matchlist
                    a3.append(z)        #this process would continue until we get m=(n choose q) i.e the desired 'complete' output is received
                    e=e+1               #problem arises when a 'complete' output (getting n choose q matches) is not possible, e.g: we cannot get 4c2=6 matches for 4 teams, 2 teams playing in each match; we would get only 2 matches and it would be incomplete
                    continue            #for such cases, program does not give any output whereas I want it to display a message that no such tournament will be possible for the given combination of n and q
                break
            continue
        if e==d:
            break
for i in range(m):
    print("Match ",i+1," will be played between : ",end="")
    for element in matchlist[i]:
        print(":",element,end=" ")
    print()