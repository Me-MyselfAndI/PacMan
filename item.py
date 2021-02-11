import play


class Item:

    # str               image
    # list[int, int]    position
    # int               cat  (category)

    def __init__(self, image_name, position, cat):
        self.position = position
        self.cat = cat
        self.image = play.new_image(image=image_name, x=position[0], y=position[1], size=0.7)
