"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Beecrowd Challenges

"""
"""
Como de costume, neste ano Noel recebeu muitos pedidos de presentes. Só que em função de alguns imprevistos, não terá 
como entregar todos os presentes pessoalmente neste ano. Daí então decidiu utilizar o velho e bom correio tradicional, 
para alguns pedidos que podem ser entregues por carta.

Para esta tarefa, pediu ajuda ao elfo Evergreen Xadada, para que ele imprimisse etiquetas a todos os envelopes que 
serão destinados a algumas destas crianças, cujo pedido pode ser entregue por carta. Cada uma destas etiquetas deverá 
conter apenas o nome da criança e a saudação "Feliz Natal" no respectivo idioma desta criança. Para auxiliar nesta 
tarefa, Noel disponibilizou uma tabela com vários idiomas e o nome e o país de cada uma das crianças selecionadas, de 
acordo com o exemplo abaixo. Você deve ajudar Evergreen fazendo um programa que imprima estas etiquetas.

Entrada
A entrada é composta por um único caso de teste. A primeira linha de entrada contém um inteiro N (1 < N < 100) que 
indica a quantidade de traduções da palavra "Feliz Natal" existentes na entrada. As próximas N * 2 linhas contém 
respectivamente o nome de uma língua seguido da tradução de "Feliz Natal" para esta língua. Segue um inteiro 
M (1 < M < 100) que indica a quantidade de crianças que receberão as cartas. As próximas M * 2 linhas conterão, 
respectivamente, o nome da criança e a língua nativa desta criança.

Obs.: É garantido que nenhuma tradução apareça repetida ou duplicada e os países de todas as crianças estejam presentes 
na relação dos países.

Saída
Seu programa deverá imprimir todas as etiquetas de acordo com a entrada, conforme o exemplo abaixo, sempre com uma 
linha em branco após a impressão de cada uma das etiquetas, inclusive após a última etiqueta.
"""


num_idioms = int(input())
dict = {}
for i in range(num_idioms):
    language = input()
    traducion = input()
    dict[language] = traducion

num_kids = int(input())
for i in range(num_kids):
    nome = input()
    language = input()
    print(nome)
    print(dict[language])
    print()

"""
Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriais de cada um dos 
valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar em um valor com mais de 15 dígitos.

Entrada
O arquivo de entrada contém vários casos de teste. Cada caso contém dois números inteiros M (0 ≤ M ≤ 20) e 
N (0 ≤ N ≤ 20). O fim da entrada é determinado por eof.

Saída
Para cada caso de teste de entrada, seu programa deve imprimir uma única linha, contendo um número que é a soma de 
ambos os fatoriais (de M e N).
"""

while (True):
    try:
        M, N = map(int,input().split())
        M = list(range(M + 1))
        N = list(range(N + 1))
        M.remove(0)
        N.remove(0)
        m_fact = 1
        n_fact = 1
        for i in M:
            m_fact *= i
        for i in N:
            n_fact *= i

        print(m_fact + n_fact)
    except:
        break