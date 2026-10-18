"""
Atividade: Controle de Níveis de Água
Sistema simples de monitoramento de um reservatório, exibindo alertas
coloridos no terminal com a biblioteca colorama.

Instalação da biblioteca:
    pip install colorama
"""

from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=False)

# Lista com as mensagens de cada nível
mensagens = [
    "Nível 1 - CRÍTICO: abasteça o reservatório imediatamente!",
    "Nível 2 - BAIXO: atenção, o nível está diminuindo.",
    "Nível 3 - MÉDIO: reservatório em condição normal.",
    "Nível 4 - ALTO: nível elevado, acompanhe de perto.",
    "Nível 5 - MUITO ALTO (ALERTA): risco de transbordamento!",
]


def definir_cor(nivel):
    """Retorna a cor do colorama correspondente ao nível informado (1 a 5)."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE  # nível inválido


def exibir_situacao(nivel):
    """Exibe no terminal a mensagem do nível atual com a cor correspondente."""
    if 1 <= nivel <= len(mensagens):
        cor = definir_cor(nivel)
        print(cor + mensagens[nivel - 1])
    else:
        print(Fore.WHITE + f"Nível {nivel} inválido. Use valores de 1 a 5.")


def main():
    print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

    # Simulação: valores definidos no código 
    leituras = [1, 2, 3, 4, 5]

    for nivel in leituras:
        exibir_situacao(nivel)

    # Restaura o estilo padrão do terminal
    print(Style.RESET_ALL + "\nMonitoramento finalizado.")


if __name__ == "__main__":
    main()