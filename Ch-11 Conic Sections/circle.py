from manim import *

class Circle_Scene(Scene):

    def construct(self):

        circle_val = ValueTracker(0)

        grid = Axes([-3, 3, 1], [-1.5, 1.5, 1])
        center = Dot((0, 0, 0))
        circle = Circle(radius=2, color=RED_C)
        center_coords = MathTex("(a, b)").shift(DOWN * 0.35 + LEFT * 0.6)

        line = Line(ORIGIN, RIGHT*2, color=GREEN_C)
        brace_r = BraceLabel(line, "r", UP)

        text1 = Text("Formation of Circle")
        text1.move_to((-4, 3, 0))

        line.add_updater(lambda m: m.set_angle(circle_val.get_value()))

        gp = VGroup(grid, center, circle, center_coords, line, brace_r)

        self.play(Create(grid))
        self.play(Create(text1))
        self.play(Create(center))
        self.play(Create(line))
        self.play(Create(center_coords))
        self.play(circle_val.animate(run_time=2, rate_func=linear).set_value(2 * PI), Create(circle, run_time=2, rate_func=linear))

        self.play(Create(brace_r))

        self.wait(2)
        self.play(Uncreate(text1))
        self.play(gp.animate.shift(LEFT*4))

        eq = MathTex("(x - a)^2 + (y - b)^2 = r^2").shift(RIGHT*4 + UP*2)
        self.play(Write(eq))

        self.wait(3)
        self.clear()
        
        credits = MarkupText(f"Made by <span color=\"{BLUE}\">Harsh Narayan Jha</span> using <span color=\"{YELLOW}\">manim</span>.", font_size=36)
        self.play(FadeIn(credits))
        self.wait(1)
        self.play(FadeOut(credits))