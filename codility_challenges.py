"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Codility - Iteration Lessions 1 - Binary Gap

"""


def binary_gap(N : int) -> int:
    binary = "{0:b}".format(N)
    print(binary)
    contador_0 = 0
    maior_gap = 0

    for i in binary:

        if i == '1':
            if (contador_0 > maior_gap):
                maior_gap = contador_0
            contador_0 = 0
        if i == "0":
            contador_0 += 1

    print(maior_gap)
    return maior_gap

