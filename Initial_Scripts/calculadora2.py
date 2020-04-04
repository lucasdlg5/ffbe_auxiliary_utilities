import math 

"1 a 120"

cactuar = 10000
gigantuar = 30000
km_minituar = 100000



stars = int(input('Quantas estrelas tem o pesonagem ?\nDigite:'))
lvl = int(input('Digite o level\nDigite:'))

valor_exp_total = 0

if lvl >= 100 or stars >= 6:
    for valor_do_xp in range (1,lvl):
        valor_do_xp = (math.ceil(stars*500000*(( lvl / 99)**(5/2) - (( lvl-1 )/99)**(5/2))))
        valor_exp_total = valor_exp_total + valor_do_xp
else:
   if lvl = 101:
       101 = 0
   if lvl = 102:
       102 = 378273
   if lvl = 103:
       103 = 409796
   if lvl = 104:
       104 = 441319
   if lvl = 105:
       105 = 472842
   if lvl = 106:
       106 = 650584
   if lvl = 107:
       107 = 828326
   if lvl = 108:
       108 = 1006068
   if lvl = 109:
       109 = 1183810
   if lvl = 110:
       110 = 1361552
   if lvl = 111:
       111 = 1705958
   if lvl = 112:
       112 = 2050364
   if lvl = 113:
       113 = 2394770
   if lvl = 114:
       114 = 2739176
   if lvl = 115:
       115 = 3083582
   if lvl = 116:
       116 = 3785510
   if lvl = 117:
       117 = 4487438
   if lvl = 118:
       118 = 5189366
   if lvl = 119:
       119 = 5891294
   if lvl = 120:
       120 = 6593222
 



print (valor_exp_total)




a = (valor_exp_total)
d = 0
falta = a - d
print(falta)
qc = int(falta / cactuar)
qg = int(falta / gigantuar)
qkmm = int(falta / km_minituar)

print (f'você deve usar, {qc} Cactuar, {qg} Gigantuar ou {qkmm} King Metal Minituar')

