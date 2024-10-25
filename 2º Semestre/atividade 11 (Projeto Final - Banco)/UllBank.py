import os
from classis import *
from Defis import *

Ull = Banco()

while True:
        escolha = menu () 

        match escolha: 
                case 1:
                    login(Ull)
                
                case 2:
                      cadastro(Ull)