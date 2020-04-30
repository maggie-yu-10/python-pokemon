class Pokemon(object):
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)

if __name__ == "__main__":
    pokemon = Pokemon()
    pokemon.printName()