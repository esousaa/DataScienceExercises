# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        # Váriavel que recebe a palvra que será utilizada no jogo
        self.word = word
        # Váriavel que será a mascará da palavra
        self.word_mask = list("_" * len(self.word))
        # Lista que controla os palpites corretos
        self.right = []
        # Lista que controla os palpites errados
        self.wrong = []
        # Váriavel para guardar o título do jogo
        self.title = "		>>>>>>>>>>Hangman<<<<<<<<<<"
        # Váriavel que apresenta o nível de erros do jogador
        self.board = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''']
        # Acerta a palavra e a mascara eliminando os espaços
        self.valida_word()


    # Método que valida o palpite do jogador
    def guess(self, letter):
        valida = False
        for i in range(0,len(self.word)):
            if self.word[i] == letter:
                self.word_mask[i] = letter
                valida = True
        if valida == True:
           self.right.append(letter)
        else:
            self.wrong.append(letter)


    # Método para verificar se o jogo terminou
    def hangman_status(self):
        if "".join(self.word_mask) == self.word:
            return 0
        else:
            return 1

    # Método que valida se a letra informada, já foi informada nas jogadas anteriores
    def valida_palpite( self, letra ) :
        if self.wrong.count(letra) > 0 or self.right.count(letra) > 0:
            return False
        else:
            return True


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        finish = False
        if len(self.wrong) <= (len(self.board)-2):
            status = Hangman.hangman_status(self)
            if status > 0:
                self.clear_screen()
                print(self.title + "\n")
                print(self.board[len(self.wrong)] + "\n\n")
                print("Palavra : " + "".join(self.word_mask) + "\n")
                print("Palpites corretos:\n" + ",".join(map(str, self.right)) + "\n")
                print("Palpites errados:\n" + ",".join(map(str, self.wrong)) + "\n")
                correto = False
                while correto == False:
                    try:
                        letra = input("Informe uma letra: \n")[0]
                        correto = letra.isalpha()
                        if correto == True:
                            valida_letra = self.valida_palpite(letra)
                            if valida_letra == True:
                                self.guess(letra)
                                continue
                            else:
                                print("Esta letra já foi informada. Favor informar uma nova letra.!")
                                correto = False
                        else:
                           print("O jogo só aceita lestras. Favor informar uma letra.")
                    except :
                       continue
            else:
                self.clear_screen()
                print(self.title + "\n")
                print(self.board[len(self.wrong)] + "\n\n")
                print("Palavra : " + "".join(self.word_mask) + "\n")
                print("Parabéns você venceu o Jogo!\n")
                finish = True
        else:
            self.clear_screen()
            print(self.title + "\n")
            print(self.board[len(self.wrong)] + "\n\n")
            print('Game over! Você perdeu.\n')
            print('A palavra era ' + self.word)
            finish = True
        return finish
    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    # Método que substitui os espaços por traços
    def valida_word(self):
        if list(self.word).count(" ") == 1:
            self.word_mask[list(self.word).index(" ")] = "-"
            self.word = self.word.replace(" ","-")
        elif list(self.word).count(" ") > 1:
            for i in range(0,len(self.word)):
                if self.word[i] == " ":
                    self.word_mask[i] = "-"
            self.word = self.word.replace(" ", "-")

# Função para ler uma palavra de forma aleatória do banco de palavras
def start_game():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(start_game())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    # Verifica o status do jogo
    termina = False
    while termina == False:
        termina = game.print_game_status()

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
    main()
