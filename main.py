altura = float(input('qual é a sua altura em cm: '))
peso =float(input('seu peso em kg: '))

IMC = peso / (altura/100)**2
print(IMC)

if IMC < 18.5:
    print(f'seu IMC é de {IMC},e é classified como meagre')


elif IMC >= 18.5 and IMC < 24.9:
 print(f'seu IMC e de {IMC},é classificado como normal')

elif IMC >=25 and IMC < 29.9:
 print(F'seu IMC é de {IMC}, é classificado como sobrepeso')

elif IMC >= 30 and IMC < 39.9:
    print(f'seu imc é de {IMC}, é classificado como obesidade')

else:
    print("pode parar de comer e começar a malhar! obesidade grave ")