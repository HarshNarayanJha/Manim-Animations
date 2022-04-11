from manim import *

class Ellipse_Scene(Scene):
    
    def construct(self):

        a = 6
        b = 4
        
        grid = Axes([-3, 3, 1], [-1.5, 1.5, 1])
        # directrix = DoubleArrow((-3, 3, 0), (-3, -3, 0))
        # directrix_l = MathTex("l").next_to(directrix, LEFT)
        focus_1 = Dot((-2, 0, 0), color=PINK)
        focus_2 = Dot((2, 0, 0), color=PINK)

        line = Line(ORIGIN, focus_2)

        ellipse = Ellipse(a, b)

        self.play(Create(grid))
        # self.play(Create(directrix))
        # self.play(Create(directrix_l))
        self.play(Create(focus_1), Create(focus_2))
        self.play(Create(ellipse))