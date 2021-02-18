import pygame

class MouseInfo:
    x = 0
    y = 0
    left = False
    right = False
    middle = False


class SpriteSheet:
    cols = 0
    rows = 0
    img: pygame.Surface = None
    cells = []
    imgSize: pygame.Rect = None
    cellSize: pygame.Rect = None
    cellCount = 0

    def __init__(self, img: pygame.Surface, cols, rows):
        self.img = img
        self.cols = cols
        self.rows = rows
        self.imgSize = img.get_rect().size
        self.cellSize = pygame.Rect(0, 0, self.imgSize[0] / self.cols, self.imgSize[1] / self.rows)
        self.__calculate()
        self.cellCount = len(self.cells)

    def __calculate(self):
        for y in range(self.rows):
            for x in range(self.cols):
                self.cells.append(self.img.subsurface(pygame.Rect(
                    x * self.cellSize.width, y * self.cellSize.height, self.cellSize.width, self.cellSize.height
                )))

    def get_sprite(self, cellId):
        if cellId > self.cellCount or cellId < 0:
            return None
        return self.cells[cellId]
