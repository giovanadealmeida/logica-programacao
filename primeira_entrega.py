#Pedir para o usuario digitar  dois numeros
num1 = input("Digite primeiro numero: ")
num2 = input('Digite segundo numero: ')

#Converter os numeros para inteiros
num1 = int(num1)
num2 = int(num2)

#Implementos de 4 operacao matematica
soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
resto = num1 % num2

#laco de repeticao
if soma >= divisao and soma >= subtracao and soma >= resto:
  print('soma é maior que todos os outros')
elif soma <= divisao and soma <= subtracao and soma <= resto:
  print('soma é menor que todos os outros')
else:
  print('soma é diferente dos outros')

#Resultado das operacoes matematicas
print('Soma', soma)
print('Divisao',divisao)
print('Subtracao',subtracao)
print('resto',resto)
