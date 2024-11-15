frase1= input().split()
frase2= input().split()

set1=set()
set2=set()
set3=set()   


for texto in frase1:
    set1.add(texto)

for i in frase2:
    set2.add(i)

for i in set1:
    if i in set2:
        set3.add(i)

texto=""

for comum in set3:
    texto += f"{comum} "

print(texto.strip())  




   
        