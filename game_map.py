import play, time


class Game_map:

    def __init__(self, image_name, walls, dots, fruit):
        self.score = 0
        self.fruit = fruit
        self.full_image = play.new_image(image=image_name, x=0, y=0, size=50)
        self.full_image.transparency = 0
        self.walls = walls
        self.dots = dots
        self.you_won_sprite = play.new_image(image='images/text/YouWon.png', x=0, y=0, size=100)
        self.you_won_sprite.hide()
        self.game_over_sprite = play.new_image(image='images/text/GameOver.png', x=0, y=0, size=100)
        self.game_over_sprite.hide()


    def delete_field(self, pacman, ghosts):
        time.sleep(2)
        for i in range(len(self.dots)-1, -1, -1):
            self.dots[i].image.hide()
            del self.dots[i]
        for i in range(len(self.fruit)-1, -1, -1):
            self.fruit[i].image.hide()
            del self.fruit[i]
        for i in range(len(self.walls)-1, -1, -1):
            self.walls[i].hide()
            del self.walls[i]
        for i in range(len(ghosts)-1, -1, -1):
            ghosts[i].remove()
            del ghosts[i]
        pacman.remove()
        time.sleep(6)
        quit()



    def game_won(self, pacman, ghosts):
        self.you_won_sprite.show()
        time.sleep(1)
        self.delete_field(pacman, ghosts)
        print("You Won")

    def game_over(self, pacman, ghosts):
        self.game_over_sprite.show()
        time.sleep(1)
        self.delete_field(pacman, ghosts)
        print("Game Over")

