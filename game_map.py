import play, time


class Game_map:

    def __init__(self, image_name, walls, dots, fruit):
        self.score = 0
        self.fruit = fruit
        self.full_image = play.new_image(image=image_name, x=0, y=0, size=50)
        self.full_image.transparency = 0
        self.walls = walls
        self.dots = dots

    def delete_field(self, pacman, ghosts):
        for i in range(len(self.dots)-1, -1, -1):
            self.dots[i].image.remove()
            del self.dots[i]
        for i in range(len(self.fruit)-1, -1, -1):
            self.fruit[i].image.remove()
            del self.fruit[i]
        for i in range(len(self.walls)-1, -1, -1):
            self.walls[i].remove()
            del self.walls[i]
        for i in range(len(ghosts)-1, -1, -1):
            ghosts[i].remove()
            del ghosts[i]
        pacman.remove()
        time.sleep(6)
        quit()



    def game_won(self, pacman, ghosts):
        you_won = play.new_image(image='images/Text/YouWon.png', x=0, y=0, size=100)
        you_won.move(1)
        self.delete_field(pacman, ghosts)
        print("You Won")

    def game_over(self, pacman, ghosts):
        game_over = play.new_image(image='images/Text/GameOver.png', x=0, y=0, size=100)
        game_over.move(1)
        self.delete_field(pacman, ghosts)
        print("Game Over")

