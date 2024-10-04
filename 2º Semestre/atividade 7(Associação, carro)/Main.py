from Classes import *

motor1 = Motor(150.0, "Ford")
motor2 = Motor(200.0, "Chevrolet")
motor3 = Motor(180.0, "Honda")

roda1 = Rodas(16, "Pirelli")
roda2 = Rodas(18, "Michelin")

carro1 = Carro()
carro1.setMotor(motor1)
carro1.setRodas(roda1)

carro2 = Carro()
carro2.setMotor(motor2)
carro2.setRodas(roda1)

carro3 = Carro()
carro3.setMotor(motor3)
carro3.setRodas(roda1)

carro4 = Carro()
carro4.setMotor(motor1)
carro4.setRodas(roda2)

carro5 = Carro()
carro5.setMotor(motor2)
carro5.setRodas(roda2)

carro6 = Carro()
carro6.setMotor(motor3)
carro6.setRodas(roda2)

carros = [carro1, carro2, carro3, carro4, carro5, carro6]

print(" \t \t \t LISTA DE CARROS: \n")

posicao = 1
numero = 1


for car in carros:
    print(f"{posicao}º: \n \t Carro: \n Carro{numero} \n \n \t Motor: \n marca --> {car.getMotor().getMarca()} \n Potência --> {car.getMotor().getPotencia()} \n \n \t Conjunto de Rodas: \n Marca --> {car.getRodas().getMarca()} \n Tamanho --> {car.getRodas().getTamanho()} \n \n")

    posicao += 1
    numero += 1
