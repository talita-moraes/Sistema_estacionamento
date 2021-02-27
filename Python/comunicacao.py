import serial
import funcoes
import sqlite3

conn = sqlite3.connect('dados.db')
c = conn.cursor() 

global conexao
porta = 'COM4'
velocidade = 9600
conexao = serial.Serial(porta, velocidade)


while(conexao.isOpen() == True):
    opcao = int(conexao.readline().decode())    #receber o valor da opcao
    cartao = conexao.readline().decode()        #recebr o numero do cartao

    cartao = str(cartao)
    
    if(funcoes.verificardado(c,cartao,'IDUsuario')== False):
        resposta = str('nao encontrado')
        
    elif(funcoes.verificardado(c,cartao,'IDUsuario')== True):
        if(opcao == 1):
            tipo = str(funcoes.buscartipo(c, cartao))
            
            conexao.write(tipo.encode())                          # mandar o tipo do usuario
            tipoArduino = bool(conexao.readline().decode())       #receber o valor da opcao

            if (tipoArduino == True):
                funcoes.inserirdadosacesso(c, cartao, funcoes.data())            
                resposta = str('Usuario entrou!')
            
        elif(opcao == 2):
            funcoes.atualizardadoacesso(c, funcoes.data(),cartao)
            resposta = str('Usuario saida!')

        conexao.write(resposta.encode())            # mandar mensagem do tipo do usuario
    
        
# Salvar
conn.commit()

# Fechar conexão
conexao.close()
    
    

    
