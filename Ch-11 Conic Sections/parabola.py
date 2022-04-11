from manim import *
from cmath import sqrt

class Parabola_Scene(Scene):
    
    def construct(self):

        def para(y):
            return (y ** 2) / (4 * a)

        grid = Axes([-1, 1, 1], [-1, 1, 1])

        a = 1
        
        directrix = DoubleArrow((-a, 4, 0), (-a, -4, 0))
        directrix_txt = MathTex("l").next_to(directrix, LEFT).shift(DOWN * 2)
        focus = Dot((a, 0, 0), color=BLUE)
        focus_F = MathTex("F (a, 0)", font_size=32).next_to(focus, DOWN).set_color(BLUE)

        y = ValueTracker(-5)

        p = Dot(color=RED)
        p.add_updater(lambda m: m.move_to((para(y.get_value()), y.get_value(), 0)))
        p_P = MathTex(f"P (x, y)", font_size=32).set_color(RED)
        p_P.add_updater(lambda m: m.next_to(p))

        directrix_L = MathTex("L", font_size=32)
        directrix_L.add_updater(lambda m: m.move_to((-a, y.get_value(), 0)).shift(LEFT*0.3))

        e_T = MathTex(r"\frac{PL}{PF} = 1 \Rightarrow PL = PF", font_size=38).move_to((3, -3, 0))

        line1 = DashedLine(color=RED)
        line2 = DashedLine(color=RED)

        line1.add_updater(lambda m: m.put_start_and_end_on(p.get_center(), focus.get_center()))
        line2.add_updater(lambda m: m.put_start_and_end_on((-a, p.get_y(), 0), p.get_center()))

        parabola = TracedPath(p.get_center, stroke_color=GREEN)

        parabola_things = VGroup(grid, directrix, directrix_txt, focus, focus_F, p, p_P, directrix_L, line1, line2, parabola, e_T)

        self.play(Create(grid))

        self.play(Create(directrix), Create(directrix_txt))

        self.play(Create(focus), Create(focus_F))
        self.play(Create(p), Create(p_P))
        self.play(Create(directrix_L))
        self.play(Create(line1), Create(line2))

        self.add(parabola)
        self.play(Write(e_T))

        self.play(y.animate(run_time=5, rate_func=linear).set_value(3))

        self.wait(3)

        p.clear_updaters()
        directrix_L.clear_updaters()
        line1.clear_updaters()
        line2.clear_updaters()
        self.play(parabola_things.animate.shift(LEFT*4))
        self.wait(2)

        eqn = MathTex("y^2 = 4ax").move_to((4, 0, 0))
        self.play(Write(eqn))
        self.play(eqn.animate.shift(UP*2))
        self.play(Write(Tex("Equation of a Parabola").move_to((4, 1, 0))))

        self.wait(2)
        self.clear()

        credits = MarkupText(f"Made by <span color=\"{BLUE}\">Harsh Narayan Jha</span> using <span color=\"{YELLOW}\">manim</span>.", font_size=36)
        self.play(FadeIn(credits))
        self.wait(1)
        self.play(FadeOut(credits))