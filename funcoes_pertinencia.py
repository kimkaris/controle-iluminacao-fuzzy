import skfuzzy as fuzzy
import universo_variaveis as universo

#funções de pertinência para as variáveis
universo.luminosidade_natural['escuro'] = fuzzy.trimf(universo.luminosidade_natural.universe, [0, 0, 45])
universo.luminosidade_natural['medio'] = fuzzy.trapmf(universo.luminosidade_natural.universe, [10, 50, 60, 90])
universo.luminosidade_natural['claro'] = fuzzy.trimf(universo.luminosidade_natural.universe, [65, 100, 100])

universo.deteccao_presenca['ausente'] = fuzzy.trimf(universo.deteccao_presenca.universe, [0, 0, 40])
universo.deteccao_presenca['baixo'] = fuzzy.trapmf(universo.deteccao_presenca.universe, [5, 30, 50, 90])
universo.deteccao_presenca['alto'] = fuzzy.trimf(universo.deteccao_presenca.universe, [60, 100, 100])

universo.temperatura_ambiente['frio'] = fuzzy.trimf(universo.temperatura_ambiente.universe, [0, 0, 25])
universo.temperatura_ambiente['confortavel'] = fuzzy.trapmf(universo.temperatura_ambiente.universe, [10, 20, 30, 40])
universo.temperatura_ambiente['quente'] =  fuzzy.trimf(universo.temperatura_ambiente.universe, [30, 50, 50])

universo.preferencia_usuarios['baixo'] = fuzzy.trimf(universo.preferencia_usuarios.universe, [0, 0, 30])
universo.preferencia_usuarios['medio'] = fuzzy.trapmf(universo.preferencia_usuarios.universe, [10, 40, 60, 90])
universo.preferencia_usuarios['alto'] = fuzzy.trimf(universo.preferencia_usuarios.universe, [70, 100, 100])

universo.intensidade_iluminacao['baixo'] = fuzzy.trimf(universo.intensidade_iluminacao.universe, [0, 0, 40])
universo.intensidade_iluminacao['medio'] = fuzzy.trapmf(universo.intensidade_iluminacao.universe, [10, 45, 55, 90])
universo.intensidade_iluminacao['alto'] = fuzzy.trimf(universo.intensidade_iluminacao.universe, [60, 100, 100])
