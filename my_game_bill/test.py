import play
from play import screen_my

billiard = play.Balls((0, 0), (0.1, 0.2), "")
print(billiard)

play.poster(billiard, screen_my)
