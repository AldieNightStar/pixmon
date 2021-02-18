import pygame

from pix.defs import MouseInfo, SpriteSheet

DEF_COLOR = 'white'


def inner_main(screen_width, screen_height, hnd_load, hnd_input, hnd_update):
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pix_class = Pix(screen)
    hnd_load(pix_class)
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            else:
                hnd_input(event)
            if not (pix_class.mouseInfo is None):
                if event.type == pygame.MOUSEMOTION:
                    pix_class.mouseInfo.x, pix_class.mouseInfo.y = event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pix_class.mouseInfo.left = event.button == pygame.BUTTON_LEFT
                    pix_class.mouseInfo.right = event.button == pygame.BUTTON_RIGHT
                    pix_class.mouseInfo.middle = event.button == pygame.BUTTON_MIDDLE
                elif event.type == pygame.MOUSEBUTTONUP:
                    pix_class.mouseInfo.left = not event.button == pygame.BUTTON_LEFT
                    pix_class.mouseInfo.right = not event.button == pygame.BUTTON_RIGHT
                    pix_class.mouseInfo.middle = not event.button == pygame.BUTTON_MIDDLE
        pygame.display.update()
        screen.fill("black")
        hnd_update(pix_class)


class Pix:
    _screen: pygame.Surface = None
    _images = {}
    _spritesheets = {}
    mouseInfo = None

    def __init__(self, screen):
        self._screen = screen

    def rect(self, x, y, w, h, c=DEF_COLOR):
        pygame.draw.rect(self._screen, c, (x, y, w, h))

    def loadspr(self, id, path: str):
        img = pygame.image.load(path).convert_alpha()
        self._images[id] = img

    def loadsprsheet(self, id, path: str, cols, rows):
        img = pygame.image.load(path).convert_alpha()
        self._spritesheets[id] = SpriteSheet(img, cols, rows)

    def spr(self, id, x, y, w=0, h=0):
        if not (id in self._images):
            pass
        if w == 0 and h == 0:
            self._screen.blit(self._images[id], (x, y))
        else:
            self._screen.blit(pygame.transform.scale(self._images[id], (w, h)), (x, y))

    def sprc(self, sprsheetId, cellId, x, y, w=0, h=0):
        if not (sprsheetId in self._spritesheets):
            pass
        img = self._spritesheets[sprsheetId].get_sprite(cellId)
        if w == 0 and h == 0:
            self._screen.blit(img, (x, y))
        else:
            self._screen.blit(pygame.transform.scale(img, (w, h)), (x, y))

    def mouse(self) -> MouseInfo:
        if self.mouseInfo is None:
            self.mouseInfo = MouseInfo()
        return self.mouseInfo
