import operator

print("Olá, bem-vindo à calculadora!")

a = int(input("Digite o primeiro número: "))

i = str(input("\nAgora selecione a operação desejada: "))

b = int(input("\nDigite o Segundo número: "))

if(i == '+'):
    res = operator.add(a,b)
elif (i == '-'):
    res = operator.sub(a,b)
elif (i == '*'):
    res = operator.mul(a,b)
elif (i == '/'):
    res = operator.truediv(a,b)
else:
    print("Operação Inválida!")
    exit()


print("\nprocessando...")
print(f'\nO Resultado é {res}.')
print("\nObrigado por utilizar!")