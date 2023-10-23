#Python 3.11.5

"""
    Jogo da Forca - é um jogo em que o jogador tem que acertar qual é a palavra proposta,
    tendo como dica o número de letras e o tema ligado à palavra. 
    A cada letra errada, é desenhado uma parte do corpo do enforcado. 
"""

print('-'*60)
print(f"| {'Jogo da Forca':^56} |")
print('-'*60)

palavra_secreta = 'casa'
jogadas = 0
vidas = 7
lista_de_letras_palpite_acertados = ''

while True:
    
    letra_palpite = input('Digite uma letra: ').lower()

    # Virifica se é um número.
    if letra_palpite.isdigit():
        print('-'*30)
        print(f'Entrada Invalida\n'
              f'Números não são permitidos.')
        print('-'*30)
        continue

    # Verifica se são mais de uma letra ou texto vazio.
    if len(letra_palpite) > 1 or not letra_palpite:
        print('-'*23)
        print(f"{'Jogada Invalida !':^23}")
        print('-'*23)
        continue



    palavra_palpite = ''

    # Adiciona letra em lista de letras Acertadas.
    if letra_palpite in palavra_secreta:
        lista_de_letras_palpite_acertados += letra_palpite

    else:
        # Numeros de Jogadas
        jogadas += 1

    for letra in palavra_secreta:
        if letra in lista_de_letras_palpite_acertados:
            palavra_palpite += letra
            
        else:
            palavra_palpite += '*'


    print(f'Palavra formada: {palavra_palpite}')
    print(f'Vidas: {vidas - jogadas}')

    if vidas == jogadas:
        print('Você perdeu !')
        break


    #Verifica a palavra
    if palavra_palpite == palavra_secreta:
        print('-'*30)
        print(f"{'Você ganhou !':^30}")
        print('-'*30)
        break

"""
    Desenvolvido por> Matheus de Faria
    SO: Debian GNU/Linux 12 (bookworm)
    Data: 22/10/2023
"""