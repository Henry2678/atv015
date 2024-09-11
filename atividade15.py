# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
def calcular(numero1, numero2, operaçao):
    if operacao == "soma":
        return numero1 + numero2
    elif operacao == "subtracao":
        return numero1 - numero2
    elif operacao == "multiplicacao":
        return numero1 * numero2
    elif operacao == "divisao":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return"erro: divisao por zero!"
    else:
        return "operacao invalida" 
numero1 = float(input("digite o primeiro numero "))
numero2 = float(input("digite o segundo numero ")) 
operacao = str(input("digite a operacao (soma, subtracao, multiplicacao, divisao )"))
resultado = calcular(numero1, numero2, operacao)
print(f"o resultado da operacao e {resultado}")   




