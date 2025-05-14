def calculadora_basica():
    """
    Desafio da profa. Aline no curso git e github. (fiz exemplo parecido pois não havia na atividade
     os exercícios mencionados no vídeo)
    """
    try:
        num1_str = input("Digite o primeiro valor: ")
        num1 = float(num1_str)

        num2_str = input("Digite o segundo valor: ")
        num2 = float(num2_str)

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif operacao == '-':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif operacao == '*':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif operacao == '/':
            if num2 == 0:
                print("Erro! Divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
        else:
            print("Operação inválida. Use +, -, *, ou /.")

    except ValueError:
        print("Erro! Por favor, digite valores numéricos válidos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chamando a função para executar a calculadora
calculadora_basica()