from manim import *

class ThreeD_Scene_Test(ThreeDScene):

    TEXT_FONT_SIZE = 84
    def create_axes(self):
        self.axis = ThreeDAxes((-5, 5, 1), (-5, 5, 1), (-5, 5, 1))

        self.x_label = self.axis.get_x_axis_label("x")
        self.y_label = self.axis.get_y_axis_label("y").move_to((0, 5 + 1, 0))
        self.z_label = self.axis.get_z_axis_label("z")

        self.axis.get_x_axis().set_color(RED)
        self.axis.get_y_axis().set_color(GREEN)
        self.axis.get_z_axis().set_color(BLUE)

        self.set_camera_orientation(phi=0, theta = -90 * DEGREES, zoom=0.6)
        self.play(Create(self.axis), Write(self.x_label), Write(self.y_label), Write(self.z_label))

    def text_part_1(self):
        text1 = Text("We know the 2-D Coordinate Plane quite well", font_size=self.TEXT_FONT_SIZE, t2c={'2-D Coordinate Plane': YELLOW}, disable_ligatures=True)
        self.play(FadeIn(text1))
        self.wait(3)

        text2 = Text("The X and Y Axes", font_size=self.TEXT_FONT_SIZE, t2c={'X': RED, 'Y': GREEN}, disable_ligatures=True)
        self.play(ReplacementTransform(text1, text2))
        self.wait(3)
        self.play(FadeOut(text2))

    def get_P_coords(self):
        return self.P_coords[0].get_value(), self.P_coords[1].get_value(), self.P_coords[2].get_value()

    def get_P_coords_text(self):
        return rf"P ({int(self.P_coords[0].get_value())}, {int(self.P_coords[1].get_value())}, {int(self.P_coords[2].get_value())})"

    def point_P_setup(self):
        self.P_coords_x = ValueTracker(2)
        self.P_coords_y = ValueTracker(3)
        self.P_coords_z = ValueTracker(0)
        self.P_coords = [self.P_coords_x, self.P_coords_y, self.P_coords_z]

        self.P = Dot(point=self.axis.c2p(*self.get_P_coords()))
        self.P.add_updater(lambda m: m.move_to(self.get_P_coords()))

        self.P_txt = MathTex(rf"P ({int(self.P_coords[0].get_value())}, {int(self.P_coords[1].get_value())})", color=YELLOW, font_size=36).next_to(self.P)

        self.P_txt_3d = MathTex(self.get_P_coords_text(), color=YELLOW, font_size=36).next_to(self.P).rotate(90 * DEGREES, axis=X_AXIS)
        self.P_txt_3d.add_updater(lambda m: m.become(MathTex(self.get_P_coords_text(), color=YELLOW, font_size=36).next_to(self.P).rotate(90 * DEGREES, axis=X_AXIS)))

        self.play(Create(self.P), Create(self.P_txt))
        self.wait(3)

        self.x_dot_line = DashedLine(start=ORIGIN, end=(1, 0, 0), color=RED)
        self.x_dot_line.add_updater(lambda m: m.put_start_and_end_on(start=(0, self.P.get_y(), 0), end=(self.P.get_x(), self.P.get_y(), 0)))

        self.y_dot_line = DashedLine(start=ORIGIN, end=(0, 1, 0), color=GREEN)
        self.y_dot_line.add_updater(lambda m: m.put_start_and_end_on(start=(self.P.get_x(), 0, 0), end=(self.P.get_x(), self.P.get_y(), 0)))

        self.z_dot_line = DashedLine(start=ORIGIN, end=(0, 0, 1), color=BLUE)

        self.play(Create(self.x_dot_line), Create(self.y_dot_line))

    def text_part_2(self):
        text3 = Text("Now let's add another Dimension into play", font_size=self.TEXT_FONT_SIZE, t2c={'Dimension': YELLOW}, disable_ligatures=True)
        self.play(FadeIn(text3))
        self.wait(3)

        text4 = Text("The Z axis", font_size=self.TEXT_FONT_SIZE + 60, t2c={'Z': BLUE}, disable_ligatures=True)
        self.play(ReplacementTransform(text3, text4))
        self.wait(3)
        self.play(FadeOut(text4))

    def show_planes(self):
        self.xy_plane = Square(8).set_fill(RED, opacity=0.3).set_stroke(GREEN)
        self.xy_plane_text = Text("The XY Plane", font_size=self.TEXT_FONT_SIZE, t2c={'X': RED, 'Y': GREEN}, disable_ligatures=True)

        self.yz_plane = Square(8).set_fill(GREEN, opacity=0.3).set_stroke(BLUE).rotate(90 * DEGREES, axis=X_AXIS).rotate(90 * DEGREES, axis=Z_AXIS)
        self.yz_plane_text = Text("The YZ Plane", font_size=self.TEXT_FONT_SIZE, t2c={'Z': BLUE, 'Y': GREEN}, disable_ligatures=True).rotate(90 * DEGREES, axis=X_AXIS).rotate(90 * DEGREES, axis=Z_AXIS)

        self.xz_plane = Square(8).set_fill(BLUE, opacity=0.3).set_stroke(RED).rotate(90 * DEGREES, axis=Y_AXIS).rotate(90 * DEGREES, axis=Z_AXIS)
        self.xz_plane_text = Text("The XZ Plane", font_size=self.TEXT_FONT_SIZE, t2c={'X': RED, 'Z': BLUE}, disable_ligatures=True).rotate(90 * DEGREES, axis=X_AXIS)

        self.play(Create(self.xy_plane))
        self.play(Write(self.xy_plane_text))
        self.wait()
        self.play(Uncreate(self.xy_plane), Unwrite(self.xy_plane_text))

        self.play(Create(self.yz_plane))
        self.play(Write(self.yz_plane_text))
        self.wait()
        self.play(Uncreate(self.yz_plane), Unwrite(self.yz_plane_text))

        self.play(Create(self.xz_plane))
        self.play(Write(self.xz_plane_text))
        self.wait()
        self.play(Uncreate(self.xz_plane), Unwrite(self.xz_plane_text))

    def show_octants(self):
        self.oct_1 = Cube(4, 0.1, WHITE, 4).move_to((2, 2, 2))
        self.oct_1_text = MathTex(r"Octant XYZ", font_size=self.TEXT_FONT_SIZE)

        self.oct_2 = Cube(4, 0.1, WHITE, 4).move_to((-2, 2, 2))
        self.oct_2_text = MathTex(r"Octant X'YZ", font_size=self.TEXT_FONT_SIZE)

        self.oct_3 = Cube(4, 0.1, WHITE, 4).move_to((-2, -2, 2))
        self.oct_3_text = MathTex(r"Octant X'Y'Z", font_size=self.TEXT_FONT_SIZE)

        self.oct_4 = Cube(4, 0.1, WHITE, 4).move_to((2, -2, 2))
        self.oct_4_text = MathTex(r"Octant XY'Z", font_size=self.TEXT_FONT_SIZE)

        self.oct_5 = Cube(4, 0.1, WHITE, 4).move_to((2, 2, -2))
        self.oct_5_text = MathTex(r"Octant XYZ'", font_size=self.TEXT_FONT_SIZE)

        self.oct_6 = Cube(4, 0.1, WHITE, 4).move_to((-2, 2, -2))
        self.oct_6_text = MathTex(r"Octant X'YZ'", font_size=self.TEXT_FONT_SIZE)
        
        self.oct_7 = Cube(4, 0.1, WHITE, 4).move_to((-2, -2, -2))
        self.oct_7_text = MathTex(r"Octant X'Y'Z'", font_size=self.TEXT_FONT_SIZE)

        self.oct_8 = Cube(4, 0.1, WHITE, 4).move_to((2, -2, -2))
        self.oct_8_text = MathTex(r"Octant XY'Z'", font_size=self.TEXT_FONT_SIZE)

        self.octs = [(self.oct_1, self.oct_1_text), (self.oct_2, self.oct_2_text), (self.oct_3, self.oct_3_text), (self.oct_4, self.oct_4_text),
                (self.oct_5, self.oct_5_text), (self.oct_6, self.oct_6_text), (self.oct_7, self.oct_7_text), (self.oct_8, self.oct_8_text)]

        # for i in range(6):
        #     self.octs.pop()

        for i, j in self.octs:
            j.to_corner(UP+RIGHT)

        for oct, text in self.octs:
            self.play(Create(oct))
            self.add_fixed_in_frame_mobjects(text)
            self.wait()
            self.play(Uncreate(oct), Unwrite(text))


    def construct(self):

        self.create_axes()
        self.text_part_1()

        self.point_P_setup()

        self.text_part_2()

        self.move_camera(phi=60*DEGREES, theta = -45 * DEGREES, focal_distance=10, zoom=1, run_time=3)
        self.play(self.x_label.animate.rotate(90 * DEGREES, axis=X_AXIS),
                    self.y_label.animate.rotate(90 * DEGREES, axis=X_AXIS),
                    self.P_txt.animate.rotate(90 * DEGREES, axis=X_AXIS))

        self.play(self.P_txt.animate.become(self.P_txt_3d))
        self.P_txt.add_updater(lambda m: m.become(MathTex(self.get_P_coords_text(), color=YELLOW, font_size=36).next_to(self.P).rotate(90 * DEGREES, axis=X_AXIS)))

        line = Arrow(start=ORIGIN, end=self.P.get_center())
        line.add_updater(lambda m: m.put_start_and_end_on(ORIGIN, self.P.get_center()))

        self.play(Create(line))

        self.play(self.P_coords_z.animate.set_value(1))

        self.play(Uncreate(line))

        self.z_dot_line.add_updater(lambda m: m.put_start_and_end_on(start=(self.P.get_x(), self.P.get_y(), 0), end=(self.P.get_x(), self.P.get_y(), self.P.get_z())))
        self.play(Create(self.z_dot_line))

        self.play(self.P_coords_z.animate.set_value(2))

        self.play(self.P_coords_x.animate.set_value(-3), self.P_coords_y.animate.set_value(1), self.P_coords_z.animate.set_value(2))
        self.wait()
        self.play(self.P_coords_x.animate.set_value(4), self.P_coords_y.animate.set_value(-4), self.P_coords_z.animate.set_value(3))
        self.wait()
        self.play(self.P_coords_x.animate.set_value(1), self.P_coords_y.animate.set_value(2), self.P_coords_z.animate.set_value(4))
        self.wait()
        # self.play(self.P_coords_x.animate.set_value(-1), self.P_coords_y.animate.set_value(-2), self.P_coords_z.animate.set_value(3))
        # self.wait()

        self.show_planes()

        self.move_camera(phi=60*DEGREES, theta = -135 * DEGREES, focal_distance=20, zoom=1, run_time=3)

        self.show_octants()
        self.wait(3)

        self.clear()
        self.set_camera_orientation(phi=0, theta = -90 * DEGREES, zoom=1)

        # Formulas
        form_text_1 = Text("The Distance formula is now also influenced by the Z coordinates", font_size=36, t2c={'Z': BLUE}, disable_ligatures=True)
        self.play(Write(form_text_1))
        self.wait()
        self.play(Unwrite(form_text_1))

        distance_formula = MathTex(r"AB\,=\,\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}", substrings_to_isolate="xyz")

        distance_formula.set_color_by_tex("x", RED)
        distance_formula.set_color_by_tex("y", GREEN)
        distance_formula.set_color_by_tex("z", BLUE)

        self.play(Write(distance_formula, run_time=3))
        self.wait(3)
        self.play(Unwrite(distance_formula, run_time=3))

        form_text_2 = Text("The Section formula is also influenced by the Z coordinates", font_size=36, t2c={'Z': BLUE}, disable_ligatures=True)
        self.play(Write(form_text_2))
        self.wait()
        self.play(Unwrite(form_text_2))

        section_formula = MathTex(r"P(x,y,z) = \Big(", r"{m_1x_2+m_2x_1", r"\over", r"m_1+m_2},", r"{m_1y_2+m_2y_1", r"\over", r"m_1+m_2},", r"{m_1z_2+m_2z_1", r"\over", r"m_1+m_2}", r"\Big)", substrings_to_isolate="xyz")

        section_formula.set_color_by_tex("x", RED)
        section_formula.set_color_by_tex("y", GREEN)
        section_formula.set_color_by_tex("z", BLUE)

        self.play(Write(section_formula, run_time=3))
        self.wait(3)
        self.play(Unwrite(section_formula, run_time=3))

        self.clear()
        self.wait(1)

        credits = MarkupText(f"Made with ❤ by <span color=\"{BLUE}\">Harsh Narayan Jha</span> using <span color=\"{YELLOW}\">manim</span>.", font_size=36)
        self.play(FadeIn(credits))
        self.wait(1)
        self.play(Unwrite(credits, reverse=False))
