import play

dist_const = 4
far_dist_const = 15
close_length_const = 0.7
far_length_const = 1.3


class Creature:
    def __init__(self, image_name, position, game_map, size):
        self.image_name = image_name
        self.position = position
        self.game_map = game_map
        self.image = play.new_image(image=image_name, x=position[0], y=position[1], size=size)

        self.up = play.new_box(color="red", x=position[0], y=position[1] + self.image.height/2 + dist_const, width=self.image.width * close_length_const, height=1)
        self.right = play.new_box(color="red", x=position[0] + self.image.width/2 + dist_const, y=position[1], width=1, height=self.image.height * close_length_const)
        self.left = play.new_box(color="red", x=position[0] - self.image.width/2 - dist_const, y=position[1], width=1, height=self.image.height * close_length_const)
        self.down = play.new_box(color="red", x=position[0], y=position[1] - self.image.height/2 - dist_const, width=self.image.width * close_length_const, height=1)

        #self.up.hide()
        #self.right.hide()
        #self.left.hide()
        #self.down.hide()

        self.far_up = play.new_box(color="green", x=position[0], y=position[1] + self.image.height / 2 + far_dist_const,
                               width=self.image.width*far_length_const, height=1)
        self.far_right = play.new_box(color="green", x=position[0] + self.image.width / 2 + far_dist_const, y=position[1], width=1,
                                  height=self.image.height*far_length_const)
        self.far_left = play.new_box(color="green", x=position[0] - self.image.width / 2 - far_dist_const, y=position[1], width=1,
                                 height=self.image.height*far_length_const)
        self.far_down = play.new_box(color="green", x=position[0], y=position[1] - self.image.height / 2 - far_dist_const,
                                 width=self.image.width*far_length_const, height=1)

        #self.far_up.hide()
        #self.far_right.hide()
        #self.far_left.hide()
        #self.far_down.hide()

    def remove(self):
        self.image.go_to(x=0, y=0)
        self.image.remove()
        self.right.remove()
        self.far_right.remove()
        self.left.remove()
        self.far_left.remove()
        self.up.remove()
        self.far_up.remove()
        self.down.remove()
        self.far_down.remove()

    def check_move(self, dx, dy):
        # If dx  > 0
        if dx > 0:
            # Use is_touching to detect if the right sprite is touching one of the walls
            if self.close_blocked_right():
                return False
        # Otherwise, only if dx is < 0, then
        elif dx < 0:
            # Use is_touching to detect if the left sprite is touching one of the walls
            if self.close_blocked_left():
                return False
        # If dy > 0
        if dy > 0:
            # Use is_touching to detect if the top sprite is touching one of the walls
            if self.close_blocked_up():
                return False
        # If dy < 0
        elif dy < 0:
            # Use is_touching to detect if the bottom sprite is touching one of the walls
            if self.close_blocked_down():
                return False
        # return True

    def close_blocked_right(self):
        for wall in self.game_map.walls:
            if self.right.is_touching(wall):
                # If so, return false
                return True
        return False

    def close_blocked_up(self):
        for wall in self.game_map.walls:
            if self.up.is_touching(wall):
                # If so, return false
                return True
        return False

    def close_blocked_left(self):
        for wall in self.game_map.walls:
            if self.left.is_touching(wall):
                # If so, return false
                return True
        return False

    def close_blocked_down(self):
        for wall in self.game_map.walls:
            if self.down.is_touching(wall):
                # If so, return false
                return True
        return False

    def far_blocked_right(self):
        for wall in self.game_map.walls:
            if self.far_right.is_touching(wall):
                # If so, return false
                return True
        return False

    def far_blocked_up(self):
        for wall in self.game_map.walls:
            if self.far_up.is_touching(wall):
                # If so, return false
                return True
        return False

    def far_blocked_left(self):
        for wall in self.game_map.walls:
            if self.far_left.is_touching(wall):
                # If so, return false
                return True
        return False

    def far_blocked_down(self):
        for wall in self.game_map.walls:
            if self.far_down.is_touching(wall):
                # If so, return false
                return True
        return False

    def move(self, dx, dy):
        # check_move (dx, dy): if we got True, we continue, but if False, we just don't do anything
        # If we got FALSE from check_move ()
        if self.check_move(dx, dy) == False:
            # stop the function
            return False

        self.position = [self.position[0] + dx, self.position[1] + dy]

        self.image.x = self.position[0]
        # move little sprites by dx
        self.up.x = self.position[0]
        self.down.x = self.position[0]
        self.right.x = self.position[0] + self.image.width/2 + dist_const
        self.left.x = self.position[0] - self.image.width/2 - dist_const

        self.image.y = self.position[1]
        # move little sprites by dy
        self.up.y = self.position[1] + self.image.height/2 + dist_const
        self.down.y = self.position[1] - self.image.height/2 - dist_const
        self.right.y = self.position[1]
        self.left.y = self.position[1]

        self.image.x = self.position[0]
        # move little sprites by dx
        self.far_up.x = self.position[0]
        self.far_down.x = self.position[0]
        self.far_right.x = self.position[0] + self.image.width/2 + far_dist_const
        self.far_left.x = self.position[0] - self.image.width/2 - far_dist_const

        self.image.y = self.position[1]
        # move little sprites by dy
        self.far_up.y = self.position[1] + self.image.height/2 + far_dist_const
        self.far_down.y = self.position[1] - self.image.height/2 - far_dist_const
        self.far_right.y = self.position[1]
        self.far_left.y = self.position[1]

        return True
