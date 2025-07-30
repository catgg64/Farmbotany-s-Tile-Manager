import pygame
import os
import time

tiles = {
    "1": [{"name": "Grass", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False}],
    "2": [{"name": "Hoed Ground", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 96, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False}],
    "3": [{"name": "Empty", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 16,"size_x": 16, "size_y": 16, "terrain": False}],
    "4": [{"name": "Crop", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 720, "rect_y": 32,"size_x": 16, "size_y": 16, "terrain": False}],
    "5": [{"name": "Dirt", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 64, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False}],
    "6": [{"name": "Top Left Corner Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False}],
    "7": [{"name": "Left Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False}],
    "8": [{"name": "Botton Left Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False}],
    "9": [{"name": "Top Corner Center Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False}],
    "10": [{"name": "Botton Center Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False}],
    "11": [{"name": "Top Right Corner Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False}],
    "12": [{"name": "Right Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False}],
    "13": [{"name": "Botton Right Grass Dirt In", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False}],
    "14": [{"name": "Top Left Corner Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False}],
    "15": [{"name": "Left Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False}],
    "16": [{"name": "Botton Left Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False}],
    "17": [{"name": "Top Corner Center Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 64, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False}],
    "18": [{"name": "Botton Center Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 64, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False}],
    "19": [{"name": "Top Right Corner Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 80, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False}],
    "20": [{"name": "Right Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 80, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False}],
    "21": [{"name": "Botton Right Grass Dirt Out", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 80, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False}],
    "22": [{"name": "Sand", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 80, "rect_y": 80, "size_x": 16, "size_y": 16, "terrain": False}],
    "23": [{"name": "Hoed Ground top: true, right: true, left: true, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 176, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "24": [{"name": "Hoed Ground top: true, right: true, left: true, bottom: false", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 176, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "25": [{"name": "Hoed Ground top: true, right: true, left: false, bottom: false", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 160, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "26": [{"name": "Hoed Ground top: true, right: true, left: false, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 160, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "27": [{"name": "Hoed Ground top: true, right: false, left: true, bottom: false", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 192, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "28": [{"name": "Hoed Ground top: true, right: false, left: true, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 192, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "29": [{"name": "Hoed Ground top: true, right: false, left: false, bottom: false", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 128, "rect_y": 64, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "30": [{"name": "Hoed Ground top: true, right: false, left: false, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 128, "rect_y": 48, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "31": [{"name": "Hoed Ground top: false, right: true, left: true, bottom: false", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 240, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "32": [{"name": "Hoed Ground top: false, right: true, left: true, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 176, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "33": [{"name": "Hoed Ground top: false, right: true, left: false, bottom: false", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 288, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "34": [{"name": "Hoed Ground top: false, right: true, left: false, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 160, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "35": [{"name": "Hoed Ground top: false, right: false, left: true, bottom: false", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 320, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "36": [{"name": "Hoed Ground top: false, right: false, left: true, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 192, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "37": [{"name": "Hoed Ground top: false, right: false, left: false, bottom: true", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 128, "rect_y": 32, "size_x": 16, "size_y": 16, "terrain": False, "child": "2"}],
    "38": [{"name": "Dirt Hill left top", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 192, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "39": [{"name": "Dirt Hill left center", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 208, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "40": [{"name": "Dirt Hill left bottom", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 224, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "41": [{"name": "Dirt Hill center top", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 192, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "42": [{"name": "Dirt Hill center center", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 208, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "43": [{"name": "Dirt Hill center bottom", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 224, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "44": [{"name": "Dirt Hill right top", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 192, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "45": [{"name": "Dirt Hill right center", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 208, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "46": [{"name": "Dirt Hill right bottom", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 224, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "47": [{"name": "Dirt Hill left single grass block", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 176, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "48": [{"name": "Dirt Hill center single grass block", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 176, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "49": [{"name": "Dirt Hill right single grass block", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 176, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "50": [{"name": "Dirt Hill left side", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 240, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "51": [{"name": "Dirt Hill right side", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 240, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "52": [{"name": "Dirt Hill bottom", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 304, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "53": [{"name": "Dirt Hill right side with top", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 256, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "54": [{"name": "Dirt Hill left side with top", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 256, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "55": [{"name": "Dirt Hill right side with center", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 272, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "56": [{"name": "Dirt Hill left side with center", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 272, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "57": [{"name": "Dirt Hill right side with bottom", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 288, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "58": [{"name": "Dirt Hill left side with bottom", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 288, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "59": [{"name": "Shop dirt 1x1", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 2880, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "60": [{"name": "Shop dirt 2x1", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 2896, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "61": [{"name": "Shop dirt 3x1", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 2912, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "62": [{"name": "Shop dirt 4x1", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 0, "rect_y": 2928, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "63": [{"name": "Shop dirt 1x2", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 2880, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "64": [{"name": "Shop dirt 2x2", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 2896, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "65": [{"name": "Shop dirt 3x2", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 2912, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "66": [{"name": "Shop dirt 4x2", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 16, "rect_y": 2928, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "67": [{"name": "Shop dirt 1x3", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 2880, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "68": [{"name": "Shop dirt 2x3", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 2896, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "69": [{"name": "Shop dirt 3x3", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 2912, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "70": [{"name": "Shop dirt 4x3", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 32, "rect_y": 2928, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "71": [{"name": "Shop dirt 1x4", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 2880, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "72": [{"name": "Shop dirt 2x4", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 2896, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "73": [{"name": "Shop dirt 3x4", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 2912, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
    "74": [{"name": "Shop dirt 4x4", "texture": "Sprites/tile_set.png", "requires_rect": True, "rect_x": 48, "rect_y": 2928, "size_x": 16, "size_y": 16, "terrain": False, "collision": True}],
}

def setup_surfaces(tile_exspansion):
    for tile_id, tile_data in tiles.items():
        for tile in tile_data:
            try:
                # Verify file exists
                if not os.path.exists(tile["texture"]):
                    raise FileNotFoundError(f"Sprite sheet {tile['texture']} not found")
                # Load image into a Surface

                surface = pygame.image.load(tile["texture"]).convert_alpha()

                if tile["requires_rect"]:
                    rect = pygame.Rect(tile["rect_x"], tile["rect_y"], tile["size_x"], tile["size_y"])
                    # Verify rect is valid
                    if not surface.get_rect().contains(rect):
                        raise ValueError(f"Rectangle {rect} is outside sprite sheet bounds {surface.get_rect()}")
                    tile["surface"] = surface.subsurface(rect)
                else:
                    tile["surface"] = surface
                del tile["texture"]  # Remove path to avoid misuse
                tile["surface"] = pygame.transform.scale(tile["surface"], (tile_exspansion, tile_exspansion))
            except (pygame.error, FileNotFoundError, ValueError) as e:
                print(f"Error loading texture for tile {tile_id}: {e}")
                tile["surface"] = pygame.Surface((16, 16))  # Fallback surface
                tile["surface"].fill((255, 0, 0))  # Red for debugging
                del tile["texture"]

class TileData:
    def __init__(self, sub_id, id):
        self.id = id
        self.sub_id = sub_id

class Tile:
    # At first initializes the tile.
    def __init__(self, pos_x, pos_y, id, sub_id, tile_size, slot_list):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = id
        self.sub_id = sub_id
        self.tile_size = tile_size
        self.rect = pygame.Rect(pos_x, pos_y, tile_size, tile_size)
        slot_list.append(self)

    # Then it updates (draws it every frame).
    def update(self, id, sub_id, screen, pos_x, pos_y):
        self.rect = pygame.Rect(pos_x, pos_y, self.tile_size, self.tile_size)
        self.id = id
        self.sub_id = sub_id
        if sub_id != "3":
            tile_data = tiles[sub_id][0]
            screen.blit(tile_data["surface"], (pos_x, pos_y))
        if id != "3":
            tile_data = tiles[id][0]
            screen.blit(tile_data["surface"], (pos_x, pos_y))
        
    # Pretty self-explanatory, right?
    def update_id_and_sub_id(self, id, sub_id):
        self.id = id
        self.sub_id = sub_id


    def is_colliding_with_point_if_so_give_the_id_and_sub_id(self, point):
        if self.rect.collidepoint(point):
            return [self.id, self.sub_id]
        else:
            return None

    def return_id_and_sub_id(self):
        return self.id, self.sub_id

    def is_colliding_with_point_if_so_return_pos(self, point):
        if self.rect.collidepoint(point):
            return self.pos_x, self.pos_y
        else:
            return False
    
    def is_colliding_with_point(self, point):
        if self.rect.collidepoint(point):
            return True
        else:
            return False
    
    def is_colliding_with_rect(self, rect):
        if self.rect.colliderect(rect):
            return True
        else:
            return False
    

class SpecialTile:
    def __init__(self, texture, size, pos_x, pos_y):
        self.texture = texture
        self.size = size
        self.image = pygame.image.load(self.texture)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = pygame.Rect(pos_x, pos_y, size, size)

    def update(self, screen, pos_x, pos_y):
        screen.blit(self.image, (pos_x, pos_y))
        
    def is_colliding_with_rect(self, rect):
        if self.rect.colliderect(rect):
            return True
        return False

class Crop(SpecialTile):
    def __init__(self, size, plant_time, pos_x, pos_y):
        self.texture = "Sprites/wheat_growing.png"
        self.image = pygame.image.load(self.texture)
        super().__init__(self.texture, size, pos_x, pos_y)
        self.start_time = time.time()
        self.plant_time = plant_time
        self.can_collect = False
        self.time_passed_since_beguining = 0
        self.time_passed_since_beguining = time.time() - self.start_time


    def update(self, screen, pos_x, pos_y):
        super().update(screen, pos_x, pos_y)
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
        self.time_passed_since_beguining = time.time() - self.start_time
        if self.time_passed_since_beguining >= self.plant_time:
            self.can_collect = True
            self.texture = "Sprites/wheat.png"
            self.image = pygame.image.load(self.texture)
            self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def check_for_harvest(self):
        if pygame.mouse.get_pressed()[0] and self.can_collect:
            return True
        return False



def setup_tile_data(width, length):
    return [TileData("1", "1") for _ in range(width * length)]  # Use valid ID "1"

def position_to_tile_value(x, y, width, length, tile_size, offset_x, offset_y):
    calc_x = (x - offset_x) // tile_size
    calc_y = (y - offset_y) // tile_size
    return calc_x, calc_y
    

def tile_value_to_position(x, y, width, tile_size):
    pos_x = x * tile_size
    pos_y = y * tile_size
    return pos_x, pos_y

def create_rects(tile_list, rect_list, width):
    for index, tile in enumerate(tile_list):
        tile_data = tiles[tile.id][0]
        if tile_data["has_collision"]:
            pass

def draw_tilemap(tile_list, width, screen, tile_size, offset_x, offset_y):
    drawn_tiles = 0
    for index, tile in enumerate(tile_list):
        if tile.id not in tiles:
            print(f"Warning: Tile ID {tile.id} not found at index {index}")
            continue
        tile_data = tiles[tile.id][0]
        sub_id_tile_data = tiles[tile.sub_id][0]
        pos = tile_value_to_position(index, width, tile_size)
        screen.blit(sub_id_tile_data["surface"], (offset_x + pos[0], offset_y + pos[1]))
        screen.blit(tile_data["surface"], (offset_x + pos[0], offset_y + pos[1]))

        drawn_tiles += 1

# Instantiates all the slots.
def initialize_tilemap(tile_list, sub_tile_list, width, tile_size, offset_x, offset_y, tile_slot_list):
    for row_idx in range(len(tile_list)):
        for col_idx in range(len(tile_list[row_idx])):
            tile_data = TileData(sub_tile_list[row_idx][col_idx], tile_list[row_idx][col_idx])
            pos = tile_value_to_position(col_idx, row_idx, width, tile_size)
            Tile(offset_x + pos[0], offset_y + pos[1], tile_data.id, tile_data.sub_id, tile_size, tile_slot_list)
        
    
    # for index, tile in enumerate(tile_list):
    #     tile_data = tiles[tile.id][0]
    #     pos = tile_value_to_position(x, y, width, tile_size)
    #     Tile(offset_x + pos[0], offset_y + pos[1], tile.id, tile.sub_id, tile_size, tile_slot_list)


# Updates all the slots.
def update_tile_map(tile_list, sub_tile_list, tile_slot_list, width, tile_size, offset_x, offset_y, internal_surface, draw_queue):   
    for row_idx in range(len(tile_list)):
        for col_idx in range(len(tile_list[row_idx])):
            if tile_slot_list[row_idx * width + col_idx] in draw_queue:
                tile_data = TileData(sub_tile_list[row_idx][col_idx], tile_list[row_idx][col_idx])
                pos = tile_value_to_position(col_idx, row_idx, width, tile_size)
                tile_slot_list[row_idx * width + col_idx].update(tile_data.id, tile_data.sub_id, internal_surface, offset_x + pos[0], offset_y + pos[1])


    # for index, tile in enumerate(tile_list):
    #     tile_data = tiles[tile.id][0]
    #     pos = tile_value_to_position(index, width, tile_size)
    #     tile_slot_list[index].update(tile.id, tile.sub_id, internal_surface, offset_x + pos[0], offset_y + pos[1])

def update_special_tiles(special_tiles_list, width, tile_size, offset_x, offset_y, internal_surface, draw_queue):
    for row_idx, row in enumerate(special_tiles_list):
        for column_idx, column in enumerate(row):
            if column is not None:
                if column in draw_queue:
                    pos = tile_value_to_position(row_idx, column_idx, width, tile_size)
                    column.update(internal_surface, offset_x + pos[0], offset_y + pos[1])

    
    # for index, tile in enumerate(special_tiles_list):
    #     if tile is not None:
    #         pos = tile_value_to_position(index, width, tile_size)
    #         tile.update(internal_surface, offset_x + pos[0], offset_y + pos[1])



def check_collision_in_all_tiles(point, tile_slot_list):
    for tile in tile_slot_list:
        if tile.is_colliding_with_point_if_so_give_the_id_and_sub_id(point):
            return tile.is_colliding_with_point_if_so_give_the_id_and_sub_id(point)
    return None

def check_for_harvest_in_all_crops(special_items_list, point):
    for index, tile in enumerate(special_items_list):
        if isinstance(tile, Crop):
            return tile.check_for_harvest(point)
    return None

def get_neighbors(tile_value, width, tile_map):
    neighbors = [None, None, None, None, None, None, None, None]
    neighbors[0] = tile_map[tile_value - width - 1]
    neighbors[1] = tile_map[tile_value - width]
    neighbors[2] = tile_map[tile_value - width + 1]
    neighbors[3] = tile_map[tile_value - 1]
    neighbors[4] = tile_map[tile_value + 1]
    neighbors[5] = tile_map[tile_value + width - 1]
    neighbors[6] = tile_map[tile_value + width]
    neighbors[7] = tile_map[tile_value + width + 1]
    return neighbors


