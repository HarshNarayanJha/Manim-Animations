from manim import *

class Wronskian(Scene):
    def construct(self):
        theW = Text("The Wronskian")

        defi = MathTex("The Wronskian of n differentiable functions is the determinant formed with the functions and their n - 1 first derivatives`")
        # self.play(Write(theW, run_time=4))
        # self.play(FadeOut(theW))

        self.play(Write(defi, run_time=8))
