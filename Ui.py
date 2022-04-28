from abc import ABC, abstractmethod
from Game import Game, GameError

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def __get_input(self):
        while True:
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                if 1 <= row <= 3 and 1 <= col <= 3:
                    #Range check on input
                    break
                else:
                    print("Invalid input, please try again")
            except ValueError:
                print("Invalid input, please try again")
        return row,col


    def run(self):
        while self.__game.winner == None:
            print(self.__game)
            row,col = self.__get_input()
            try:
                self.__game.play(row,col)
            except GameError:
                print("Cannot play here!")

        print(self.__game)
        if self.__game.winner == Game.DRAW:
            print("The game was drawn")
        else:
            print(f"The winner is {self.__game.winner}")
