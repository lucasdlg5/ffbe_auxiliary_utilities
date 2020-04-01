import math 

"1 a 120"
minituar = 90000
cactuar = 410000
gigantuar = 1290000
km_minituar = 4500000




lvl = int(input('digite o level\nDigite:'))

valor_exp_total = 0

for valor_do_xp in range (1,lvl):
    valor_do_xp = (math.ceil(1*500000*(( lvl / 99)**(5/2) - (( lvl-1 )/99)**(5/2))))
    valor_exp_total = valor_exp_total + valor_do_xp

print (valor_exp_total)


a = int(input('Digite a quantidade de XP necessaria\nDigite:'))
d = int(input('Digite a quantidade de XP atual do personagem\nDigite:'))
falta = a - d
print(falta)
qm = int(falta / minituar)
qc = int(falta / cactuar)
qg = int(falta / gigantuar)
qkmm = int(falta / km_minituar)

print (f'você deve usar {qm} Minituar, {qc} Cactuar, {qg} Gigantuar ou {qkmm} King Metal Minituar')

