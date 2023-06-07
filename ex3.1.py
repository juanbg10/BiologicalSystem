# # Faça um programa que receba uma lista de genes e uma função de regulação para cada gene com operadores not, and e or ('!', '&', ' | ') como no exercício VPL 02, e imprima a TABELA de TRANSIÇÃO de ESTADOS. Utilize o que foi feito nos exercícios anteriores. (Se quiser, pode fazer tudo diferente também)

# # Exemplo de execução:

# # Nomes dos genes (separados por vírgula): A,B,C

# # Função para A: !A&C | B&C | !C

# # Função para B: !A&!B | C

# # Função para C: A&B

# # Tabela de Transição de Estados:

# # 000 110

# # 001 110

# # 010 100

# # 011 110

# # 100 100

# # 101 010

# # 110 101

# # 111 111


def function_transform(rules):
  rules = rules.replace('!', ' not ')
  rules = rules.replace('&', ' and ')
  return rules.replace('|', ' or ')

def activate_gene(initial_state, activation):
  transition_gene = map(int, initial_state)
  activation_result = activation(*transition_gene)
  return '1' if activation_result else '0'
  # if activation_result:
  #   return '1'
  # else:
  #   return '0'

#############################
genes = input('Nomes dos genes (separados por vírgula): ').strip()

function_dict = {}

for gene in genes.split(','):
  rules = input(f'Função para {gene}: ')
  format_rules = function_transform(rules)
  expression = f'lambda {genes}: {format_rules}'
  function_dict[gene] = eval(expression)

print('Tabela de Transição de Estados: ')

qtd = len(function_dict)
possibilities = range(2 ** qtd)

for i in possibilities:
    initial_state = bin(i)[2:].rjust(qtd,'0')
    final_state = ''


    for gene, activation in function_dict.items():
        final_state += activate_gene(initial_state, activation)
    
    print(initial_state, final_state)
