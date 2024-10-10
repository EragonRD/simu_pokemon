import pygame
import sys
import json

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre et les couleurs
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_RED = (139, 0, 0)
LIGHT_RED = (255, 102, 102)
GRAY = (200, 200, 200)

# Charger la liste des Pokémon depuis le fichier JSON
with open("pokemon_list.json", "r") as f:
    pokemon_data = json.load(f)

pokemons = pokemon_data["pokemons"]  # Récupère la liste des Pokémon


class Button:
    """Classe pour représenter un bouton stylisé."""
    def __init__(self, text, x, y, width, height, font, color_text, color_button, hover_color, selected_color=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.color_text = color_text
        self.color_button = color_button
        self.hover_color = hover_color
        self.selected_color = selected_color  # Couleur lorsque le bouton est sélectionné
        self.text_surface = self.font.render(self.text, True, self.color_text)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.is_hovered = False

    def draw(self, screen, selected=False):
        """Dessine le bouton avec style et effet de survol."""
        if selected:
            pygame.draw.rect(screen, self.selected_color, self.rect, border_radius=10)  # Utilise la couleur sélectionnée
        elif self.is_hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.color_button, self.rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.rect, 3, border_radius=10)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, mouse_pos):
        """Vérifie si le bouton est cliqué."""
        return self.rect.collidepoint(mouse_pos)

    def update_hover_state(self, mouse_pos):
        """Met à jour l'état de survol du bouton."""
        self.is_hovered = self.rect.collidepoint(mouse_pos)


class TextInputBox:
    """Classe pour représenter une zone de texte pour saisir des noms."""
    def __init__(self, x, y, w, h, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = ''
        self.font = font
        self.active = False
        self.text_surface = self.font.render(self.text, True, self.color)

    def handle_event(self, event):
        """Gérer l'entrée utilisateur pour la zone de texte."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si l'utilisateur clique dans la zone de texte
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        """Dessine la zone de texte et le texte entré."""
        pygame.draw.rect(screen, WHITE, self.rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text


class Menu:
    """Classe pour représenter le menu principal avec un titre."""
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, 100)  # Police pour le titre
        self.font = pygame.font.Font(None, 74)  # Police pour les boutons
        self.title_text = self.title_font.render("PokeCombat", True, BLACK)
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, 100))
        
        # Bouton "Start" avec un nouveau style
        self.start_button = Button("Start", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100, 
                                   self.font, BLACK, DARK_RED, LIGHT_RED)

    def display(self):
        """Affiche le menu principal avec un titre."""
        self.screen.fill(GRAY)  # Fond gris pour un style différent
        # Afficher le titre
        self.screen.blit(self.title_text, self.title_rect)
        # Afficher le bouton "Start"
        self.start_button.draw(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        """Gère les événements pour le menu."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_clicked(event.pos):
                return "player_input"
        return "menu"

    def update(self, mouse_pos):
        """Met à jour l'état des éléments en fonction de la position de la souris."""
        self.start_button.update_hover_state(mouse_pos)


class PlayerInput:
    """Classe pour gérer l'entrée des noms des joueurs."""
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.player1_input = TextInputBox(WIDTH // 2 - 150, HEIGHT // 2 - 100, 300, 50, self.font)
        self.player2_input = TextInputBox(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 50, self.font)
        self.start_button = Button("Next", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, self.font, BLACK, DARK_RED, LIGHT_RED)
    
    def display(self):
        """Affiche l'interface pour entrer les noms des joueurs."""
        self.screen.fill(WHITE)
        prompt1 = self.font.render("Nom Joueur 1:", True, BLACK)
        prompt2 = self.font.render("Nom Joueur 2:", True, BLACK)
        self.screen.blit(prompt1, (WIDTH // 2 - 150, HEIGHT // 2 - 150))
        self.screen.blit(prompt2, (WIDTH // 2 - 150, HEIGHT // 2))
        
        self.player1_input.draw(self.screen)
        self.player2_input.draw(self.screen)
        self.start_button.draw(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        """Gère les événements pour la saisie des noms."""
        self.player1_input.handle_event(event)
        self.player2_input.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_clicked(event.pos):
                if self.player1_input.get_text() and self.player2_input.get_text():
                    return "choose_pokemon", self.player1_input.get_text(), self.player2_input.get_text()
        return "player_input", None, None


class ChoosePokemon:
    """Classe pour choisir un Pokémon avec un menu défilant pour deux joueurs."""
    def __init__(self, screen, player1_name, player2_name):
        self.screen = screen
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.font = pygame.font.Font(None, 36)

        # Charger les Pokémon depuis le fichier JSON
        with open("pokemon_list.json", "r") as f:
            pokemon_data = json.load(f)

        # On récupère la liste des noms de Pokémon directement
        self.pokemons = pokemon_data["pokemons"]

        # Dimensions pour les boutons
        self.button_width = 150
        self.button_height = 50
        self.margin_x = 20  # Espace horizontal entre les boutons
        self.margin_y = 20  # Espace vertical entre les boutons

        # Calculer le nombre de colonnes et la hauteur totale de la surface défilante
        self.columns = (WIDTH - self.margin_x) // (self.button_width + self.margin_x)
        self.total_rows = (len(self.pokemons) + self.columns - 1) // self.columns  # Nombre total de lignes
        self.scroll_offset = 0  # Décalage pour le défilement

        # Taille de la surface défilante (scrollable)
        self.scroll_surface_height = self.total_rows * (self.button_height + self.margin_y) + self.margin_y
        self.scroll_surface = pygame.Surface((WIDTH, self.scroll_surface_height))  # Crée une surface défilante

        # Créer les boutons pour chaque Pokémon
        self.pokemon_buttons = []
        for idx, pokemon in enumerate(self.pokemons):
            row = idx // self.columns
            col = idx % self.columns
            x = col * (self.button_width + self.margin_x) + self.margin_x
            y = row * (self.button_height + self.margin_y) + self.margin_y
            btn = Button(pokemon, x, y, self.button_width, self.button_height, self.font, BLACK, GRAY, LIGHT_RED, LIGHT_RED)
            self.pokemon_buttons.append(btn)

        self.selected_pokemon1 = None
        self.selected_pokemon2 = None  # Ajouter une variable pour le Pokémon du joueur 2
        self.current_player = 1  # Indique quel joueur est en train de sélectionner
        self.confirm_button = Button("Valider", WIDTH // 2 - 100, HEIGHT - 80, 200, 50, self.font, BLACK, DARK_RED, LIGHT_RED)

    def display(self):
        """Affiche l'interface pour sélectionner les Pokémon avec un menu défilant."""
        self.screen.fill(WHITE)
        player_prompt = self.font.render(f"{self.player1_name} choisit son Pokémon :", True, BLACK) if self.current_player == 1 else self.font.render(f"{self.player2_name} choisit son Pokémon :", True, BLACK)
        self.screen.blit(player_prompt, (WIDTH // 2 - 200, 50))

        # Afficher une portion de la surface défilante (décalée par le défilement)
        self.scroll_surface.fill(WHITE)
        for button in self.pokemon_buttons:
            is_selected = (self.current_player == 1 and button.text == self.selected_pokemon1) or (self.current_player == 2 and button.text == self.selected_pokemon2)
            button.draw(self.scroll_surface, selected=is_selected)

        # Afficher la portion visible de la surface défilante
        self.screen.blit(self.scroll_surface, (0, 100), (0, self.scroll_offset, WIDTH, HEIGHT - 200))

        # Afficher le bouton de validation seulement si un Pokémon est sélectionné
        if (self.current_player == 1 and self.selected_pokemon1) or (self.current_player == 2 and self.selected_pokemon2):
            self.confirm_button.draw(self.screen)

        pygame.display.flip()

    def handle_event(self, event):
        """Gère les événements pour la sélection des Pokémon."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le bouton de validation est cliqué
            if self.current_player == 1 and self.selected_pokemon1 and self.confirm_button.is_clicked(event.pos):
                self.current_player = 2  # Passer au joueur 2
                self.selected_pokemon2 = None  # Réinitialiser la sélection du joueur 2
            elif self.current_player == 2 and self.selected_pokemon2 and self.confirm_button.is_clicked(event.pos):
                return "start_game"  # Validation finale pour le joueur 2

            # Vérifier les boutons de Pokémon (ajuster les coordonnées pour le défilement)
            for button in self.pokemon_buttons:
                if button.is_clicked((event.pos[0], event.pos[1] + self.scroll_offset - 100)):
                    if self.current_player == 1:
                        self.selected_pokemon1 = button.text  # Enregistrer le Pokémon sélectionné pour le joueur 1
                    else:
                        self.selected_pokemon2 = button.text  # Enregistrer le Pokémon sélectionné pour le joueur 2
                    return "choose_pokemon"

        # Gérer le défilement avec la molette
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_offset -= event.y * 20  # Ajuster la vitesse du défilement ici
            # Limiter le défilement pour ne pas sortir de la surface
            self.scroll_offset = max(0, min(self.scroll_offset, self.scroll_surface_height - HEIGHT + 200))

        return "choose_pokemon"


class GameApp:
    """Classe principale pour gérer l'application."""
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PokeCombat - Menu")
        self.menu = Menu(self.screen)
        self.player_input = None
        self.choose_pokemon = None
        self.game = None
        self.state = "menu"  # "menu", "player_input", "choose_pokemon", "start_game"
        self.player1_name = ""
        self.player2_name = ""
        self.pokemon1 = ""
        self.pokemon2 = ""
    
    def run(self):
        """Boucle principale de l'application."""
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.state == "menu":
                    self.state = self.menu.handle_event(event)
                elif self.state == "player_input":
                    # Initialiser self.player_input si ce n'est pas déjà fait
                    if not self.player_input:
                        self.player_input = PlayerInput(self.screen)
                    self.state, self.player1_name, self.player2_name = self.player_input.handle_event(event)
                elif self.state == "choose_pokemon":
                    # Initialiser self.choose_pokemon si ce n'est pas déjà fait
                    if not self.choose_pokemon:
                        self.choose_pokemon = ChoosePokemon(self.screen, self.player1_name, self.player2_name)
                    result = self.choose_pokemon.handle_event(event)
                    if result == "start_game":
                        self.pokemon1 = self.choose_pokemon.selected_pokemon1
                        self.pokemon2 = self.choose_pokemon.selected_pokemon2
                        # Création de l'instance Game avec les arguments requis
                        self.game = Game(self.screen, self.player1_name, self.player2_name, self.pokemon1, self.pokemon2)
                        self.state = "start_game"

            # Met à jour les éléments selon l'état actuel
            if self.state == "menu":
                self.menu.update(mouse_pos)
                self.menu.display()
            elif self.state == "player_input":
                self.player_input.display()
            elif self.state == "choose_pokemon":
                if not self.choose_pokemon:
                    self.choose_pokemon = ChoosePokemon(self.screen, self.player1_name, self.player2_name)
                self.choose_pokemon.display()
            elif self.state == "start_game":
                if not self.game:
                    self.game = Game(self.screen, self.player1_name, self.player2_name, self.pokemon1, self.pokemon2)
                self.game.display()

            pygame.display.update()

        pygame.quit()
        sys.exit()


class Game:
    """Classe représentant l'écran de jeu où le combat entre Pokémon a lieu."""
    def __init__(self, screen, player1_name, player2_name, pokemon1, pokemon2):
        self.screen = screen
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
        # Points de vie pour chaque Pokémon
        self.hp1 = 100  # Vie du Pokémon 1
        self.hp2 = 100  # Vie du Pokémon 2
        
        # Capacités fictives
        self.abilities = ["Attaque 1", "Attaque 2", "Attaque 3", "Attaque 4"]
        
        self.font = pygame.font.Font(None, 36)

    def display(self):
        """Affiche l'écran de jeu."""
        self.screen.fill((50, 150, 50))  # Couleur de fond pour l'écran du jeu
        
        # Affichage des informations sur les joueurs
        self.display_player_info()

        # Affichage des capacités
        self.display_abilities()

        # Affichage des instructions
        font_small = pygame.font.Font(None, 36)
        instructions = font_small.render("Cliquez sur une capacité pour attaquer.", True, (255, 255, 255))
        self.screen.blit(instructions, (250, 550))

        pygame.display.flip()

    def display_player_info(self):
        """Affiche les informations des joueurs dans un bloc séparé."""
        # Dimensions du bloc pour chaque joueur
        block_width = 300
        block_height = 100
        
        # Bloc pour le joueur 1 (à gauche)
        player1_block = pygame.Rect(50, 50, block_width, block_height)
        pygame.draw.rect(self.screen, (255, 255, 255), player1_block, 0, border_radius=10)  # Fond blanc
        pygame.draw.rect(self.screen, (0, 0, 0), player1_block, 3, border_radius=10)  # Bordure noire
        
        # Texte pour le joueur 1
        player1_name_text = self.font.render(self.player1_name, True, (0, 0, 0))
        pokemon1_name_text = self.font.render(self.pokemon1, True, (0, 0, 0))
        hp1_text = self.font.render(f"HP: {self.hp1}", True, (0, 0, 0))

        # Afficher le nom du joueur et du Pokémon
        self.screen.blit(player1_name_text, (player1_block.x + 10, player1_block.y + 10))  # Nom du joueur
        self.screen.blit(pokemon1_name_text, (player1_block.x + 10, player1_block.y + 40))  # Nom du Pokémon
        self.screen.blit(hp1_text, (player1_block.x + 200, player1_block.y + 40))  # Points de vie du Pokémon
        
        # Bloc pour le joueur 2 (à droite)
        player2_block = pygame.Rect(WIDTH - block_width - 50, 50, block_width, block_height)
        pygame.draw.rect(self.screen, (255, 255, 255), player2_block, 0, border_radius=10)  # Fond blanc
        pygame.draw.rect(self.screen, (0, 0, 0), player2_block, 3, border_radius=10)  # Bordure noire
        
        # Texte pour le joueur 2
        player2_name_text = self.font.render(self.player2_name, True, (0, 0, 0))
        pokemon2_name_text = self.font.render(self.pokemon2, True, (0, 0, 0))
        hp2_text = self.font.render(f"HP: {self.hp2}", True, (0, 0, 0))

        # Afficher le nom du joueur et du Pokémon
        self.screen.blit(player2_name_text, (player2_block.x + 10, player2_block.y + 10))  # Nom du joueur
        self.screen.blit(pokemon2_name_text, (player2_block.x + 10, player2_block.y + 40))  # Nom du Pokémon
        self.screen.blit(hp2_text, (player2_block.x + 200, player2_block.y + 40))  # Points de vie du Pokémon

    def display_abilities(self):
        """Affiche les blocs des capacités."""
        ability_width = 150
        ability_height = 50
        x_start = (WIDTH // 2) - (ability_width * 2)
        y_start = HEIGHT - 100

        for idx, ability in enumerate(self.abilities):
            # Calculer la position de chaque capacité
            x = x_start + (idx * ability_width)
            y = y_start
            
            # Dessiner le rectangle pour la capacité
            pygame.draw.rect(self.screen, (255, 255, 255), (x, y, ability_width, ability_height), 0, border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, ability_width, ability_height), 2, border_radius=10)

            # Afficher le texte de la capacité
            ability_text = self.font.render(ability, True, (0, 0, 0))
            text_rect = ability_text.get_rect(center=(x + ability_width // 2, y + ability_height // 2))
            self.screen.blit(ability_text, text_rect)

    def handle_event(self, event):
        """Gère les événements du jeu."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifie si un bloc d'attaque a été cliqué
            mouse_pos = event.pos
            self.check_ability_click(mouse_pos)

    def check_ability_click(self, mouse_pos):
        """Vérifie si une capacité a été cliquée."""
        ability_width = 150
        ability_height = 50
        x_start = (WIDTH // 2) - (ability_width * 2)
        y_start = HEIGHT - 100

        for idx in range(len(self.abilities)):
            x = x_start + (idx * ability_width)
            y = y_start
            
            if x <= mouse_pos[0] <= x + ability_width and y <= mouse_pos[1] <= y + ability_height:
                print(f"{self.player1_name} a utilisé {self.abilities[idx]}!")  # Remplacer par la logique de combat

# Démarrage de l'application
if __name__ == "__main__":
    app = GameApp()
    app.run()