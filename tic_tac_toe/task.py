from random import choice
from collections import Counter

class Cell:
    def __init__(self):
        self.__value = 0

    def __bool__(self):
        return not self.__value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, item):
        self.__value = item



class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2


    def __init__(self):
        self.pole = None


    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))


    def __getitem__(self, item):
        self.check(item)

        return self.pole[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.check(key)

        self.pole[key[0]][key[1]].value = value

    @classmethod
    def check(cls, key):
        if not isinstance(key, tuple) and not (set([type(key[0]), type(key[1])]) == set([int])):
            raise TypeError(f"Your {type(key)} or insert data not correct")

        if not (0 <= key[0] <= 2)  or not (0 <= key[1] <= 2):
            raise IndexError("Wrong index")

    def __bool__(self):
        if  any([self.human_win, self.computer_win]):
            return False
        return  0  in [j.value for i in self.pole for j in i]

    def show(self):
        result = []
        s = ''
        pole = self.pole
        for i in range(3):
            for j in range(3):
                if pole[i][j]:
                    result.append(' '.center(3))
                elif pole[i][j].value == 1:
                    result.append('X'.center(3))
                else:
                    result.append('O'.center(3))
            s += '-----------\n'
            s += '|'.join(result) + '\n'
            result = []
        s += '-----------'

        print(s)

    def human_go(self):
        try:
            a, b = map(int, input(f"Enter cords of your turn: ").split())

            if self.pole[a][b]:
                self.pole[a][b].value = self.HUMAN_X
            else:
                print("Choose other Cell")
                self.human_go()
        except Exception as e:
            print(f"You entered wrong type value {e}, must be Integer")
            self.human_go()

    def computer_go(self):
        if self:
            pole = self.pole
            a, b = choice([(i, j) for i in range(3) for j in range(3) if pole[i][j]])

            self.pole[a][b].value = self.COMPUTER_O

    @property
    def human_win(self):
        return self.__checker_win(self.HUMAN_X)

    @property
    def computer_win(self):
        return self.__checker_win(self.COMPUTER_O)


    def __checker_win(self, player):
        pole = [[j.value for j in i] for i in self.pole]
        dig_m, dig = [], []
        for i in range(3):
            row, col = pole[i], []
            dig_m.append(pole[i][i]), dig.append(pole[i][-(i+1)])
            for j in range(3):
                col.append(pole[j][i])
            if any([i.count(player) == 3 for i in [dig_m, dig, col, row]]):
                return True



game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.human_win:
    print("Congratulations! Human Win ")
elif game.computer_win:
    print("Skynet so close, be careful my chicken dumb human!")
else:
    print("Draw.")












