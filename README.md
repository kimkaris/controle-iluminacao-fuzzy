# Controle de iluminação inteligente por meio de lógica difusa 
Trabalho realizado para a disciplina de Aprendizagem de Máquina.

## Especificação

### Objetivo
Desenvolver um sistema capaz de ajustar automaticamente a intensidade da iluminação em ambientes internos.

### Variáveis de entrada
- Luminosidade natural:
  - Conjuntos fuzzy: Escuro, Médio, Claro
  - Níveis de pertinência: Baixo, Médio, Alto
- Detecção de presença:
  - Conjuntos fuzzy: Ausente, Baixa, Alta
  - Níveis de pertinência: Baixo, Médio, Alto
- Temperatura ambiente:
  - Conjuntos fuzzy: Frio, Confortável, Quente
  - Níveis de pertinência: Baixo, Médio, Alto
- Preferência dos usuários:
  - Conjuntos fuzzy: Baixa, Média, Alta
  - Níveis de pertinência: Baixo, Médio, Alto

### Variável de saída
- Intensidade da iluminação:
  - Conjuntos fuzzy: Baixa, Média, Alta
  - Níveis de pertinência: Baixo, Médio, Alto

## Informações do sistema
- Usamos a biblioteca SciKit-Fuzzy para facilitar na implementação do trabalho
- Desenvolvemos o código pensando em um ambiente interno genérico, mas ressaltamos que para lugares específicos (como um quarto de hospital ou uma sala de aula), seria necessário realizar ajustes conforme as necessidades das pessoas que frequentam esses espaços 
- Trabalhamos com um universo de valores que varia a intensidade entre 0 a 100 nas variáveis **luminosidade natural**, **detecção de presença**, **preferência de usuários** e **intensidade de iluminação**; e com um universo de valores de 0 a 50ºC apenas na variável **temperatura ambiente**
- As funções de pertinência e regras foram definidas intuitivamente por nosso próprio grupo
- A deffuzificação foi testada por meio de vários métodos, como média dos máximos, primeiro dos máximos e centróide
- Na realização de testes, foram utilizado valores para testar saídas de intensidade de luz baixa, média e alta
- Foram levados em consideração para a escolha do método de deffuzificação resultados da intensidade que tendessem para um valor maior do que o esperado, pois nosso grupo concordou que era preferível ter mais incidência de luz no ambiente do que menos. O método de deffuzificação que mais se adequou às nossas preferências foi o **centróide** 
