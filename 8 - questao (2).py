import os

idade: int; somaIdade: int; mediaIda: float; idade50: int
peso: float; peso60:float
altura: float; somaAltura: float; alturaAbaixo150:int
corDeOlho: str; somaCorOlhoAzul: int
corDeCabelo: str; somaCorCabeloRuivo: int
corDeCabeloRuiSOlhoA: int
qtdCad: int

idade = 0 
idade50 = 0
somaIdade = 0
mediaIda = 0
peso = 0
peso60 = 0
altura = 0
somaAltura = 0
alturaAbaixo150 = 0
somaCorOlhoAzul = 0
somaCorCabeloRuivo = 0
corDeCabeloRuiSOlhoA = 0

os.system('cls')
qtdCad = int(input('Informe quantos cadrastros seram realizados: '))
print('=' * 47)

for n in range(1, qtdCad + 1):

    print(f'{n}º pessoa')

    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura: '))
    corDeOlho = str(input('Digite a cor dos seus olhos(A-azul;P-preto;V-verde e C-castanho): '))
    corDeCabelo = str(input('Digite a cor do seu cabelo (P-preto;C-castanho;L-louro e R-ruivo): '))

    if idade > 50:
        idade50 += 1
    if peso < 60:
        peso60 += 1
    if altura < 1.50:
        somaIdade += idade
        mediaIda += 1
    if corDeOlho == 'A':
        somaCorOlhoAzul += 1
    if corDeOlho != 'A' and corDeCabelo == "R":
        corDeCabeloRuiSOlhoA += 1

    

print(f'Esta e a quantidade de pessoas informadas que tem idade acima de 50 {idade50}. Foram informadas  {peso60} pessoas com peso inferior a 60kg')

if idade50 <= 0:
    print(f'Não foram informadas pessoas acima de 50 anos. Foram informadas {peso60} pessoas com peso inferior a 60kg')
elif peso60 <= 0:
    print(f'Esta e a quantidade de pessoas que tem idade acima de 50 {idade50}. Não foram informadas pessoas com o peso abaixo de 60kg')
else:
     print(f'Nao foram informadas pessoas acima de 50 anos. Não foram informadas pessoas com o peso abaixo de 60kg')

if somaIdade == 0:
    print(f'Não foram informadas pessoas com menos de 1.50')
else:
    print(f'Média das idades das pessoas com altura inferior a 1.50 é {somaIdade/mediaIda * 100:.2f}%')


if somaCorOlhoAzul <=0:
    print(f'Não foram informadas pessoas com olhos azuis')
else:
    print(f'A porcentagem de pessoas informadas com olhos azuis é {somaCorOlhoAzul/n * 100:.2f}%')

if corDeCabeloRuiSOlhoA <= 0:
    print("Não foram informadas pessoas com cabelo ruivo sem olhos azuis")
else:
    print(f'Foram iformadas {corDeCabeloRuiSOlhoA} pessoas com cabelo ruivo que nao contém olhos azuis ')