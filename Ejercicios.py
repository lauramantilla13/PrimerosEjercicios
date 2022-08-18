#Primer Ejercicio
def staircase(n):
    contador = 0
    while contador < n:
        contador = contador + 1
        if n>0 and n<=100:
            espacios = n - contador
            print((" " * espacios)+ ("#" * contador))
        
staircase(6)

#Segundo Ejercico
def sherlockAndAnagrams(s):
    contador = 0
    for i in range(1, len(s)):
        d={}
        for j in range(len(s)-i+1):
            ss = "".join(sorted(s[j:j+i]))
            if ss not in d:
                d[ss]=1
            else:
                d[ss]+=1
            contador += d[ss]-1
    return contador

sherlockAndAnagrams("abba")

#Tercer Ejercicio
from itertools import combinations

def shortPalindrome(s):
    s = s.lower()
    m = (10**9 + 7) 
    n_tuplas = 0
    s1= []
    for i in s:
        if s.count(i) >= 2:
            s1.append(i)
    comb = combinations(s1, 4)
    for i in comb:
        if i[-1]==i[0] and i[1]==i[2]:
             n_tuplas+=1
    return n_tuplas%m

shortPalindrome("kkkkkkz")