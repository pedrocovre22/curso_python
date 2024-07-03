velocidade = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_radar_1 = velocidade > RADAR_1
multa = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_radar_1:
    print('passou da velocidade')

if multa:
    print('carro passou no radar 1')

if multa and vel_carro_radar_1:
    print('carro multado no radar 1')