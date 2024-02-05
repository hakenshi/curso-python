# CONSTANTES = "Variáveis" que não mudam seu valor
# Muitas condições no mesmo if (ruim)
#      <- Contagem de complexidade (ruim)

velocidade = 60
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

inicio_do_radar= LOCAL_1 - RADAR_RANGE
fim_do_radar = LOCAL_1 + RADAR_RANGE

velocidade_carro_passou_radar_1 = velocidade > RADAR_1

checa_onde_o_radar_comeca = local_carro >= inicio_do_radar
checa_onde_o_radar_termina = local_carro <= fim_do_radar

carro_passou_no_radar1 = checa_onde_o_radar_comeca and checa_onde_o_radar_termina

if velocidade_carro_passou_radar_1 :
    print('O carro passou no radar 1 acima do limite permitido')

if carro_passou_no_radar1 :
    print('O carro passou no radar 1')

if carro_passou_no_radar1 and velocidade_carro_passou_radar_1 :
    print(f'O carro foi multado no radar 1 a {velocidade-RADAR_1}km/h acima do limite permitido')