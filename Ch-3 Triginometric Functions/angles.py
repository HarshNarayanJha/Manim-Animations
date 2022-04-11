from math import cos, degrees, sin
import math
from manim import *
from manim.mobject.geometry import ArrowTriangleTip

class Angles(Scene):

    def construct(self):

        intro_text = Text("Angles", font_size=72)
        intro_underline = Underline(intro_text)
        intro_underline.add_updater(lambda m: m.next_to(intro_text, direction=DOWN, buff=SMALL_BUFF).match_width(intro_text))

        self.play(Write(intro_text))
        self.wait(2)
        self.play(intro_text.animate.move_to((-6, 3, 0)).set_font_size(36).set_color(GOLD), GrowFromCenter(intro_underline))

        angle_val_r = ValueTracker(0.00)
        angle_val_d = ValueTracker(0.00)
        
        line1 = Arrow(start=LEFT*2, end=RIGHT*2, tip_shape=ArrowTriangleTip)
        line2 = Arrow(start=LEFT*2, end=RIGHT*2, tip_shape=ArrowTriangleTip)
        line2.add_updater(lambda m: m.set_angle(angle_val_r.get_value()))

        point_a = MarkupText(f"<span color=\"{GREEN}\">A</span>", font_size=28).next_to(line1)
        point_b = MarkupText(f"<span color=\"{RED}\">B</span>", font_size=28).next_to(line2)
        point_b.add_updater(lambda m: m.next_to(line2.tip, direction=UP+RIGHT if angle_val_r.get_value() > 0 else DOWN+RIGHT))

        vertex_text = MarkupText("O\nVertex", font_size=24).shift(LEFT*2+DOWN*0.25)
        initial_text = MarkupText(f"<span color=\"{GREEN}\">Initial Side</span>", font_size=24).next_to(line1, direction=DOWN)
        initial_text.add_updater(lambda m: m.next_to(line1, direction=DOWN if angle_val_r.get_value() > 0 else UP))

        terminal_text = MarkupText(f"<span color=\"{RED}\">Terminal Side</span>", font_size=24).next_to(line2).rotate_about_origin(0.5)
        terminal_text.add_updater(lambda m: m.next_to(line2, direction=ORIGIN).shift(UP*0.4+LEFT*0.1 if angle_val_r.get_value() > 0 else DOWN*0.4+LEFT*0.1))

        self.play(Create(line1), Create(line2))

        self.play(angle_val_r.animate.set_value(0.5), angle_val_d.animate.set_value(degrees(0.5)))
        
        self.play(Write(point_a), Write(point_b))

        self.play(Write(vertex_text), Write(initial_text), Write(terminal_text))

        angle = Angle(line1, line2, radius=1.25)
        angle.add_updater(lambda m: m.become(Angle(line1, line2, radius=1.25, other_angle=angle_val_r.get_value() < 0)))

        self.play(Create(angle))

        degree_var = Variable(angle_val_d.get_value(), r"Angle\,(in\,^\circ)").move_to((4, -2, 0))
        radian_var = Variable(angle_val_r.get_value(), r"Angle\,(in\,radians)").next_to(degree_var, DOWN, aligned_edge=RIGHT)
        degree_var.tracker = angle_val_d
        radian_var.tracker = angle_val_r

        angle_group = VGroup(line1, line2, point_a, point_b, vertex_text, initial_text, terminal_text, angle)

        self.wait(2)

        # About Angles Begin #
        about_angle_text_1 = MarkupText(f"<span color=\"{GOLD}\">Angle</span> is the measure of <u>rotation</u> of a given ray about its initial point.", font_size=26)
        about_angle_text_2 = MarkupText(f"The original ray is called the <span color=\"{GREEN}\">Initial Ray</span> and the final position of the ray\nis called the <span color=\"{RED}\">Terminal Side</span> of the angle.", font_size=26)
        about_angle_text_3 = MarkupText(f"The point of <u>rotation</u> is called Vertex.", font_size=26)

        about_angle_text_1.shift(DOWN*1.5)
        about_angle_text_2.next_to(about_angle_text_1, direction=DOWN)
        about_angle_text_3.next_to(about_angle_text_2, direction=DOWN)

        self.play(Write(about_angle_text_1, run_time=2.5))
        self.play(Write(about_angle_text_2, run_time=2.5))
        self.play(Write(about_angle_text_3, run_time=2.5))

        self.wait(3)

        self.play(Unwrite(about_angle_text_1), Unwrite(about_angle_text_2), Unwrite(about_angle_text_3))
        # About Angles End #

        # About Angle sign Begin #
        about_angle_sign_text_1 = MarkupText(f"If the direction of <u>rotation</u> is <span color=\"{GREEN_C}\">Anticlockwise</span>, the angle is <span color=\"{GREEN_C}\">Positive (+ve)</span>.", font_size=26)
        about_angle_sign_text_2 = MarkupText(f"If the direction of <u>rotation</u> is <span color=\"{RED_C}\">Clockwise</span>, the angle is <span color=\"{RED_C}\">Negative (-ve)</span>.", font_size=26)
        about_angle_sign_text_1.shift(DOWN*2)
        about_angle_sign_text_2.shift(UP*2)
        
        self.play(Write(about_angle_sign_text_1, run_time=2.5))
        self.wait(2)
        self.play(Unwrite(about_angle_sign_text_1))

        self.play(angle_val_r.animate.set_value(-0.5), angle_val_d.animate.set_value(degrees(-0.5)), terminal_text.animate.rotate_about_origin(-1))

        self.play(Write(about_angle_sign_text_2, run_time=2.5))
        self.wait(2)
        self.play(Unwrite(about_angle_sign_text_2))
        # About Angle sign End #

        self.play(angle_val_r.animate(run_time=0.2).set_value(0.000000001), angle_val_d.animate(run_time=0.2).set_value(degrees(0.000000001)), terminal_text.animate(run_time=0.2).rotate_about_origin(0.5))
        self.wait(1)

        self.play(Unwrite(terminal_text), Unwrite(point_b))

        self.play(angle_val_r.animate(run_time=3).set_value(1.99999999*PI), angle_val_d.animate(run_time=3).set_value(degrees(1.99999999*PI)))
        self.wait(1)

        self.play(Write(point_b))

        # About Revolution Begin #
        about_revolution_text_1 = MarkupText(f"One <u>complete rotation</u> from the position of the <span color=\"{GREEN}\">Initial Side</span> is called <b>1 Revolution</b>", font_size=26)

        about_revolution_text_1.shift(DOWN*2)

        self.play(Write(about_revolution_text_1, run_time=2.5))
        self.wait(2)
        self.play(Unwrite(about_revolution_text_1))

        self.play(angle_val_r.animate.set_value(0.0000001))
        self.play(angle_val_d.animate.set_value(degrees(0.0000001)))
        # About Revolution End #

        self.wait(2)
        self.play(FadeOut(angle_group), FadeOut(angle))

        # Angles Units #
        topic_text_2 = MarkupText("We have two <i>units</i> to measure angles", font_size=50)
        topic_text_2a = Text("Degrees", color=BLUE_D, font_size=48).shift(LEFT*2)
        topic_text_2b = Text("Radians", color=YELLOW_E, font_size=48).shift(RIGHT*2)

        self.play(Write(topic_text_2, run_time=2))
        self.play(topic_text_2.animate.shift(UP*2))

        self.play(Write(topic_text_2a), Write(topic_text_2b))
        self.wait(1)
        self.play(FadeOut(topic_text_2), FadeOut(topic_text_2b), topic_text_2a.animate.next_to(intro_text, DOWN).set_font_size(36))
        # Angle Units End #

        # Degree Measure Begin #
        self.play(FadeIn(angle_group), FadeIn(angle))
        self.play(FadeOut(vertex_text), FadeOut(initial_text), FadeOut(terminal_text))#, FadeOut(point_b))

        self.play(Create(degree_var))
        self.play(Create(radian_var))

        theta_text = MathTex(r"\theta").next_to(angle, RIGHT)
        theta_text.add_updater(lambda m: m.next_to(angle, RIGHT).shift(UP*0.5))

        self.play(Create(theta_text))

        self.play(angle_val_r.animate(run_time=0.2).set_value(0.0000001), angle_val_d.animate(run_time=0.2).set_value(degrees(0.0000001)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(PI/6), angle_val_d.animate(run_time=2).set_value(degrees(PI/6)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(2*PI/6), angle_val_d.animate(run_time=2).set_value(degrees(2*PI/6)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(PI/2), angle_val_d.animate(run_time=2).set_value(degrees(PI/2)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(5*PI/6), angle_val_d.animate(run_time=2).set_value(degrees(5*PI/6)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(1.000001*PI), angle_val_d.animate(run_time=2).set_value(degrees(1.000001*PI)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(3*PI/2), angle_val_d.animate(run_time=2).set_value(degrees(3*PI/2)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(1.9999999999*PI), angle_val_d.animate(run_time=2).set_value(degrees(1.9999999999*PI)))
        self.wait(1)

        self.play(angle_val_r.animate(run_time=2).set_value(-PI/6), angle_val_d.animate(run_time=2).set_value(degrees(-PI/6)))
        self.wait(1)
        self.play(angle_val_r.animate(run_time=2).set_value(-PI/2), angle_val_d.animate(run_time=2).set_value(degrees(-PI/2)))
        self.wait(1)

        self.play(FadeOut(line1), FadeOut(line2), FadeOut(point_a), FadeOut(point_b), FadeOut(angle), FadeOut(theta_text))
        self.wait(1)
        self.play(FadeIn(topic_text_2b), topic_text_2a.animate.move_to(LEFT*2).set_font_size(48))
        self.wait(1)
        self.play(FadeOut(topic_text_2a), topic_text_2b.animate.next_to(intro_text, DOWN).set_font_size(36))

        self.wait(1)

        angle_val_r.set_value(0.000001)
        angle_val_d.set_value(degrees(0.000001))

        # Radians Part #
        unit_circle = Circle(radius=2, color=BLUE)
        line_r_1 = Line(start=ORIGIN, end=RIGHT*2)
        line_r_2 = Line(start=ORIGIN, end=RIGHT*2+UP*0.001)
        line_r_2.add_updater(lambda m: m.set_angle(angle_val_r.get_value()))

        angle_r = Angle(line_r_1, line_r_2, radius=1.5)
        angle_r.add_updater(lambda m: m.become(Angle(line_r_1, line_r_2, radius=1.5, other_angle=angle_val_r.get_value() < 0)))

        point_r_a = MarkupText(f"<span color=\"{GREEN}\">A</span>", font_size=28).next_to(line_r_1)
        point_r_b = MarkupText(f"<span color=\"{RED}\">B</span>", font_size=28).next_to(line_r_2)
        point_r_o = MarkupText("O", font_size=28).next_to(ORIGIN, LEFT+DOWN)
        point_r_b.add_updater(lambda m: m.next_to(line_r_2.get_end(), direction=UP+RIGHT if angle_val_r.get_value() > 0 else DOWN+RIGHT))

        # Wrong Part #
        # unit_circle_text_1 = MarkupText("Do you thing that trigonometry is about Triangles?", font_size=26)
        # unit_circle_text_2 = MarkupText("No, it is about circles.", font_size=26)

        # self.play(Write(unit_circle_text_1))
        # self.wait(1)
        # self.play(Transform(unit_circle_text_1, unit_circle_text_2))
        # self.wait(1)

        # self.play(FadeOut(unit_circle_text_1))
        # Wrong Part End #

        self.play(Create(unit_circle))
        self.play(Create(line_r_1), Create(line_r_2))
        self.play(Create(point_r_a), Create(point_r_b), Create(point_r_o))

        self.play(angle_val_r.animate.set_value(1), angle_val_d.animate.set_value(degrees(1)))
        self.wait(0.5)
        self.play(angle_val_r.animate.set_value(PI/2), angle_val_d.animate.set_value(degrees(PI/2)))
        self.wait(0.5)
        self.play(angle_val_r.animate.set_value(1.000000001 * PI), angle_val_d.animate.set_value(degrees(1.000000001 * PI)))
        self.wait(0.5)

        self.play(angle_val_r.animate.set_value(1), angle_val_d.animate.set_value(degrees(1)))

        arc_r = Arc(radius=2, angle=1, color=YELLOW)
        arc_line_r = Line(start=RIGHT*5, end=RIGHT*6, color=YELLOW)
        arc_line_r.set_length(arc_r.get_length())

        arc_line_r_text = MathTex(r"1\,radian", font_size=36).next_to(arc_line_r, DOWN)

        self.play(Create(arc_r))
        self.play(Transform(arc_r, arc_line_r))
        self.play(Create(arc_line_r_text))

        self.wait(4)

        self.clear()

        convert_text_1 = MathTex(r"Angle\,in\,Radians = \frac{\pi}{180}\,\times\,Angle\,in\,Degrees").shift(UP)
        convert_text_2 = MathTex(r"Angle\,in\,Degrees = \frac{180}{\pi}\,\times\,Angle\,in\,Radians").shift(DOWN)

        self.play(Write(convert_text_1, run_time=2), Write(convert_text_2, run_time=2))
        self.wait(2)
        self.play(Unwrite(convert_text_1, run_time=2), Unwrite(convert_text_2, run_time=2))

        credits = MarkupText(f"Made by <span color=\"{BLUE}\">Harsh Narayan Jha</span> using <span color=\"{YELLOW}\">manim</span>.", font_size=36)
        self.play(FadeIn(credits))
        self.wait(1)
        self.play(FadeOut(credits))