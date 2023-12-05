from skfuzzy import control as ctrl
import funcoes_pertinencia
import universo_variaveis as universo

#regras de luminosidade natural
#se a luminosidade natural for escura, média ou clara mas a detecção de presença for ausente, a intensidade de iluminação será baixa
regra1 = ctrl.Rule((universo.luminosidade_natural['escuro'] | universo.luminosidade_natural['medio'] | universo.luminosidade_natural['claro']) 
                   & universo.deteccao_presenca['ausente'], universo.intensidade_iluminacao['baixo'])

regra2 = ctrl.Rule(universo.luminosidade_natural['medio'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['medio'])
regra3 = ctrl.Rule(universo.luminosidade_natural['claro'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['baixo'])

#regras de preferência de usuários
#se a preferência de usuário for baixa, média ou alta mas a detecção de presença for ausente, não há necessidade de obedecer as preferências 
#do usuário
regra4 = ctrl.Rule((universo.preferencia_usuarios['baixo'] | universo.preferencia_usuarios['medio'] | universo.preferencia_usuarios['alto']) 
                   & universo.deteccao_presenca['ausente'], universo.intensidade_iluminacao['baixo'])

regra5 = ctrl.Rule((universo.preferencia_usuarios['baixo'] & universo.deteccao_presenca['baixo']), universo.intensidade_iluminacao['baixo'])
regra6 = ctrl.Rule((universo.preferencia_usuarios['medio'] & universo.deteccao_presenca['baixo']), universo.intensidade_iluminacao['medio'])
regra7 = ctrl.Rule((universo.preferencia_usuarios['alto'] & universo.deteccao_presenca['baixo']), universo.intensidade_iluminacao['alto'])

regra8 = ctrl.Rule((universo.preferencia_usuarios['baixo'] & universo.deteccao_presenca['alto']), universo.intensidade_iluminacao['baixo'])
regra9 = ctrl.Rule((universo.preferencia_usuarios['medio'] & universo.deteccao_presenca['alto']), universo.intensidade_iluminacao['medio'])
regra10 = ctrl.Rule((universo.preferencia_usuarios['alto'] & universo.deteccao_presenca['alto']), universo.intensidade_iluminacao['alto'])

#regras de temperatura ambiente
#se a temperatura for quente, confortável ou fria e a detecção de presença for ausente, a intensidade será baixa
regra11 = ctrl.Rule((universo.temperatura_ambiente['quente'] | universo.temperatura_ambiente['confortavel'] | universo.temperatura_ambiente['frio']) 
                    & universo.deteccao_presenca['ausente'], universo.intensidade_iluminacao['baixo'])

regra12 = ctrl.Rule(universo.temperatura_ambiente['quente'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])
regra13 = ctrl.Rule(universo.temperatura_ambiente['quente'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

regra14 = ctrl.Rule(universo.temperatura_ambiente['confortavel'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])
regra15 = ctrl.Rule(universo.temperatura_ambiente['confortavel'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

regra16 = ctrl.Rule(universo.temperatura_ambiente['frio'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])
regra17 = ctrl.Rule(universo.temperatura_ambiente['frio'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

#realizando inferências das regras 
iluminacao = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10, regra11, regra12, regra13, 
                                 regra14, regra15, regra16, regra17])
valores = ctrl.ControlSystemSimulation(iluminacao)