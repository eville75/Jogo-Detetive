class Nodo:
    def __init__(self, pergunta=None, resposta_sim=None, resposta_nao=None, suspeito=None, descricao=None):
        self.pergunta = pergunta
        self.resposta_sim = resposta_sim
        self.resposta_nao = resposta_nao
        self.suspeito = suspeito
        self.descricao = descricao

class JogoDetetive:
    def __init__(self):
        # Descrições dos suspeitos
        self.descricoes = {
            "João": "João é um homem de 30 anos, trabalha como jardineiro e estava na cena do crime.",
            "Maria": "Maria é uma mulher de 25 anos, vizinha da vítima e ouviu gritos na noite do crime.",
            "Carlos": "Carlos é um homem de 40 anos, trabalha como eletricista e tem um histórico criminal.",
            "Ana": "Ana é uma mulher de 35 anos, ex-namorada da vítima e foi vista perto da cena do crime."
        }
        
        # Construir a árvore binária de perguntas
        self.raiz_fase1 = Nodo(
            pergunta="A vítima estava no jardim?",
            resposta_sim=Nodo(
                pergunta="Havia pegadas na terra?",
                resposta_sim=Nodo(suspeito="João"),
                resposta_nao=Nodo(suspeito="Carlos")
            ),
            resposta_nao=Nodo(
                pergunta="Havia sinais de arrombamento?",
                resposta_sim=Nodo(suspeito="Carlos"),
                resposta_nao=Nodo(
                    pergunta="Alguém ouviu gritos?",
                    resposta_sim=Nodo(suspeito="Maria"),
                    resposta_nao=Nodo(suspeito="Ana")
                )
            )
        )

        # Status do jogo
        self.fase = 1

    def dar_contexto(self):
        print("Você é um detetive encarregado de resolver um misterioso assassinato.")
        print("A vítima foi encontrada em sua casa e há quatro suspeitos: João, Maria, Carlos e Ana.")
        print("Interrogue as pessoas e visite os locais para juntar pistas e encontrar o assassino.\n")
    
    def ver_descricoes(self):
        print("Descrições dos suspeitos:")
        for suspeito, descricao in self.descricoes.items():
            print(f"{suspeito}: {descricao}")
        print()
    
    def interrogar(self, nodo):
        if nodo.suspeito:
            return nodo.suspeito
        resposta = input(nodo.pergunta + " (sim/nao): ").strip().lower()
        if resposta == "sim":
            return self.interrogar(nodo.resposta_sim)
        else:
            return self.interrogar(nodo.resposta_nao)
    
    def fase1(self):
        while True:
            print("\nFase 1:")
            print("1. Saber mais informações")
            print("2. Acusar alguém")
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                suspeito = self.interrogar(self.raiz_fase1)
                print(f"Após a investigação, você suspeita que o assassino é {suspeito}.")
            elif opcao == "2":
                suspeito = input("Quem você quer acusar? ").strip()
                if suspeito in self.descricoes:
                    print(f"Você acusou {suspeito}.")
                    if suspeito == "João":  # Supondo que João seja o assassino correto nesta fase
                        print("Parabéns! Você acertou o assassino.")
                        self.fase = 2
                    else:
                        print("Você acusou a pessoa errada. Tente novamente.")
                else:
                    print("Suspeito inválido. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")
            if self.fase == 2:
                break
    
    def fase2(self):
        print("\nParabéns, você chegou à Fase 2!")
        print("Nesta fase, você precisa coletar mais evidências e interrogar os suspeitos novamente para garantir a acusação correta.")
        # Adicionar lógica para a fase 2 (pode ser uma nova árvore binária ou mais perguntas)
        # Para simplificação, vamos apenas terminar o jogo aqui.
        print("Jogo concluído! Você resolveu o caso.")
    
    def jogar(self):
        self.dar_contexto()
        while self.fase == 1:
            self.fase1()
        if self.fase == 2:
            self.fase2()

if __name__ == "__main__":
    jogo = JogoDetetive()
    jogo.jogar()
