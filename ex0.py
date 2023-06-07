# Exercício de exemplo para VPL #####
'''
Faça um programa que leia um número inteiro n 
(que representa o número de genes envolvidos num sistema a ser analisado) 
e imprima as combinações possíveis do estado inicial desses genes. 
Exemplo de execução: 

Entre com o número de genes: 2
00
01
10
11

'''

# aqui você vai escrever seu código.
# ao  terminar, aperte o botão do disquete para salvar.
# foguetinho para executar
# check box para avaliar

genes = int(input("Entre com o número de genes: "))

for i in range(2**genes):
    print(bin(i)[2:].rjust(genes,"0"))




