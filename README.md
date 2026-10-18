# Controle de Níveis de Água

Sistema simples de monitoramento de um reservatório de água, executado no terminal. Exibe mensagens de alerta com cores diferentes conforme o nível de água, usando a biblioteca **colorama**.

## Níveis

| Nível | Situação | Cor |
|-------|----------|-----|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Como executar

1. Instale a biblioteca:
   pip install colorama

2. Execute o programa:
python controle_niveis_agua.py

## O que o código usa

- Lista com as mensagens de cada nível
- Função `definir_cor()` que escolhe a cor conforme o nível
- Biblioteca `colorama` para colorir o terminal
- `Style.RESET_ALL` para restaurar o estilo padrão no final

## Autora
Ashley Beatriz - Agenda 11 - DSI
