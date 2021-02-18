import pygame
import pix

GAME_WIDTH = 640
GAME_HEIGHT = 480


def update(pix: pix.Pix):
    pass


def load(pix: pix.Pix):
    pass


def _input(event: pygame.event.Event):
    pass


if __name__ == '__main__':
    pix.inner_main(GAME_WIDTH, GAME_HEIGHT, load, _input, update)
