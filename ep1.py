# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: João Pedro Henneberg Ribeiro, joaophr1@al.insper.edu.br
# - aluno B: Alex Nelson Steijntjes, alexs4@al.insper.edu.br

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
                "oficina mecanica magrao": "Colocar um escapamento esportivo e deixar a EP de lado",
                "inicio": "Ir para o insper e negociar sobre a entrega da EP atrasada"
            }
        },
            
        "oficina mecanica magrao": {
            "titulo": "Turbinando o carro",
            "descricao": "Voce esta na oficina mexendo em seu carro antes da entrega da EP",
            "opcoes": {
                "escapamento novo": "Colocar um escapamento esportivo",
                "inicio": "Voltar ao insper para chegar a tempo para entrega da EP"
            }
        },
        "escapamento novo":{
            "titulo": "Escapamento ilegal",
            "descricao": "Voce foi pego pela policia com uma modificacao ilegal e não conseguiu voltar a tempo no INSPER para a entrega da EP",
            "opcoes": {}
        },    
    
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
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
    

# Programa principal.
if __name__ == "__main__":
    main()
