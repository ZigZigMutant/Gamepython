import random

# STATUS DO JOGADOR
vida = 100
ouro = 0
pocao = 2

# INIMIGOS
inimigos = ["Goblin", "Esqueleto", "Bandido", "Lobo Atroz"]

print("=" * 40)
print("  Nome do jogo kaksdkasjh")
print("=" * 40)

nome = input("Digite o nome do seu herói: ")

print(f"\nBem-vindo, {nome}!")
print(" Textinho 1.")
print("textinho 2.\n")

# LOOP PRINCIPAL
while vida > 0:

    print("\n" + "-" * 40)
    print(f"Vida: {vida}")
    print(f"Poções: {pocao}")
    print(f"Ouro: {ouro}")
    print("-" * 40)

    print("\nVocê encontra uma estrada.")
    print("1 - Explorar")
    print("2 - Descansar")
    print("3 - Sair do jogo")

    escolha = input("Escolha: ")

    # EXPLORAR
    if escolha == "1":

        inimigo = random.choice(inimigos)
        vida_inimigo = random.randint(30, 60)

        print(f"\nUm {inimigo} apareceu!")

        # COMBATE
        while vida_inimigo > 0 and vida > 0:

            print("\n--- COMBATE ---")
            print(f"Sua vida: {vida}")
            print(f"Vida do {inimigo}: {vida_inimigo}")

            print("\n1 - Atacar")
            print("2 - Usar poção")
            print("3 - Fugir")

            acao = input("Escolha: ")

            # ATAQUE
            if acao == "1":
                dano = random.randint(10, 25)
                vida_inimigo -= dano

                print(f"\nVocê causou {dano} de dano!")

                if vida_inimigo > 0:
                    dano_inimigo = random.randint(5, 20)
                    vida -= dano_inimigo

                    print(f"O {inimigo} atacou você!")
                    print(f"Você perdeu {dano_inimigo} de vida.")

            # POÇÃO
            elif acao == "2":
                if pocao > 0:
                    cura = random.randint(20, 35)
                    vida += cura
                    pocao -= 1

                    if vida > 100:
                        vida = 100

                    print(f"\nVocê recuperou {cura} de vida!")
                else:
                    print("\nVocê não possui poções!")

            # FUGIR
            elif acao == "3":
                print(f"\nVocê fugiu do {inimigo}!")
                break

            else:
                print("\nEscolha inválida!")

        # VITÓRIA
        if vida_inimigo <= 0:
            recompensa = random.randint(10, 30)
            ouro += recompensa

            print(f"\nVocê derrotou o {inimigo}!")
            print(f"Ganhou {recompensa} moedas de ouro!")

            # CHEFE FINAL
            if ouro >= 100:
                print("\n" + "=" * 40)
                print("O REI DEMÔNIO SURGIU!")
                print("=" * 40)

                chefe_vida = 120

                while chefe_vida > 0 and vida > 0:

                    print(f"\nSua vida: {vida}")
                    print(f"Vida do Rei Demônio: {chefe_vida}")

                    print("\n1 - Atacar")
                    print("2 - Usar poção")

                    boss = input("Escolha: ")

                    if boss == "1":
                        dano = random.randint(15, 30)
                        chefe_vida -= dano

                        print(f"\nVocê causou {dano} de dano!")

                        if chefe_vida > 0:
                            dano_chefe = random.randint(15, 25)
                            vida -= dano_chefe

                            print(f"O Rei Demônio atacou!")
                            print(f"Você perdeu {dano_chefe} de vida.")

                    elif boss == "2":
                        if pocao > 0:
                            vida += 30
                            pocao -= 1

                            if vida > 100:
                                vida = 100

                            print("\nVocê usou uma poção!")
                        else:
                            print("\nSem poções!")

                # FINAL
                if vida > 0:
                    print("\n" + "=" * 40)
                    print("VOCÊ SALVOU A CIDADE DE AVERNO!")
                    print("=" * 40)
                    print(f"Herói: {nome}")
                    print(f"Ouro final: {ouro}")
                    break
                else:
                    print("\nVocê foi derrotado pelo Rei Demônio...")

    # DESCANSAR
    elif escolha == "2":
        vida += 20

        if vida > 100:
            vida = 100

        print("\nVocê descansou e recuperou energia!")

    # SAIR
    elif escolha == "3":
        print("\nVocê desistiu da aventura.")
        break

    else:
        print("\nEscolha inválida!")

# GAME OVER
if vida <= 0:
    print("\n" + "=" * 40)
    print("GAME OVER")
    print("=" * 40)