nome_do_heroi = input("Digite o nome do herói: ")
xp_do_heroi_str = input("Digite a quantidade de XP do herói: ")

try:
    xp_do_heroi = int(xp_do_heroi_str)

    nivel_do_heroi = ""

    if xp_do_heroi < 1000:
        nivel_do_heroi = "Ferro"
    elif 1001 <= xp_do_heroi <= 2000:
        nivel_do_heroi = "Bronze"
    elif 2001 <= xp_do_heroi <= 5000:
        nivel_do_heroi = "Prata"
    elif 5001 <= xp_do_heroi <= 7000:
        nivel_do_heroi = "Ouro"
    elif 7001 <= xp_do_heroi <= 8000:
        nivel_do_heroi = "Platina"
    elif 8001 <= xp_do_heroi <= 9000:
        nivel_do_heroi = "Ascendente"
    elif 9001 <= xp_do_heroi <= 10000:
        nivel_do_heroi = "Imortal"
    elif xp_do_heroi >= 10001:
        nivel_do_heroi = "Radiante"

    print(f"O Herói de nome {nome_do_heroi} está no nível de {nivel_do_heroi}")

except ValueError:
    print("Por favor, digite um valor numérico válido para a XP.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")