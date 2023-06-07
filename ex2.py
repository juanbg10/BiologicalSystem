# Faça um programa que receba uma lista de genes e uma função de regulação para cada gene com operadores not, and e or ('!', '&', ' | ') e imprima uma lista dos estados em que cada gene estará ativado. A ordem dos genes deverá ser a ordem dada na lista. Repare que o operador or está entre espaços que equivale a separar com parênteses. Por exemplo, '!A&C | B&C | !C' que equivale a (!A&C) | (B&C) | (!C). Não haverá parênteses nas expressões.
# Para simplificar, consideraremos que as funções serão sempre nesse formato, sem encadeamentos sobrepostos difíceis de identificar.

# Em outras palavras: dá para fazer um split primeiro com ' | ' para separar os pedaços e depois use o que foi feito no exercício anterior para '&'. Repita para todos os genes. Se quiser usar outra implementação muito mais simples, utilize-a.

# Exemplo de execução:

# Nomes dos genes (separados por vírgula): A,B,C

# Função para A: !A&C | B&C | !C

# Função para B: !A&!B | C

# Função para C: A&B

# Estados que ativarão A: ['000', '001', '010', '011', '100', '110', '111']

# Estados que ativarão B: ['000', '001', '011', '101', '111']

# Estados que ativarão C: ['110', '111']

#  input's

#concatena, ordena, tira duplicado

# A: ['001', '011'] ['011', '111'] ['000', '010', '100', '110']

# B: ['000', '001'] ['001', '011', '101', '111']

# C: ['110', '111']


# ====== GERAR GENE  ======
def gerar_gene(listgenes, genes):
    graph = listgenes.split('&')

    activationsgenes = []

    for i in range(2**len(genes)):
        state = bin(i)[2:].rjust(qtd, '0')
        values = {k: int(v) for k, v in zip(genes, state)}

        result = True

        for item in graph:
            if (result == False):
                break
            if item.startswith('!'):
                result = result and not bool(values[item.replace('!', '')])
            else:
                result = result and bool(values[item])
        if result:
            activationsgenes.append(state)

    return activationsgenes


# ====== MAIN ======

genes = input('Nomes dos genes (separados por vírgula): ').replace(
    ' ', '').strip().split(',')

qtd = len(genes)

allfunlist = []

for i in genes:
    function = input(f"Função para {i}: ").replace(' ', '')
    opcfun = function.split('|')
    allfunlist.append(opcfun)

resultado = []
aux = 0

for funlist in allfunlist:
    for fun in funlist:
        activegenes = gerar_gene(fun, genes)

        for z in activegenes:
            resultado.append(z)

    print(f"Estados que ativarão {genes[aux]}: ", sorted(list(set(resultado)), reverse=False)) 
    aux = aux + 1
    resultado = []


# Nomes dos genes (separados por vírgula): A,B,C

# Função para A: !A&C | B&C | !C

# Função para B: !A&!B | C

# Função para C: A&B
