from manim import Matrix, Rectangle, ReplacementTransform, Scene, MathTex, Unwrite, Write, MarkupText, Text, Transform, Tex
from manim.constants import RIGHT, UP, LEFT, DOWN, UL, UR, DL, DR
from manim.utils import color

class Warshall(Scene):

    def intro(self):
        intro_text = Text("Warshall's Algoritm", font_size=94)
        what_is_it = Text("What is it?", font_size=42)
        definition = Tex(r'It is used to find the ``transitive closure" of a\\'\
                         r'directed graph using an iterative algorithm.')

        self.play(Write(intro_text))
        self.wait(3)
        self.play(Transform(intro_text, what_is_it))
        self.wait(4)
        self.play(Transform(intro_text, definition))
        self.wait(5)

        self.play(Unwrite(intro_text))

        self.wait(1.5)

    def relation(self):
        relation_text = Tex(r'Consider this relation \\'\
                            r'$R = \{(1, 2), (2, 3), (4, 5), (5, 2)\}$\\'\
                            r'Over the Set $A = \{1, 2, 3, 4, 5\}$')
        text1 = Tex(r'A Transitive clouser literally means to form the\\'\
                    r'``full transitive relation" for a given relation.')
        text2 = Tex(r'We can do it manually, but there is this\\'\
                    r'nice algorithm called ``Warshall Algorithm"\\'\
                    r'which provides a systematic method to find that.')

        text2.submobjects[0][52:69].set_fill(color.YELLOW)

        text3 = Tex(r'``It works out like this, for each element in the Set A = k,\\'\
                    r'if there is a relation from i to k and k to j\\'\
                    r'form a relation from i to j')

        relation_text.to_edge(UP + DOWN * 0.2)
        text1.move_to(relation_text.get_bottom() + DOWN * 1.2)
        text2.move_to(text1.get_bottom() + DOWN * 1.2)
        text3.move_to(text2.get_bottom() + DOWN * 1.2)

        self.play(Write(relation_text))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(5)

        self.play(Unwrite(text1), Unwrite(text2), Unwrite(text3))
        self.play(relation_text.animate.to_edge(UP).scale(0.8))

        self.wait(1.5)

    def construct(self):

        # self.intro()
        # self.relation()

        matrix_initial = [[0] * 5] * 5

        # matrix_initial_tex = Matrix(r"""\begin{bmatrix}
        # 0 & 0 & 0 & 0 & 0\\
        # 0 & 0 & 0 & 0 & 0\\
        # 0 & 0 & 0 & 0 & 0\\
        # 0 & 0 & 0 & 0 & 0\\
        # 0 & 0 & 0 & 0 & 0\\
        # \end{bmatrix}
        # """)
        #
        matrix_initial_tex = Matrix(matrix_initial, v_buff=0.6, h_buff=0.75)

        matrix_tex_brackets = matrix_initial_tex.get_brackets()
        matrix_tex_rows = matrix_initial_tex.get_rows()


        matrix_columns = MathTex(r"""1 \quad 2 \quad 3 \quad 4 \quad 5""", color=color.GREY)
        matrix_rows = MathTex(r"""\begin{array}{c} 1 \\ 2 \\ 3 \\ 4 \\ 5 \end{array}""", color=color.GREY)

        matrix_columns.move_to(matrix_initial_tex.get_top() + UP * 0.5)
        matrix_rows.move_to(matrix_initial_tex.get_left() + LEFT * 0.8)

        adjancy_text = Text("Adjacency Matrix")
        adjancy_text.to_edge(UP, buff=0.8)

        relation_tex = MathTex(r"R = \{(1, 2), (2, 3), (4, 5), (5, 2)\}")
        relation_tex.to_edge(DOWN, buff=0.2)

        self.play(Write(matrix_tex_brackets))
        self.play(Write(matrix_columns), Write(matrix_rows))
        self.play(Write(adjancy_text), Write(relation_tex))

        self.play(Write(matrix_tex_rows[0]))
        prev_row = matrix_tex_rows[0]
        for row in matrix_tex_rows[1:]:
            self.wait(0.01)
            self.play(ReplacementTransform(prev_row.copy(), row))
            prev_row = row


        self.wait(1.8)

        one_tex = Tex("1", color=color.BLUE_C)

        replace_instructions = []
        for x, y in ((1, 2), (2, 3), (4, 5), (5, 2)):
            replace_instructions.append(
                ReplacementTransform(matrix_tex_rows[x-1][y-1], one_tex.copy().move_to(matrix_tex_rows[x-1][y-1].get_center()))
            )
            matrix_rows[0][x-1].set_color(color.GREEN)
            matrix_columns[0][y-1].set_color(color.GREEN)

        self.play(*replace_instructions)

        self.wait()
