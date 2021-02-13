import time

import play
from pacman import Pacman
from game_map import Game_map
from item import Item
from ghost import Ghost

ghosts = []
dots = []
fruit = []

map_sprites = []
play.set_backdrop((0, 0, 0))
# complete_map = play.new_image(image="images/map/Map.png", x=0, y=0, size=50)
map_sprites.append(play.new_image(image="images/map/Map2.jpg", x=-118, y=231, size=32))
map_sprites.append(play.new_image(image="images/map/Map1.jpg", x=-220, y=231, size=32))
map_sprites.append(play.new_image(image="images/map/Map2.jpg", x=118, y=231, size=32))
map_sprites.append(play.new_image(image="images/map/Map1.jpg", x=220, y=231, size=32))
map_sprites.append(play.new_image(image="images/map/Map3.jpg", x=-220, y=168, size=32))
map_sprites.append(play.new_image(image="images/map/Map3.jpg", x=220, y=168, size=32))
map_sprites.append(play.new_image(image="images/map/Map5.jpg", x=-283, y=210, size=34))
map_sprites.append(play.new_image(image="images/map/Map5.jpg", x=-283, y=190, size=34))
map_sprites.append(play.new_image(image="images/map/Map4.jpg", x=-242, y=90, size=34))
map_sprites.append(play.new_image(image="images/map/Map6.jpg", x=-1, y=285, size=36))
map_sprites.append(play.new_image(image="images/map/Map7.jpg", x=-1, y=247, size=32))
map_sprites.append(play.new_image(image="images/map/Map5.jpg", x=284, y=210, size=34))
map_sprites.append(play.new_image(image="images/map/Map5.jpg", x=284, y=190, size=34))
map_sprites.append(play.new_image(image="images/map/Map8.jpg", x=241, y=90, size=34))
map_sprites.append(play.new_image(image="images/map/Map9.jpg", x=-245, y=-49, size=32))
map_sprites.append(play.new_image(image="images/map/Map25.jpg", x=245, y=-51, size=32))
map_sprites.append(play.new_image(image="images/map/Map11.jpg", x=0, y=-285, size=36))
map_sprites.append(play.new_image(image="images/map/Map10.jpg", x=-284, y=-182, size=36))
map_sprites.append(play.new_image(image="images/map/Map12.jpg", x=284, y=-182, size=36))
map_sprites.append(play.new_image(image="images/map/Map13.jpg", x=-264, y=-187, size=32))
map_sprites.append(play.new_image(image="images/map/Map14.jpg", x=264, y=-184, size=32))
map_sprites.append(play.new_image(image="images/map/Map15.jpg", x=-128, y=-51, size=32))
map_sprites.append(play.new_image(image="images/map/Map15.jpg", x=128, y=-51, size=32))
map_sprites.append(play.new_image(image="images/map/Map16.jpg", x=0, y=170, size=32))
map_sprites.append(play.new_image(image="images/map/Map16.jpg", x=0, y=-182, size=32))
map_sprites.append(play.new_image(image="images/map/Map16.jpg", x=0, y=-68, size=32))
map_sprites.append(play.new_image(image="images/map/Map17.jpg", x=0, y=128, size=32))
map_sprites.append(play.new_image(image="images/map/Map17.jpg", x=0, y=-226, size=32))
map_sprites.append(play.new_image(image="images/map/Map17.jpg", x=0, y=-112, size=32))
map_sprites.append(play.new_image(image="images/map/Map18.jpg", x=-128, y=110, size=32))
map_sprites.append(play.new_image(image="images/map/Map19.jpg", x=-84, y=111, size=32))
map_sprites.append(play.new_image(image="images/map/Map21.jpg", x=128, y=111, size=32))
map_sprites.append(play.new_image(image="images/map/Map20.jpg", x=84, y=110, size=32))
map_sprites.append(play.new_image(image="images/map/Map22.jpg", x=0, y=20, size=16))
map_sprites.append(play.new_image(image="images/map/Map23.jpg", x=-150, y=-249, size=32))
map_sprites.append(play.new_image(image="images/map/Map24.jpg", x=-127, y=-203, size=32))
map_sprites.append(play.new_image(image="images/map/Map26.jpg", x=150, y=-249, size=32))
map_sprites.append(play.new_image(image="images/map/Map24.jpg", x=127, y=-203, size=32))
map_sprites.append(play.new_image(image="images/map/Map27.jpg", x=-209, y=-135, size=32))
map_sprites.append(play.new_image(image="images/map/Map28.jpg", x=-194, y=-172, size=32))
map_sprites.append(play.new_image(image="images/map/Map28.jpg", x=194, y=-172, size=32))
map_sprites.append(play.new_image(image="images/map/Map29.jpg", x=209, y=-135, size=32))
map_sprites.append(play.new_image(image="images/map/Map3.jpg", x=-118, y=-134, size=32))
map_sprites.append(play.new_image(image="images/map/Map3.jpg", x=118, y=-134, size=32))

game_map = Game_map("images/map/Map.png", map_sprites, dots, fruit)

for x in range(0, 19):
    for y in range(0, 19):
        dots.append(Item("images/Dot.png", [-257 + x * 28.542, -257 + y * 28.542], "dot"))

for i in range (len(dots)-1, -1, -1):
    for j in range (len(game_map.walls)):
        if dots[i].image.is_touching(game_map.walls[j]):
            dots[i].image.remove()
            dots.remove(dots[i])

fruit.append(Item("images/Fruit.png", [-257 + 0 * 28.542, -257 + 29 * 28.542], "fruit"))
fruit.append(Item("images/Fruit.png", [-257 + 29 * 28.542, -257 + 29 * 28.542], "fruit"))
fruit.append(Item("images/Fruit.png", [-257 + 29 * 28.542, -257 + 0 * 28.542], "fruit"))
fruit.append(Item("images/Fruit.png", [-257 + 0 * 28.542, -257 + 0 * 28.542], "fruit"))

ghost_sprites = [
    play.new_box(color="red", width=7, height=7, x=-257, y=-273, transparency=1),
    play.new_box(color="pink", width=7, height=7, x=-257, y=273, transparency=1),
    play.new_box(color="cyan", width=7, height=7, x=252, y=-273, transparency=1),
    play.new_box(color="orange", width=7, height=7, x=252, y=273, transparency=1)
]

pacman = Pacman("images/pacman.png", [-257 + 0 * 28.542, -257 + 0 * 28.542], game_map, 5)
ghosts = [
    Ghost("images/ghosts/Blinky.png", [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542], game_map, 30),
    Ghost("images/ghosts/Pinky.png", [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542], game_map, 30),
    Ghost("images/ghosts/Inky.png", [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542], game_map, 30),
    Ghost("images/ghosts/Clyde.png", [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542], game_map, 30)
]

targets = []
for i in range(len(ghosts)):
    targets.append(pacman.image)

game_continues = True

@play.when_key_pressed('up', 'w')
async def move_up(key):
    global game_continues
    if (game_continues):
        pacman.move_up()
        pacman.is_touching_dots()
        await play.timer(seconds=0.001)


@play.when_key_pressed('down', 's')
async def move_down(key):
    global game_continues
    if (game_continues):
        pacman.move_down()
        pacman.is_touching_dots()
        await play.timer(seconds=0.001)


@play.when_key_pressed('right', 'd')
async def move_right(key):
    global game_continues
    if (game_continues):
        pacman.move_right()
        pacman.is_touching_dots()
        await play.timer(seconds=0.001)


@play.when_key_pressed('left', 'a')
async def move_left(key):
    global game_continues
    if (game_continues):
        pacman.move_left()
        pacman.is_touching_dots()
        await play.timer(seconds=0.001)



@play.repeat_forever
async def move_blinky():
    global game_continues
    if (game_continues):
        try:
            if ghosts[0].position == [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542]:
                ghosts[0].move(None, True)
            ghosts[0].move(targets[0])
            await play.timer(seconds=0.001)
            if ghosts[0].image.is_touching(pacman.image):
                game_continues = False
                game_map.game_over(pacman, ghosts)
        except ValueError:
            time.sleep(10)
        except IndexError:
            time.sleep(10)


@play.repeat_forever
async def move_pinky():
    global game_continues
    if (game_continues):
        try:
            if ghosts[1].position == [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542]:
                ghosts[1].move(None, True)
            ghosts[1].move(targets[1])
            await play.timer(seconds=0.001)
            if ghosts[1].image.is_touching(pacman.image):
                game_continues = False
                game_map.game_over(pacman, ghosts)
        except ValueError:
            time.sleep(10)
        except IndexError:
            time.sleep(10)


@play.repeat_forever
async def move_inky():
    global game_continues
    if (game_continues):
        try:
            if ghosts[2].position == [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542]:
                ghosts[2].move(None, True)
            ghosts[2].move(targets[2])
            await play.timer(seconds=0.001)
            if ghosts[2].image.is_touching(pacman.image):
                game_continues = False
                game_map.game_over(pacman, ghosts)
        except ValueError:
            time.sleep(10)
        except IndexError:
            time.sleep(10)


@play.repeat_forever
async def move_clyde():
    global game_continues
    if (game_continues):
        try:
            if ghosts[3].position == [-257 + 19/2 * 28.542, -257 + 19/2 * 28.542]:
                ghosts[3].move(None, True)
            ghosts[3].move(targets[3])
            await play.timer(seconds=0.001)
            if ghosts[3].image.is_touching(pacman.image):
                game_continues = False
                game_map.game_over(pacman, ghosts)
        except ValueError:
            time.sleep(10)
        except IndexError:
            time.sleep(10)


@play.when_program_starts
async def change_goals():
    global game_continues
    if (game_continues):
        for tact in range (10):
            for i in range (len (ghosts)):
                ghosts[i].move(None, True)

    tact = 0
    while True:
        if not game_continues:
            for i in range(len(ghosts)):
                ghosts[i] = Ghost(None, 0, 0, game_map, size=0)
                break
        if len(dots) == 0:
            game_map.game_won(pacman, ghosts)
        if tact % 200 == 0:
            targets[0] = ghost_sprites[0]
        elif tact % 100 == 0:
            targets[0] = pacman.image

        if tact % 300 == 0:
          targets[1] = ghost_sprites[1]
          targets[2] = ghost_sprites[2]
        elif tact % 200 == 0:
            targets[1] = pacman.image
        elif tact % 100 == 0:
            targets[2] = pacman.image

        if tact % 400 == 0:
            targets[3] = ghost_sprites[3]
        elif tact % 100 == 0:
            targets[3] = pacman.image

        await play.timer(seconds=0.001)
        tact += 1


play.start_program()
