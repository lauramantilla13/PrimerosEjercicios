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
    contador = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[j] == s[k]:
                    contador += s[k+1:].count(s[i])
    print(contador%((10**9)+7))

shortPalindrome("ghhggh")