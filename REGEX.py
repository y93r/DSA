#Música: Monolith (Tradução) - Stone Sour
musica = '''
Está errado da minha parte? Cheguei tão longe, tão rápido
Estou no escuro em relação a muitas coisas
Parece tão real pra mim!
Eu consagrei!
Queria poder odiar
Vi minhas mãos sangrentas ficarem limpas diante de meus olhos!

E eu ouço meus desejos e necessidades de novo, você pode me ajudar?
E ouço um outro tipo de novo, alguém me pare
E sinto a pressão em minha mente, estou louco?
E eu preciso mudar de pele, revelar o monolito dentro de mim

Visões incomodam meus sonhos - oh Deus, que besta fez isso?
Eu não poderia... Oh Jesus, eu somente não sei
O que está dentro de mim?
Eu profanei!
Meu Deus, eu amo odiar!
Minhas mãos estão sangrentas novamente, não tem motivo!

E eu ouço meus desejos e necessidades de novo, você pode me ajudar?
E ouço um outro tipo de novo, alguém me pare
E sinto a pressão em minha mente, estou louco?
E eu preciso mudar de pele, revelar o monolito dentro de mim

E eu ouço meus desejos e necessidades de novo, você pode me ajudar?
E ouço um outro tipo de novo, alguém me pare
E sinto a pressão em minha mente, estou louco?
E eu preciso mudar de pele, revelar o monolito dentro de mim

Dentro de mim!
'''

#1-REGEX para contar quantas vezes o caractere 'a' aparece
contador = len(re.findall(r'a', musica))
print(f'O caractere "a" aparece {contador} vezes.')

#2-REGEX para contar quantas vezes a palavra monolito
#O parâmetro flags=re.IGNORECASE é usado para tornar a busca de palavras insensível a maiúsculas e minúsculas
palavra = "monolito"

contador = len(re.findall(r'\b' + re.escape(palavra) + r'\b', musica, flags=re.IGNORECASE))
print(f'A palavra {palavra} aparece {contador} vezes')

#3-REGEX para extrair as palavras seguidas de exclamação
exclamacao = re.findall(r'\b(\w+)\!', musica)
print(f'As palavras que aparecem seguidas de uma "!" são: {exclamacao}')

#Bonus
interrogação = re.findall(r'\b(\w+)\?', musica)
print(f'As palavras que aparecem seguidas de uma "?" são: {interrogação}')

#4-REGEX que extrai qualquer palavra cujo antecessor seja a palavra "meus" e o sucessor seja "e"
padrao = r'\bmeus\s+(\w+)\s+e\b'

palavras = re.findall(padrao, musica, flags=re.IGNORECASE)
print(f'Palavras encontras: {palavras}')

#5-REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento
padrao = r'\b[\wÁ-ÿ]+[áéíóúâêîôûãõàèìòùäëïöüç]'

palavras = re.findall(padrao, musica, flags=re.IGNORECASE)
print(f'Lista de palavras: {palavras}')
