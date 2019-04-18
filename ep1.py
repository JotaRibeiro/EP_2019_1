# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: João Pedro Henneberg Ribeiro, joaophr1@al.insper.edu.br
# - aluno B: Alex Nelson Steijntjes, alexs4@al.insper.edu.br

import random        

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
            }
        },
        "casa": {
            "titulo": "Humilde residencia",
            "descricao": "Voce esta em sua casa indeciso sobre seu dia",
            "opcoes": {
                "oficina": "Colocar um escapamento esportivo no seu carro no mecanico seu Magrao e deixar a EP de lado",
                "inicio": "Ir para o insper e negociar sobre a entrega da EP atrasada"
            }
        },
            
        "oficina": {
            "titulo": "Turbinando o carro",
            "descricao": "Voce esta na oficina mexendo em seu carro antes da entrega da EP",
            "opcoes": {
                "escapamento": "Colocar um escapamento esportivo novo na sua nave",
                "inicio": "Voltar ao insper para chegar a tempo para entrega da EP"
            }
        },
        "escapamento":{
            "titulo": "Escapamento ilegal",
            "descricao": "Voce foi pego pela policia com uma modificacao ilegal",
            "opcoes": {
                "lutar":"Enfrentar o policial",
                "render":"Se render ao policial"
            }
        }, 
            
        "render": {
            "titulo": "Se rendeu a policia",
            "descricao": "Voce se rendeu e foi levado a delegacia, nao conseguindo entregar a EP",
            "opcoes": {}
        },    
            
        "lutar":{
            "titulo": "Hora da luta",
            "descricao": "Voce foi pego pela policia mas decidiu enfrenta-lo (nao faca isso na vida real)",
            "opcoes": {
                "inicio": "Conseguiu voltar salvo ao insper"
            }
        },
    
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "corredor": "Voce ouviu um barulho esquisito em uma das salas do andar do professor"
            }
        },
        "corredor": {
            "titulo": "Corredor do andar da sala do professor",
            "descricao": "Voce ouviu um barulho estranho saindo de uma sala bem no fundo do corredor",
            "opcoes": {
                "andar professor": "Ficou com medinho decidiu nao entrar",
                "explorar": "Medo coisa nenhuma, voce entrou na sala"
            }
        },
        
        "explorar": {
            "titulo": "Corredor do andar da sala do professor",
            "descricao": "Aparentemente era so uma ilusao, nao aparenta ter nada de diferente na sala (mas será mesmo?...)",
            "opcoes": {
                "inicio": "Aparentemente não tem, volte ao saguao do perigo",
            }
        },
        
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "EP":{
            "titulo": "A famosa EP meia-boca",
            "descricao": "Voce fez o trabalho, entregou ao professor, mas ele achou que foi feito nas coxas",
            "opcoes": {}
        },
        
        "trabalho":{
            "titulo": "Caverna do desespero",
            "descricao": "Voce esta na bilbioteca e decidiu tentar fazer o trabalho de ultima hora",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "EP": "Fazer o trabalho de ultima hora e tentar ver se o professor aceita"
            }
        },
        
        "sala secreta": {
            "titulo": "Sala secreta da vitoria",
            "descricao": "PARABENS, voce foi teleportado para a sala secreta da vitoria, o unico moodo de se ganhar o jogo (e voce pensou que nao tinha jeito de ganhar né?...",
            "opcoes": {
                "vencer": "Ganhou o jogo, boa garoto"
            }
        },
        
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "trabalho": "Tentar fazer o EP de ultima hora"
            }
        }
    }
    nome_cenario_atual = "casa"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na sua casa, e não sabe se desiste de tudo ou vai para o insper procurar o professor para pedir um adiamento da EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print(len(cenario_atual["titulo"])*"-")
        print(cenario_atual["descricao"])
        opcoes = cenario_atual['opcoes']
        
#Teste dos Hitpoints
        jogador = 100
        policia = 100
        
        if nome_cenario_atual == "lutar":
            print("A policia te capturou, agora vc terá que lutar com ele para conseguir voltar ao insper a tempo da entrega da EP (voce tem 100 pontos de vida)")
    
            while jogador >0 and policia >0:
                x = random.randint(1,2)
                if x == 1: 
                    print("Soco em cheio, policia perdeu 20 pontos de vida")
                    policia -= 20
                else:
                    print("Levou cacetete na cabeca, menos 40 ponto de vida para voce")
                    jogador -= 40
    
        if jogador <= 0:
            print("Policial foi mais forte que voce, e voce foi capturado!")
            break
        elif policia <= 0:
            print("Vitoria, volte tranquilamente ao insper!")
                           

#Fim dos Testes dos Hitpoints 

#Easter Egg do Teleporte

#Fim do Easter Egg do Teleporte

        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Suas opções são:")
            for x,y in opcoes.items():
                print("{0}:{1}".format(x,y))
            escolha = input("Qual sua opção?")
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")

    
#Programa principal.
if __name__ == "__main__":
    main()
