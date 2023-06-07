fgenes = input('Nomes dos genes (separados por vírgula): ').replace(' ', '').strip().split(',')

activations = {}

for gene in genes:
  condition = input(f'Função para {gene}: ').replace('!', 'not').replace('&', 'and').replace('|', 'or')

  activations[gene] = eval(f'lambda {genes}: {condition}')

print('Tabela de Transição de Estados: ')

n = len(activations)

for i in range(2 ** n):
    state = bin(i)[2:].rjust(n,'0')
    
    next_state = ''


    for gene, activations in activations.item():
        next_state += '1' if activations(*map(int, state)) else '0'
    
    print(state, next_state)
