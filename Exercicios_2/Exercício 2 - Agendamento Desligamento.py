""" 
	## Agendamento de desligamento

Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
"""

import os
def turn_off_one_hour():
    os.system('shutdown /s /t 3600')
    
def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')
    
def cancel_shutdown():
    os.system('shutdown /a')
    

# turn_off_one_hour()
# turn_off_half_an_hour()
cancel_shutdown()









# 1 - Desligar o computador
# os.system('shutdown /s') # Desliga computador em 60s
# os.system('shutdowns /s /t 0') # Desliga computador imediatamente

# 2 - Cancelar o desligamento do computador
# os.system("shutdown /a") 

