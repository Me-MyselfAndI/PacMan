import play
import random
import math
from creature import Creature
import time

scale = 5
screen_unit = 28.542


def dist_between(x1, y1, x2, y2):
    # Find distance by x
    x_dist = abs(x1 - x2)
    # Find distance by y
    y_dist = abs(y1 - y2)
    # Find & return overall distance
    dist = math.sqrt(y_dist ** 2 + x_dist ** 2)

    return dist


class Ghost(Creature):
    def __init__(self, image_name, position, game_map, size):
        super().__init__(image_name, position, game_map, size)
        self.home_position = [0, 0]
        self.map_width = game_map.full_image.width
        self.map_height = game_map.full_image.height

        self.last_direction = 'initial'

    def respawn(self):
        # Here we delete the ghost
        # ____
        #

        time.sleep(10)
        self.position = self.home_position

    # TARGET HAS TO BE A SPRITE
    def move(self, target, in_house=False):
        if in_house == False:

            needs_to_move_up = self.last_direction == 'up' and (not self.close_blocked_up() and self.far_blocked_right() and self.far_blocked_left())
            needs_to_move_down = self.last_direction == 'down' and (not self.close_blocked_down() and self.far_blocked_right() and self.far_blocked_left())
            needs_to_move_right = self.last_direction == 'right' and (not self.close_blocked_right() and self.far_blocked_up() and self.far_blocked_down())
            needs_to_move_left = self.last_direction == 'left' and (not self.close_blocked_left() and self.far_blocked_up() and self.far_blocked_down())

            if needs_to_move_up:
                super().move(0, screen_unit / scale)
                return

            if needs_to_move_down:
                super().move(0, -screen_unit / scale)
                return

            if needs_to_move_right:
                super().move(screen_unit / scale, 0)
                return

            if needs_to_move_left:
                super().move(-screen_unit / scale, 0)
                return

                # Make a list of distances if we go up, right, down, left
            directions = []
            # Find the dist if we go up and append it
            directions.append((0, screen_unit / scale, dist_between(self.up.x, self.up.y, target.x, target.y), 'up'))
            # Find the dist if we go right and append it
            directions.append(
                (screen_unit / scale, 0, dist_between(self.right.x, self.right.y, target.x, target.y), 'right'))
            # Find the dist if we go down and append it
            directions.append(
                (0, -screen_unit / scale, dist_between(self.down.x, self.down.y, target.x, target.y), 'down'))
            # Find the dist if we go left and append it
            directions.append(
                (-screen_unit / scale, 0, dist_between(self.left.x, self.left.y, target.x, target.y), 'left'))

            directions = self.sort_directions(directions)

            for direction in directions:
                if super().move(direction[0], direction[1]):
                    self.last_direction = direction[3]
                    break


        else:
            dx = 0
            dy = screen_unit / scale
            self.position = [self.position[0] + dx, self.position[1] + dy]

            self.image.x = self.position[0]
            # move little sprites by dx
            self.up.x = self.position[0]
            self.down.x = self.position[0]
            self.right.x = self.position[0] + dx
            self.left.x = self.position[0] - dx

            self.image.y = self.position[1]
            # move little sprites by dy
            self.up.y = self.position[1] + dy
            self.down.y = self.position[1] - dy
            self.right.y = self.position[1]
            self.left.y = self.position[1]

    def sort_directions(self, directions):
        ordered = False
        # Do until everything is ordered:
        while not ordered:
            # Go over all elements and every time we need to look at the pairs of current and next.
            for i in range(len(directions) - 1):
                # If they are in the wrong order (i.e., next is smaller than current)
                if directions[i][2] > directions[i + 1][2]:
                    # Then swap them
                    temporary = directions[i]
                    directions[i] = directions[i + 1]
                    directions[i + 1] = temporary

            # Assume elements are ordered
            ordered = True
            # Run through all elements and check each pair of curr and next elements. If they are unordered,
            # record that they are unordered
            for i in range(len(directions) - 1):
                if directions[i][2] > directions[i + 1][2]:
                    ordered = False
                    break

        return directions
