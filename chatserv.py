#-*- coding:utf-8 -*-
nomecompleto = "Gabriel Masson"

# --------------------------------------
# Informações
# --------------------------------------

nomecompleto = "Gabriel Masson"
arquivo_chat = "chat/chat.txt"


# --------------------------------------
# Código
# --------------------------------------

entrou = open(arquivo_chat,'a')
entrou.write('\n'+nomecompleto+' entrou no batepapo \n\n')
entrou.close()

while True:
  with open(arquivo_chat,'a') as chat:

    texto = raw_input('Você: ')

    while not texto:
      print 'Digite algo..'
      texto = raw_input('Você: ')

    if texto == '#sair' or texto == '#exit' or texto == '#close':
      chat.write('\n'+nomecompleto+' saiu do batepapo \n')
      print '\n Você saiu do batepapo. \n'
      break
    else:
      chat.write(nomecompleto+': '+texto+'\n')