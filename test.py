import pyxel

class PokemonGame:
    def __init__(self):
        pyxel.init(160, 120, title="Mon Jeu Pokémon")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

if __name__ == "__main__":
    PokemonGame()