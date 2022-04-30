class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.position = [x, y]
        self.status = 'LIVE'
        self.item = None
        self.attack = 1
        self.defence = 1

    def __str__(self):
        return self.name

    def jsonify(self):
        return [self.position, self.status, self.item.name if self.item else None, self.attack, self.defence]

    def update_position(self, position):
        updated = False
        if position == 'N':
            if self.position[0] != 0:
                self.position[0] -= 1
                updated = True

        elif position == 'S':
            if self.position[0] != 7:
                self.position[0] += 1
                updated = True
        elif position == 'W':
            if self.position[1] != 0:
                self.position[1] -= 1
                updated = True
        elif position == 'E':
            if self.position[1] != 7:
                self.position[1] += 1
                updated = True
        else:
            print(f'Invalid position value: {position}')
        if updated:
            if self.item:
                self.item.position = self.position
            return True
        self.drowned()
        return False

    def drowned(self):
        if self.item:
            self.item.status = False
            self.item = None
        self.status = 'DROWNED'
        self.position = None
        self.attack = 0
        self.defence = 0

    def dead(self):
        if self.item:
            self.item.status = False
            self.item = None
        self.status = 'DEAD'
        self.attack = 0
        self.defence = 0

    def take_move(self, position):
        if self.status == 'DROWNED':
            print(f'{self.name} is DROWNED')
            return False

        return self.update_position(position)
