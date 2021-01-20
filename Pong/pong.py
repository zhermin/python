import turtle, random, time

class Window:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.title("PONG")
        self.win.bgcolor("black")

        self.screen_width = 1200 # x
        self.screen_height = 600 # y
        self.win.setup(width=self.screen_width, height=self.screen_height)

        self.win.tracer(0)
        self.win.listen()

class DrawShape(Window):
    def __init__(self):
        super().__init__()
        self.drawn = turtle.Turtle()
        self.drawn.shape("square") #20 by 20
        self.drawn.color("white")
        self.drawn.speed(0) #sets animation speed to max
        self.drawn.penup() #not to draw using Turtle

class Paddle(DrawShape):
    def __init__(self, get_player):
        super().__init__()
        self.drawn.shapesize(stretch_wid=5, stretch_len=1) #20x5 by 20x1
        self.get_player = get_player
        self.drawn.goto(self.get_player * (self.screen_width // 2 - 50),0)
        self.score = 0

    def paddle_up(self):
        self.y = self.drawn.ycor()
        if self.y + 50 <= self.screen_height // 2:
            self.y += 20
            self.drawn.sety(self.y)

    def paddle_down(self):
        self.y = self.drawn.ycor()
        if self.y - 50 >= -self.screen_height // 2:
            self.y -= 20
            self.drawn.sety(self.y)

class Paddle_A(Paddle):
    def __init__(self, get_player):
        super().__init__(get_player)

        self.win.onkeypress(self.paddle_up, "w")
        self.win.onkeypress(self.paddle_down, "s")

    def collisions(self, object):
        paddle_dist = self.get_player * (self.screen_width // 2 - 60)
        if (object.drawn.xcor() <= paddle_dist and object.drawn.xcor() > paddle_dist-5) and (object.drawn.ycor() < self.drawn.ycor() + 60 and object.drawn.ycor() > self.drawn.ycor() - 60):
            object.drawn.setx(paddle_dist)
            object.dx *= -1

class Paddle_B(Paddle):
    def __init__(self, get_player):
        super().__init__(get_player)

        self.win.onkeypress(self.paddle_up, "Up")
        self.win.onkeypress(self.paddle_down, "Down")

    def collisions(self, object):
        paddle_dist = self.get_player * (self.screen_width // 2 - 60)
        if (object.drawn.xcor() >= paddle_dist and object.drawn.xcor() < paddle_dist+5) and (object.drawn.ycor() < self.drawn.ycor() + 60 and object.drawn.ycor() > self.drawn.ycor() - 60):
            object.drawn.setx(paddle_dist)
            object.dx *= -1

class Ball(DrawShape):
    def __init__(self):
        super().__init__()
        self.drawn.goto(0,0)
        self.dx = random.choice([-1,1])*.5
        self.dy = random.choice([-1,1])*.5

        self.x_border = self.screen_width // 2 # 400
        self.y_border = self.screen_height // 2 # 300

    def movement(self):
        self.drawn.setx(self.drawn.xcor() + self.dx)
        self.drawn.sety(self.drawn.ycor() + self.dy)

        if self.drawn.ycor() >= self.y_border - 10:
            self.drawn.sety(self.y_border - 10)
            self.dy *= -1

        if self.drawn.ycor() <= -self.y_border + 10:
            self.drawn.sety(-self.y_border + 10)
            self.dy *= -1

    def scoring(self, paddle_a, paddle_b, pen):
        if self.drawn.xcor() >= self.x_border - 20:
            self.drawn.setx(0)
            self.drawn.sety(0)
            self.dx *= -1
            paddle_a.score += 1
            time.sleep(.25)

        if self.drawn.xcor() <= -self.x_border + 10:
            self.drawn.setx(0)
            self.drawn.sety(0)
            self.dx *= -1
            paddle_b.score += 1
            time.sleep(.25)

        pen.update_score(paddle_a, paddle_b)

class Pen(DrawShape):
    def __init__(self):
        super().__init__()
        self.drawn.hideturtle()
        self.drawn.goto(0, self.screen_height//2-80)

    def update_score(self, paddle_a, paddle_b):
        self.drawn.clear()
        self.drawn.write(f"{paddle_a.score} | {paddle_b.score}", align="center", font=("Courier", 32, "bold"))

def main():
    cur_win = Window()
    players = [-1,1]
    ball = Ball()
    pen = Pen()
    paddle_a = Paddle_A(players[0])
    paddle_b = Paddle_B(players[1])

    while True:
        cur_win.win.update()
        ball.movement()
        paddle_a.collisions(ball)
        paddle_b.collisions(ball)
        ball.scoring(paddle_a,paddle_b,pen)

if __name__ == "__main__":
    main()