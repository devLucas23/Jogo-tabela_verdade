## JOGO DE TABELA-VERDADE E EQUIVALÊNCIA DE PREPOSIÇÕES

# EXPLICAÇÃO

#### Funcionalidades e Regras:

Este código implementa um jogo de tabela-verdade interativo onde o jogador calcula
os valores de verdade para proposições lógicas. O jogo seleciona uma proposição aleatória,
solicita ao jogador para inserir os resultados da tabela-verdade, verifica as respostas e
fornece feedback. Se o jogador quiser, ele pode jogar novamente com uma nova proposição
lógica.

# Objetivo:
- O jogador precisa determinar a tabela-verdade de proposições lógicas e identificar
equivalências entre diferentes proposições.

# Regras:
- O jogo apresenta proposições lógicas ao jogador.
- O jogador deve completar a tabela-verdade para cada proposição apresentada.
- O jogador deve identificar se duas proposições dadas são logicamente equivalentes.
- Pontos são concedidos com base na precisão das respostas do jogador.
- Há um limite de tempo para cada pergunta.

# Funcionalidades:
- Geração de Proposições: Cria proposições lógicas aleatórias para o jogador
resolver.
- Interface de Usuário: Permite ao jogador inserir suas respostas e ver feedback
imediato.
- Pontuação: Mantém um registro da pontuação do jogador com base nas respostas
corretas.

# Explicação do jogo
### Funções que representam operações lógicas:
● não: Negação.&nbsp;
● e: Conjunção (e lógico).&nbsp;
● ou: Disjunção (ou lógico).&nbsp;
● implicação: Implicação lógica.&nbsp;
● bi-implicação: Bicondicional (se e somente se).&nbsp;
● Converte valores de verdade True e False em V e F respectivamente &nbsp;

# Explicação das Funcionalidades
1. Geração de Proposições:
- A lista propositions contém funções que representam proposições lógicas
básicas.
- O jogo escolhe aleatoriamente uma dessas proposições para o jogador
resolver.
2. Geração de Valores de Verdade:
- A função generate_truth_values gera todas as combinações possíveis
de valores de verdade para um número dado de proposições (neste caso, 2
proposições: p e q).
3. Cálculo da Tabela-Verdade:
- A função calculate_truth_table avalia a proposição lógica para todas
as combinações de valores de verdade.
- eval(expression, {}, env) calcula o valor da proposição lógica no
contexto dos valores atuais das variáveis.
4. Impressão da Tabela-Verdade:
- A função print_truth_table exibe a tabela-verdade de maneira
organizada para que o jogador possa verificar e aprender.
5. Loop Principal do Jogo:
- A função truth_table_game gerencia a seleção de proposições e a
interação com o jogador, incluindo a opção de jogar novamente.
