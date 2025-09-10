def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def jogar_enigma():
    print('Você avançou de fase. Agora acerte a palavra para ir para a próxima fase!')

    while True:
        palavra_cod = input('Digite a palavra do enigma: ').lower().strip()  # normaliza a entrada

        match palavra_cod:
            case "banco de dados":
                print("Parabens você acertou a palavra chave!")
                n = 1847
            case "web":
                print("Parabens você acertou a palavra chave!")
                n = 3092
            case "redes":
                print("Parabens você acertou a palavra chave!")
                n = 5261
            case "modelo":
                print("Parabens você acertou a palavra chave!")
                n = 7408
            case "computador":
                print("Parabens você acertou a palavra chave!")
                n = 9630
            case _:
                print(color_text("Você não digitou nenhuma das palavras corretas. ❌ Tente novamente!", "0;31"))
                continue  # volta para o início do loop

        # Se chegou aqui, significa que digitou uma palavra válida
        while True:
            try:
                palpite = int(input("Digite um número entre 1000 e 9999: "))
                if palpite < 1000 or palpite > 9999:
                    print("Número fora do intervalo! Digite um número entre 1000 e 9999.")
                    continue

                if palpite > n:
                    print("Tente um número menor.")
                elif palpite < n:
                    print("Tente um número maior.")
                else:
                    print(color_text(f"Você acertou!✅ O número era {n} pode passar para a proxima fase 👌", "0;32"))
                    return  # sai da função
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
jogar_enigma()