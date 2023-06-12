#bibliotecas
import random
from os import system, name

# Limpar o prompt a cada execução
def limpa_tela():
    #windows
    if name == 'nt':
        _= system('cls')
        #Mac ou Linux
    else:
        _=system('clear')
        
def game():
    limpa_tela()
    
    print('\nSe divirta!')
    print('Adivinhe qual é a fruta abaixo: \n')
    
    #lista de palavras
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'manga', 'melancia',
               'abacaxi', 'framboesa', 'cereja', 'amora', 'abacate', 'carambola']
    
    #escolher aleatoriamente uma palavra
    palavra = random.choice(palavras)
    
    #formação dos underline de acordo com a palavra
    letras_descobertas = ['_' for letra in palavra]
    
    #numero de chances
    chances = 6
    
    #lista para as letras erradas
    letras_erradas = []
    
    try:
        while chances > 0:
            print(' '.join(letras_descobertas))
            print('\nChances restantes:', chances)
            print('Letras erradas:', ' '.join(letras_erradas))

            while True:
                tentativa = input('\nDigite uma letra: ').lower()
                if tentativa.isalpha():
                    break
                else:
                    print('Por favor, digite apenas letras.')

            if tentativa in palavra:
                index = 0
                for letra in palavra:
                    if tentativa == letra:
                        letras_descobertas[index] = letra
                    index += 1
            else:
                chances -= 1
                letras_erradas.append(tentativa)

            if '_' not in letras_descobertas:
                print('\nVocê venceu! A palavra era:', palavra)
                break

        if '_' in letras_descobertas:
            print('\nVocê perdeu! A palavra era:', palavra)
            
    except ValueError:
        print('Digite uma letra')


#bloco main
if __name__ == '__main__':
    game()
    print(':)')
