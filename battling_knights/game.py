import json
from item import Item
from player import Player


class Game:
    def __init__(self, moves):
        self.players = {
            'R': Player('red', 0, 0),
            'B': Player('blue', 7, 0),
            'G': Player('green', 7, 7),
            'Y': Player('yellow', 0, 7)
        }

        self.items = {
            'A': Item('axe', 2, 2, 2, 0),
            'M': Item('magic_staff', 5, 5, 1, 1),
            'D': Item('dagger', 2, 5, 1, 0),
            'H': Item('helmet', 5, 2, 0, 1)
        }
        self.moves = moves
        self.lets_play()

    def lets_play(self):
        for move in self.moves:
            self.take_move(move)
        self.jsonify()

    def take_move(self, input):
        player, move = input.split(':')
        player = self.players.get(player)
        if player.take_move(move):
            self.equip_item(player)
            self.check_enemy(player)

    def check_enemy(self, player):
        for new_player in self.players:
            new_player = self.players[new_player]
            if player != new_player and player.position == new_player.position:
                if new_player.status == 'LIVE':
                    player.attack += 0.5
                    self.lets_fight(player, new_player)
                    break

    def lets_fight(self, player, new_player):
        if player.attack >= new_player.defence:
            new_player.dead()
        else:
            player.dead()

    def equip_item(self, player):
        for item in self.items:
            if player.position == self.items[item].position:
                if self.items[item].status == False:
                    self.items[item].status = True
                    player.item = self.items[item]
                    player.attack += self.items[item].attack
                    player.defence += self.items[item].defence
                    break

    def print(self):
        for _ in self.players:
            print(self.players[_])

        for _ in self.items:
            print(self.items[_])

    def jsonify(self):
        data = dict()
        for _ in self.players:
            data[str(self.players[_])] = self.players[_].jsonify()

        for _ in self.items:
            data[str(self.items[_])] = self.items[_].jsonify()

        with open("final_state.json", "w") as outfile:
            json.dump(data, outfile, indent=4)


if __name__ == '__main__':
    with open("moves.txt", "r") as f:
        moves = f.readlines()
    moves = [_.strip() for _ in moves]
    Game(moves)
