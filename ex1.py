'''
Faça um programa que receba uma lista de genes e uma única função de regulação simples, 
que não contém o operador or (' | ') e imprima uma lista dos estados estados que podem ativar o suposto gene.

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função: !A&B
['010', '011']

'''

genes = input('Nomes dos genes (separados por vírgula): ').replace(
    ' ', '').strip().split(',')
function = input('Função: ')

n = len(genes)
graph = function.split('&')

activations = []

for i in range(2 ** n):
    state = bin(i)[2:].rjust(n, '0')
    values = {k: int(v) for k, v in zip(genes, state)}

    result = True

    for item in graph:
        if(result == False):
            break
        if item.startswith('!'):
            result = result and not bool(values[item.replace('!','')])
        else:
            result = result and bool(values[item])

    if result:
        activations.append(state)

print(activations)
