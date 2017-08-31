numero = list(range(10))
maior = []
menor = []
for x in range(10):
    numero[x] = int(input("Digite um número: "))
for x in range(10):
    if(numero[x]<10):
        menor.append(numero[x])
print("São menores que dez: ", menor)
for x in range(10):
    if(numero[x]>10):
        maior.append(numero[x])
print("São maiores que dez: ",maior)
