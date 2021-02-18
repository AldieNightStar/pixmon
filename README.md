# PixMon
### Small `pygame` based lib

---

## Get started
* Template already has everything to start
* Just open `game.py` and you are ready to go :)
* Edit `GAME_WIDTH` and `GAME_HEIGHT` settings to change window size

## Rules - to not break
* Do not touch `pix` folder. It is engine
* Do not touch `__name__ == '__main__`. It would not work if you will :)
* Load game resources in `load` function
* Use input events in `_input` function
* Do not change arguments in `update`, `load` and `_input` functions. They are very important
* Use motsly `pix` class as much as you can, only then `pygame`

## Functions
```py
pix.loadspr(1, "./ball.png")                    # Load sprite as ID=1
pix.spr(1, x, y)                                # Display sprite with ID=1
pix.spr(1, x, y, w, h)                          # Display scaled sprite with ID=1

pix.mouse()                                     # Get mouse details

pix.loadsprsheet(1, "./tiles.png", cols, rows)  # Load a sprite sheet file as ID=1
pix.sprc(1, tileId, x, y)                       # Display tile from sprite sheet ID=1
pix.sprc(1, tileId, x, y, w, h)                 # Display scaled tile from sprite sheet ID=1

pix.rect(x, y, w, h, color)                     # Display rectangle (default color is white)
```

## Still in development