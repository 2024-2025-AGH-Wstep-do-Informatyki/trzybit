import pygame

class AssetManager:
    def __init__(self):
        # Magazyn na wszystkie nasze zabawki: obrazki, dźwięki i czcionki
        self.images = {}
        self.sounds = {}
        self.fonts = {}

    def load_image(self, key, filepath):
        # Ładujemy obrazek - bo przecież gra bez grafiki to tekstówka
        self.images[key] = pygame.image.load(filepath).convert_alpha()

    def get_image(self, key):
        # Wyciągamy obrazek, jeśli istnieje. Jak nie, to... no cóż, masz problem
        return self.images.get(key)

    def load_sound(self, key, filepath):
        # Dźwięki, bo cisza w grze to jak film bez muzyki
        self.sounds[key] = pygame.mixer.Sound(filepath)

    def get_sound(self, key):
        # Podajemy dźwięk po kluczu. Prosta sprawa.
        return self.sounds.get(key)

    def load_font(self, key, filepath, size):
        # Czcionki dla tych, co lubią czytać w grach
        self.fonts[key] = pygame.font.Font(filepath, size)

    def get_font(self, key):
        # Wydobywamy font, jak archeolog w ruinach
        return self.fonts.get(key)

# Przyklad użycia tego cuda
if __name__ == "__main__":
    pygame.init()

    assets = AssetManager()
    assets.load_image("player", "assets/player.png")  # Nasz heros
    assets.load_sound("jump", "assets/jump.wav")      # Dźwięk skoku jak w Mario
    assets.load_font("default", "assets/font.ttf", 24)  # Defaultowa czcionka do komunikatów

    # Testujemy, czy działa. Jak nie, to debugger w dłoń.
    player_image = assets.get_image("player")
    jump_sound = assets.get_sound("jump")
    default_font = assets.get_font("default")
