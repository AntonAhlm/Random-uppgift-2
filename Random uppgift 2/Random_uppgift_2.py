import random
krona=[]
slant=["krona","klave"]
for i in range(1,101): 
    tal1=random.choice(slant)
    print("Omgang ",i, ":",tal1)
    if tal1=="klave":
        krona.append(1)

print("Antal krona :",sum(krona))
