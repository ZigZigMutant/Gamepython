import random
import time

# STATUS DO JOGADOR
vida = 60
ataque = 1
defesa = 10
ouro = 0
pocao = 2

# INIMIGOS
inimigos = [{"nome":"Goblin", "vida_i": 50, "ataque_i": 8, "defesa_i": 10},
            
            {"nome":"Esqueleto", "vida_i": 30, "ataque_i": 10, "defesa_i": 8},

            {"nome":"Bandido", "vida_i": 40, "ataque_i": 10, "defesa_i": 15},

            {"nome":"Lobo Atroz", "vida_i": 60, "ataque_i": 12, "defesa_i": 17}]

#CHEFES
chefes = [{"nome":"Dragão", "vida_i": 140, "ataque_i": 18, "defesa_i": 20},
          
          {"nome":"Troll", "vida_i": 120, "ataque_i": 16, "defesa_i": 15}]

#CAMINHOS
caminhos = ["Você encontra uma estrada que leva a uma floresta sombria.",
           "Você encontra uma caverna misteriosa.",
           "Você encontra ruinas de um castelo abandonado.",
           "Você encontra uma masmorra escondida sob a terra."]

#CONTADOR DE BATALHAS
batalhas = 0

print("=" * 40)
time.sleep(0.5)
print("DungeonWay - Aventura nas Profundezas")
time.sleep(0.5)
print("=" * 40)
time.sleep(0.5)

nome = input("Digite o nome do seu herói: ")
time.sleep(0.5)

print("Escolha a classe do seu herói:")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")

classe = input("Escolha: ")
if classe == "1":
    vida_bonus = 40
    ataque += 8
    defesa += 8
    print("\nVocê escolheu a classe Guerreiro!")
elif classe == "2":
    vida_bonus = 5
    ataque += 12
    defesa += 3
    print("\nVocê escolheu a classe Mago!")
elif classe == "3":
    vida_bonus = 20
    ataque += 5
    defesa += 12
    print("\nVocê escolheu a classe Arqueiro!")
else:
    print("\nEscolha inválida!")

vida_total = vida + vida_bonus
vida = vida_total


print(f"\nBem-vindo, {nome}!")
time.sleep(1)
print(" Textinho 1.")
time.sleep(1)
print("textinho 2.\n")
time.sleep(1)

# LOOP PRINCIPAL
while vida > 0:

    print("\n" + "-" * 40)
    print(f"Vida: {vida}")
    print(f"Ataque: {ataque}")
    print(f"Defesa: {defesa}")
    print(f"Poções: {pocao}")
    print(f"Ouro: {ouro}")
    print("-" * 40)

    caminho_atual = random.choice(caminhos)

    print(f"\n{caminho_atual}")
    time.sleep(1.5)
    print("1 - Explorar")
    print("2 - Descansar")
    print("3 - Ir para a Loja")
    print("4 - Sair do jogo")

    escolha = input("Escolha: ")

    # EXPLORAR
    if escolha == "1":

        inimigo = random.choice(inimigos)
        vida_inimigo = inimigo["vida_i"]
        time.sleep(1)
        print("\nVocê decide explorar a área...")
        time.sleep(1)

        print(f"\nUm {inimigo['nome']} apareceu!")

        # COMBATE
        while vida_inimigo > 0 and vida > 0:

            print("\n--- COMBATE ---")
            print(f"Sua vida: {vida}")
            print(f"Vida do {inimigo['nome']}: {vida_inimigo}")

            print("\n1 - Atacar")
            print("2 - Usar poção")
            print("3 - Fugir")

            acao = input("Escolha: ")

            # ATAQUE
            if acao == "1":
                ataque_total = ataque + random.randint(1, 20)
                if ataque_total > inimigo["defesa_i"]:
                    dano = random.randint(10, 25)
                    vida_inimigo -= dano

                    print(f"\nVocê acertou o {inimigo['nome']}!")
                    time.sleep(1)
                    print(f"\nVocê causou {dano} de dano!")
                    time.sleep(1)
                else:
                    print("\nSeu ataque falhou!")
                    time.sleep(1)

                if vida_inimigo > 0:
                    ataque_inimigo = inimigo["ataque_i"] + random.randint(1, 20)
                    if ataque_inimigo > defesa:
                        dano_inimigo = random.randint(5, 20)
                        vida -= dano_inimigo

                        print(f"O {inimigo['nome']} atacou você!")
                        time.sleep(1)
                        print(f"Você perdeu {dano_inimigo} de vida.")
                        time.sleep(1)
                    else:
                        print(f"O ataque do {inimigo['nome']} falhou!")
                        time.sleep(1)

            # POÇÃO
            elif acao == "2":
                if pocao > 0:
                    cura = random.randint(20, 35)
                    vida += cura
                    pocao -= 1

                    if vida > vida_total:
                        vida = vida_total

                    print(f"\nVocê recuperou {cura} de vida!")
                    time.sleep(1)
                else:
                    print("\nVocê não possui poções!")
                    time.sleep(1)

            # FUGIR
            elif acao == "3":
                ataque_inimigo = inimigo["ataque_i"] + random.randint(1, 20)
                if ataque_inimigo > defesa:
                    print(f"\nVocê tenta fugir, mas não consegue!")
                    time.sleep(1)
                else:
                    print(f"\nVocê fugiu do {inimigo['nome']}!")
                    time.sleep(1)
                    break

            else:
                print("\nEscolha inválida!")

        # VITÓRIA
        if vida_inimigo <= 0:
            recompensa = random.randint(10, 30)
            ouro += recompensa

            print(f"\nVocê derrotou o {inimigo ['nome']}!")
            time.sleep(1)
            print(f"Ganhou {recompensa} moedas de ouro!")
            time.sleep(1)
            batalhas += 1
        
            # CHEFE FINAL
            if batalhas == 10:
                chefe = random.choice(chefes)
                print("\n" + "=" * 40)
                print(f"O {chefe['nome']} SURGIU!")
                print("=" * 40)
                time.sleep(2)

                chefe_vida = chefe["vida_i"]

                while chefe_vida > 0 and vida > 0:

                    print(f"\nSua vida: {vida}")
                    print(f"Vida do {chefe['nome']}: {chefe_vida}")

                    print("\n1 - Atacar")
                    print("2 - Usar poção")

                    boss = input("Escolha: ")

                    if boss == "1":
                        ataque_total = ataque + random.randint(1, 20)
                        if ataque_total > chefe["defesa_i"]:
                            dano = random.randint(15, 30)
                            chefe_vida -= dano
                            time.sleep(1)
                            print(f"\nVocê acertou o {chefe['nome']} com {dano} de dano!")
                        else:
                            print(f"\nSeu ataque falhou contra o {chefe['nome']}!")
                            time.sleep(1)

                        if chefe_vida > 0:
                            ataque_chefe = chefe["ataque_i"] + random.randint(1, 20)
                            if ataque_chefe > defesa:
                                dano_chefe = random.randint(15, 25)
                                vida -= dano_chefe

                                time.sleep(1)
                                print(f"O {chefe['nome']} atacou!")
                                time.sleep(1)
                                print(f"Você perdeu {dano_chefe} de vida.")
                                time.sleep(1)
                            else:
                                print(f"O ataque do {chefe['nome']} falhou!")
                                time.sleep(1)

                    elif boss == "2":
                        if pocao > 0:
                            vida += 30
                            pocao -= 1

                            if vida > vida_total:
                                vida = vida_total

                            print("\nVocê usou uma poção!")
                            time.sleep(1)
                            print(f"Você recuperou 30 de vida! Vida atual: {vida}")
                        else:
                            print("\nSem poções!")
                            time.sleep(1)

                # FINAL
                if vida > 0:
                    print("\n" + "=" * 40)
                    print("VOCÊ SALVOU A CIDADE DE AVERNO!")
                    print("=" * 40)
                    print(f"Herói: {nome}")
                    print(f"Ouro final: {ouro}")
                    break
                else:
                    print(f"\nVocê foi derrotado pelo {chefe['nome']}...")

    # DESCANSAR
    elif escolha == "2":
        vida += 30

        if vida > vida_total:
            vida = vida_total

        print("\nVocê descansou e recuperou energia!")
    
    # LOJA
    elif escolha == "3":
        print("\nVocê se depara com uma loja ambulante, ele oferece alguns produtos")
        print("\n1 - Comprar Poção $25")
        print("\n2  - Comprar Armadura $35 (aumenta defesa em 5)")
        print("\n3  - Evoluir Arma $40 (aumenta ataque em 5 )")
        print("4 - Sair da loja")

        loja = input("\nEscolha: ")
        if loja == "1":
            if ouro >= 25:
                ouro -= 25
                pocao += 1
                print("\nVocê comprou uma poção")
                time.sleep(1)
            else:
                print("\nSem ouro suficiente")
        elif loja == "2":
            if ouro >= 35:
                ouro -= 35
                defesa += 5
                print("\nVocê comprou uma armadura")
                time.sleep(1)
            else:
                print("\nSem ouro suficiente")
        elif loja == "3":
            if ouro >= 40:
                ouro -= 40
                ataque += 5
                print("\nVocê evoluiu sua arma")
                time.sleep(1)
            else:
                print("\nSem ouro suficiente")
        elif loja == "4":
            print("\nVocê saiu da loja") 
        else:
            print("\nEscolha inválida!")
    
              

    # SAIR
    elif escolha == "4":
        print("\nVocê desistiu da aventura.")
        time.sleep(1)
        print("""
  ██████╗  █████╗ ███╗   ███╗███████╗
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
 ██║  ███╗███████║██╔████╔██║█████╗
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

   ██████╗ ██╗   ██╗███████╗██████╗
  ██╔═══██╗██║   ██║██╔════╝██╔══██╗
  ██║   ██║██║   ██║█████╗  ██████╔╝
  ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
  ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
   ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
""")
        break

    else:
        print("\nEscolha inválida!")

# GAME OVER
if vida <= 0:
    time.sleep(1)
    print("\nVocê morreu em sua aventura...")
    time.sleep(1)
    print("\n" + "=" * 40)
    print("""
  ██████╗  █████╗ ███╗   ███╗███████╗
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
 ██║  ███╗███████║██╔████╔██║█████╗
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

   ██████╗ ██╗   ██╗███████╗██████╗
  ██╔═══██╗██║   ██║██╔════╝██╔══██╗
  ██║   ██║██║   ██║█████╗  ██████╔╝
  ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
  ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
   ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
""")
    print("=" * 40)