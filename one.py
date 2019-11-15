import random

# from enum import Enum
from enum import Enum
from getpass import getpass

POWER = 100


class Choice(Enum):
    rock = 1
    paper = 2
    scissors = 3


class Person:
    hp = 100
    power = POWER
    name = ''

    def __init__(self, name_, is_bot=False):
        """

        :param name_: str
        :param is_bot: bool
        """
        self.inventory = []
        self.is_bot = is_bot
        self.name = name_

    def hit(self, other):
        """

        :rtype: Person
        """
        other.hp -= self.power
        print(f'{other} got kicked by {self}. Lost {self.power} hp({other.hp} total)')

    def rps(self, result=None):
        """

        :param result: String
        :return: Choice
        """
        print(f'{self} has to choose rock/paper/scissors')
        while True:
            if not result:
                result = getpass('r/p/s: \n')
            if result == 'r':
                return Choice.rock
            elif result == 'p':
                return Choice.paper
            elif result == 's':
                return Choice.scissors

    def attack(self, other):
        """

        :param other: Person
        """
        print(f'{self} battling with {other}')
        rps = self.rps()
        # if not other.is_bot:
        his_rps = other.rps()
        fight_result = self.rps_result(rps, his_rps)
        winner = self if fight_result == 1 else (None if fight_result == 0 else other)
        looser = self if fight_result == -1 else (None if fight_result == 0 else other)
        if winner and looser:
            winner.hit(looser)
        else:
            print('Its a tie')

    def __str__(self):
        return f'Person {self.name}'

    @staticmethod
    def rps_result(rps1, rps2):
        """
        :param rps1: Choice
        :param rps2: Choice
        :return: 1 if rps1 wins
                 0 if tie
                 -1 if rps2 wins
        """
        if type(rps1) != Choice or type(rps2) != Choice:
            raise ValueError(f'Bad rps types: should be Choice, got {type(rps1)} {type(rps2)}')
        rock = Choice.rock
        paper = Choice.paper
        scisscors = Choice.scissors
        if rps1 == rock:
            return 1 if rps2 == scisscors else (0 if rps2 == rock else -1)
        elif rps1 == paper:
            return 1 if rps2 == rock else (0 if rps2 == paper else -1)
        elif rps1 == scisscors:
            return 1 if rps2 == paper else (0 if rps2 == scisscors else -1)
        else:
            return TypeError('bad values')


class Game:
    def __init__(self):
        self.players = []
        self.final_phrase = 'Boomer loomer'

    def run(self):
        print('The game has started')
        name = input('Enter your name\n')
        self.players = []
        player = Person(name)
        self.players.append(player)
        choice = ''
        while choice != 's' and choice != 'm':
            choice = input('solo(s)/multiplayer(m)?\n')
        if choice == 'm':
            player2 = input('Player2 name\n ')
            new_person = Person(player2)
            self.players.append(new_person)

        while all(x.hp > 0 for x in self.players):
            for i in range(len(self.players)):
                new_list = list(self.players)
                new_list.remove(new_list[i])
                self.players[i].attack(random.choice(new_list))

        for x in self.players:
            if x.hp <= 0:
                print(f'{x} is dead! Thanks for playing. {self.final_phrase}')

        # print(random.choice(list(Choice)))


if __name__ == '__main__':
    game = Game()
    game.run()
