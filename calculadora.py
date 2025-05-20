def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")

            print(f"Resultado: {resultado}")
            break  

        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.\n")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}. Tente novamente.\n")
        except Exception:
            print("Erro inesperado. Tente novamente.\n")

calculadora()
