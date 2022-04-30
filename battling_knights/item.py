class Item:
    def __init__(self, name, x, y, attack, defence):
        self.name = name
        self.position = [x, y]
        self.status = False
        self.attack = attack
        self.defence = defence

    def __str__(self):
        return self.name

    def jsonify(self):
        return [self.position, self.status]
