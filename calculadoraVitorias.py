def calcular_nivel(vitorias, derrotas):
    """
    Calcula o saldo de rankeadas e determina o nível do jogador.

    Args:
        vitorias (int): O número de vitórias do jogador.
        derrotas (int): O número de derrotas do jogador.

    Returns:
        str: Uma mensagem indicando o saldo de vitórias e o nível do jogador.
    """
    saldo_vitorias = vitorias - derrotas
    nivel = ""

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"

    return f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}"

# Exemplo de uso da função:
vitorias_jogador = int(input("Digite o número de vitórias: "))
derrotas_jogador = int(input("Digite o número de derrotas: "))

resultado = calcular_nivel(vitorias_jogador, derrotas_jogador)
print(resultado)