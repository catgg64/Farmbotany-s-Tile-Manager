import pygame
import tilemanager

pygame.init()
pygame.font.init()

class TileEditor:
    def __init__(self):
        #self.tilemap_width = input("Enter tilemap width:")
        #self.tilemap_lenght = input("Enter tilemap lenght:")

        self.tilemap_width = 20
        self.tilemap_lenght = 20

        self.window_size = (600, 600)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Tile Editor")
        self.clock = pygame.time.Clock()
        self.running = True

        self.internal_surface = pygame.Surface((2000, 2000))

        self.viewportx = 0
        self.viewporty = 0

        self.tilemap_width = int(self.tilemap_width)
        self.tilemap_lenght = int(self.tilemap_lenght)

        self.world = []

        for row in range(0, self.tilemap_lenght):
            tile_list = []
            for column in range(0, self.tilemap_width):
                tile_list.extend("1")
            self.world.append(tile_list)
        
        self.sub_world = self.world
        self.tile_slot_list = []
        self.draw_queue = []

        self.selected_slot_id = "2"
        self.rect_scroll = 0

        tilemanager.setup_surfaces(64)

        tilemanager.initialize_tilemap(self.world, self.sub_world, self.tilemap_width, self.tilemap_lenght, 0, 0, self.tile_slot_list)

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
        self.draw_queue = []

        self.bottom_thing_rect = pygame.Rect(0, self.window_size[0] - 64, 600, 600)

        print(self.rect_scroll)

        mouse_pos = (pygame.mouse.get_pos()[0] - self.viewportx, pygame.mouse.get_pos()[1] - self.viewporty)
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
            self.world[mouse_pos[1] // 64][mouse_pos[0] // 64] = self.selected_slot_id

        tilemanager.update_tile_map(self.world, self.sub_world, self.tile_slot_list, self.tilemap_width, 64, 0, 0, self.internal_surface, self.draw_queue)


        self.screen.blit(self.internal_surface, (self.viewportx, self.viewporty))
        
        pygame.draw.rect(self.screen, (227, 227, 227), self.bottom_thing_rect)
        
        for tile_idx, tile in enumerate(tilemanager.tiles):
            tile_surface = tilemanager.tiles[tile][0]["surface"]
#
 #           #print(tile_idx / (self.window_size[0] // 64))
 #           #print(round(tile_idx / (self.window_size[0])))
 #           #print(((tile_idx + 1) % (self.window_size[0] // 64)) * 64)
 #           #print(((tile_idx + 1) * 64) % self.window_size[0])
#
#            witch_column = tile_idx // (self.window_size[0] // 64)
#            
            self.screen.blit(tile_surface, (((tile_idx + 1) % (self.window_size[0]) + self.rect_scroll) * 64, self.bottom_thing_rect.y))

        self.clock.tick(60)
        pygame.display.flip()

tileeditor = TileEditor()

while tileeditor.running:
    tileeditor.update()