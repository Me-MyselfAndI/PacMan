import play
from creature import Creature

scale = 5
screen_unit = 28.542


class Pacman(Creature):
    def __init__(self, image_name, position, game_map, size):
        super().__init__(image_name, position, game_map, size)
        self.map_width = game_map.full_image.width
        self.map_height = game_map.full_image.height

        self.lives = 3
        self.angry = False

        self.last_direction = 'r'

    def move_up(self):
        # Go up and make last_direction equal 'u', if (not touching any of the map walls) or (last_direction is 'd')
        super().move(0, screen_unit / scale)
        self.image.angle = 90
        self.last_direction = 'u'

    def move_down(self):
        touching_wall = False
        if touching_wall == False or self.last_direction == 'u':
            super().move(0, -screen_unit / scale)
            self.image.angle = 270
            self.last_direction = 'd'

    def move_right(self):
        touching_wall = False
        if touching_wall == False or self.last_direction == 'l':
            max_y = 50
            min_y = -20
            if self.position[0] >= -250 + 19 * screen_unit and min_y < self.position[1] < max_y:
                super().move(-20 * screen_unit, 0)
            super().move(screen_unit / scale, 0)
            self.image.angle = 0
            self.last_direction = 'r'

    def move_left(self):
        touching_wall = False
        if touching_wall == False or self.last_direction == 'r':
            max_y = 50
            min_y = -20
            if self.position[0] <= -270 and min_y < self.position[1] < max_y:
                super().move(20 * screen_unit, 0)
            super().move(-screen_unit / scale, 0)
            self.image.angle = 180
            self.last_direction = 'l'

    def is_touching_dots(self):
        for dot in self.game_map.dots:
            if self.image.is_touching(dot.image):
                self.game_map.dots.remove(dot)
                dot.image.remove()
