# Controle de iluminação inteligente por meio de lógica difusa 
Trabalho realizado para a disciplina de Aprendizagem de Máquina.

## Especificação

### Objetivo
Desenvolver um sistema capaz de ajustar automaticamente a intensidade da iluminação em ambientes internos.

### Lógica Fuzzy
- Lógica Fuzzy é baseada na teoria dos conjuntos fuzzy (ou conjuntos nebulosos);
- Na lógica Fuzzy, uma premissa varia em grau de verdade de 0 a 1, o que leva a ser parcialmente verdadeira ou parcialmente falsa;
- É baseada em graus de pertinência (verdade);
- Sistemas baseados em lógica fuzzy podem ser usados para gerar estimativas, tomadas de decisão, sistemas de controle mecânico, ou até mesmo em
  - ar condicionado
  - casas inteligentes
  - intensidade da luz da tela do celular

### Variáveis de entrada
- Luminosidade natural:
  - Conjuntos fuzzy: Escuro, Médio, Claro
  - Níveis de pertinência: Baixo, Médio, Alto

![image](https://github.com/user-attachments/assets/51fcb248-19fd-4252-8c98-60331f4d98e0)

- Detecção de presença:
  - Conjuntos fuzzy: Ausente, Baixa, Alta
  - Níveis de pertinência: Baixo, Médio, Alto
 
![image](https://github.com/user-attachments/assets/bd973b90-0b39-421c-b081-e006e8277b40)

- Temperatura ambiente:
  - Conjuntos fuzzy: Frio, Confortável, Quente
  - Níveis de pertinência: Baixo, Médio, Alto
  
![image](https://github.com/user-attachments/assets/24fbb2cc-e5ec-4052-a76c-f999794f1a48)
 

- Preferência dos usuários:
  - Conjuntos fuzzy: Baixa, Média, Alta
  - Níveis de pertinência: Baixo, Médio, Alto
  
![image](https://github.com/user-attachments/assets/c079a28c-7ff8-4013-b767-95124fa3ade8)


### Variável de saída
- Intensidade da iluminação:
  - Conjuntos fuzzy: Baixa, Média, Alta
  - Níveis de pertinência: Baixo, Médio, Alto
  
![image](https://github.com/user-attachments/assets/16805595-b5bc-4905-9bb8-6e1aa36cda0d)


## Regras
![image](https://github.com/user-attachments/assets/c36c6e91-4637-4595-84c8-c7e623afdbd1)
![image](https://github.com/user-attachments/assets/7915271a-a3a9-49f6-9321-d98a29c2a946)
![image](https://github.com/user-attachments/assets/789e1ecf-4da5-40da-bc92-16b482c12d6a)


## Informações do programa
- Usamos a biblioteca SciKit-Fuzzy para facilitar na implementação do trabalho;
- Desenvolvemos o código pensando em um ambiente interno genérico, mas ressaltamos que para lugares específicos (como um quarto de hospital ou uma sala de aula), seria necessário realizar ajustes conforme as necessidades das pessoas que frequentam esses espaços 
- Trabalhamos com um universo de valores que varia a intensidade entre 0 a 100 nas variáveis **luminosidade natural**, **detecção de presença**, **preferência de usuários** e **intensidade de iluminação**; e com um universo de valores de 0 a 50ºC apenas na variável **temperatura ambiente**;
- As funções de pertinência e regras foram definidas intuitivamente por nosso próprio grupo;
- A deffuzificação foi testada por meio de vários métodos, como média dos máximos, primeiro dos máximos e centróide;
- Na realização de testes, foram utilizado valores para testar saídas de intensidade de luz baixa, média e alta;
- Foram levados em consideração para a escolha do método de deffuzificação resultados da intensidade que tendessem para um valor maior do que o esperado, pois nosso grupo concordou que era preferível ter mais incidência de luz no ambiente do que menos. O método de deffuzificação que mais se adequou às nossas preferências foi o **centróide**.
