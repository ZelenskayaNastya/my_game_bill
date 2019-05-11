from livewires import games

games.init(screen_width=500, screen_height=800, fps=50)


class Cue(games.Sprite):

    image = games.load_image('img/cue.PNG')

    def __init__(self):
        super(Cue, self).__init__(image=Cue.image,
                                  x=games.mouse.x,
                                  y=games.mouse.y)

    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
