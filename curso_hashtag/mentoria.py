
"""
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
"""


def area_pintar(largura, altura):
    """
    Calcula a quantidade de tinta necessária para pintar uma área retangular.

    Parâmetros:
    largura (float): Largura da área a ser pintada.
    altura (float): Altura da área a ser pintada.

    Retorna:
    float: Quantidade de tinta necessária em litros.
    """
    area = float(largura) * float(altura)
    tinta_necessaria = area / 6
    return tinta_necessaria


def custo_tinta(tinta_necessaria):
    """
    Calcula o custo da tinta com base na quantidade necessária.

    Parâmetros:
    tinta_necessaria (float): Quantidade de tinta necessária em litros.

    Retorna:
    float: Custo da tinta em reais.
    """
    rendimento = 6
    galao_pequeno = 3.6
    lata = 18
    if tinta_necessaria < galao_pequeno:
        preco = 25
    elif galao_pequeno <= tinta_necessaria < galao_pequeno * 2:
        preco = 50
    elif tinta_necessaria >= galao_pequeno * 2 and tinta_necessaria < lata * rendimento:
        preco = 80
    else:
        preco = 0  # Adicione uma lógica para casos não tratados

    return preco


def main():
    largura = input('Qual a largura da área? ')
    altura = input('Qual a altura da área? ')

    try:
        tot_tinta = area_pintar(largura, altura)
        print(f'{tot_tinta:.2f} litros de tinta serão necessários.')

        gasto_com_tinta = custo_tinta(tot_tinta)
        if gasto_com_tinta > 0:
            print(f'O custo com tinta para uma área de '
                  f'{tot_tinta:.2f} litros será de R$ {gasto_com_tinta:.2f}.')
        else:
            print('Quantidade de tinta fora do escopo de cálculo.')

    except ValueError:
        print('Por favor, insira valores numéricos válidos para largura e altura.')


if __name__ == "__main__":
    main()
