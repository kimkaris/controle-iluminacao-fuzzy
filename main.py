import regras as reg
import universo_variaveis as universo

if __name__ == "__main__":
    def validar_entrada(numero, limite):
            while True:
                try:
                    valor = int(input(numero))
                    if 0 <= valor <= limite:
                        return valor
                    else:
                        print("Insira um valor entre 0 e", limite)
                except ValueError:
                    print("Insira um valor válido.")


    #valores de entrada para o sistema conforme as variáveis dos conjuntos fuzzy
    print("Digite valores inteiros de sua preferência:")
    reg.valores.input['luminosidade_natural'] = validar_entrada("Insira a luminosidade natural (em um intervalo de 0 a 100): ", 100)
    reg.valores.input['deteccao_presenca'] = validar_entrada("Insira a deteccao de presenca (em um intervalo de 0 a 100): ", 100)
    reg.valores.input['temperatura_ambiente'] = validar_entrada("Insira a temperatura ambiente (em um intervalo de 0 a 50°C): ", 50)
    reg.valores.input['preferencia_usuarios'] = validar_entrada("Insira a preferencia dos usuarios (em um intervalo de 0 a 100): ", 100)

    #computando a saída da intensidade da iluminação e imprime o valor no terminal
    valor_final = reg.valores.compute()
    print(f"Intensidade da iluminação ideal: {reg.valores.output['intensidade_iluminacao']}%")

    #visualização gráfica da intensidade de iluminação ideal pós defuzzificação
    universo.intensidade_iluminacao.view(reg.valores)

    print(f"Pressione ENTER para finalizar a execução do programa: ", end = '')
    input()