import pygame
import tilemanager
import ast

pygame.init()
pygame.font.init()

class TileEditor:import ast

class TileEditor:
    def __init__(self):
        self.tilemap_width = input("Enter tilemap width: ")
        self.tilemap_length = input("Enter tilemap length: ")  # Fixed typo: lenght -> length
        self.mode = input("Paste in the world or leave empty for a new one: ")

        #self.tilemap_width = 20
        #self.tilemap_length = 20
        #self.mode = ""

        self.window_size = (600, 600)
        self.screen = pygame.display.set_mode(self.window_size, pygame.SRCALPHA)
        pygame.display.set_caption("Tile Editor")
        self.clock = pygame.time.Clock()
        self.running = True

        self.internal_surface = pygame.Surface((2000, 2000), pygame.SRCALPHA)
        self.ui_surface = pygame.Surface(self.window_size, pygame.SRCALPHA)

        self.viewportx = 0
        self.viewporty = 0

        self.tilemap_width = int(self.tilemap_width)
        self.tilemap_length = int(self.tilemap_length)

        self.world = []
        if self.mode.strip() == "":
            for row in range(self.tilemap_length):
                tile_list = ["1" for _ in range(self.tilemap_width)]
                self.world.append(tile_list)
        else:
            try:
                # Parse the string representation of the 2D list
                parsed_world = ast.literal_eval(self.mode)
                # Validate that parsed_world is a 2D list with valid tile IDs
                if not isinstance(parsed_world, list) or not all(isinstance(row, list) for row in parsed_world):
                    raise ValueError("Invalid world format: must be a 2D list")
                if len(parsed_world) != self.tilemap_length or any(len(row) != self.tilemap_width for row in parsed_world):
                    raise ValueError("World dimensions do not match specified width and length")
                # Validate tile IDs
                valid_tile_ids = set(tilemanager.tiles.keys())
                for row in parsed_world:
                    for tile_id in row:
                        if tile_id not in valid_tile_ids:
                            raise ValueError(f"Invalid tile ID: {tile_id}")
                self.world = parsed_world
            except (ValueError, SyntaxError) as e:
                print(f"Error parsing world data: {e}. Initializing with default world.")
                for row in range(self.tilemap_length):
                    tile_list = ["1" for _ in range(self.tilemap_width)]
                    self.world.append(tile_list)

        self.sub_world = self.world  # This assumes sub_world should mirror world
        self.tile_slot_list = []
        self.draw_queue = []

        self.bottom_thing_rect = pygame.Rect(0, self.window_size[1] - 64, 600, 64)  # Adjusted height for clarity
        self.selected_slot_id = "2"
        self.rect_scroll = 0

        tilemanager.setup_surfaces(64)
        tilemanager.initialize_tilemap(self.world, self.sub_world, self.tilemap_width, self.tilemap_length, 0, 0, self.tile_slot_list)
    def _event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.rect_scroll += 1
                if event.button == 5:
                    self.rect_scroll -= 1
    
    def update(self):
        self._event_handling()
        self.screen.fill("cadetblue1")
        self.internal_surface.fill("cadetblue1")
        self.draw_queue = []


        mouse_pos = (pygame.mouse.get_pos()[0] - self.viewportx, pygame.mouse.get_pos()[1] - self.viewporty)
        actual_ducking_mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        right_mouse_key_pressed = pygame.mouse.get_pressed()[0]
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_UP]:
            self.viewporty += 5
        if keys[pygame.K_DOWN]:
            self.viewporty -= 5
        if keys[pygame.K_RIGHT]:
            self.viewportx -= 5
        if keys[pygame.K_LEFT]:
            self.viewportx += 5
        
        for tile in self.tile_slot_list:
            self.draw_queue.append(tile)

        if right_mouse_key_pressed:
            if actual_ducking_mouse_pos[1] > self.window_size[1] - 64:
                if (((mouse_pos[0] - (self.rect_scroll * 64)) + self.viewportx) // 64) > 0:
                    self.selected_slot_id = str(((mouse_pos[0] - (self.rect_scroll * 64)) + self.viewportx) // 64)
            else:
                if mouse_pos[0] // 64 < self.tilemap_width and mouse_pos[1] // 64 < self.tilemap_length:
                    self.world[mouse_pos[1] // 64][mouse_pos[0] // 64] = self.selected_slot_id

        tilemanager.update_tile_map(self.world, self.sub_world, self.tile_slot_list, self.tilemap_width, 64, 0, 0, self.internal_surface, self.draw_queue)



        self.screen.blit(self.internal_surface, (self.viewportx, self.viewporty))
        
        pygame.draw.rect(self.screen, (227, 227, 227), self.bottom_thing_rect)
        
        for tile_idx, tile in enumerate(tilemanager.tiles):
            tile_surface = tilemanager.tiles[tile][0]["surface"]

            self.screen.blit(tile_surface, (((tile_idx + 1) % (self.window_size[0]) + self.rect_scroll) * 64, self.bottom_thing_rect.y))

        if keys[pygame.K_c]:
            print(self.world)

        self.clock.tick(60)
        pygame.display.flip()

tileeditor = TileEditor()

while tileeditor.running:
    tileeditor.update()