from manim_imports_ext import *

class MainScene(VoiceoverScene, ThreeDScene):

    def construct(self):
        self.set_speech_service(
            KokoroService(
                volume=1.5,
            )
        )

        title = Title("Algebraic Modeling").set_color(WHITE)
        self.add(title)

        box = Rectangle(height=1.5, width=3).set_color(RED).set_fill(WHITE, opacity=1).round_corners(0.1).set_stroke(width=0)
        times_three = Text("multiply").set_color(BgColor).scale(0.8)
        model = MathTex("x \\times y = z").set_color(text_color).scale(2.5)
        x_element = model[0][0]
        times = model[0][1]
        y_element = model[0][2]
        z_element = model[0][4]

        five = Text("5").set_color(text_color).next_to(box.get_center(), UP * 6 + LEFT)
        three = Text("3").set_color(text_color).next_to(box.get_center(), UP * 6 + RIGHT)
        fifteen = Text("15").set_color(text_color)

        with self.voiceover(
            """
                            think of algebraic model as a <bookmark mark='box'/>box,
                            which you put some values <bookmark mark='input'/>inside,
                            and it <bookmark mark='output'/>returns the result.
                            """
        ) as tracker:

            self.wait_until_bookmark("box")
            self.add(box, times_three)


            self.wait_until_bookmark("input")
            self.play(
                AnimationGroup(
                    five.animate.shift(DOWN * 2),
                    three.animate.shift(DOWN * 2),
                )
            )


            # self.play(five.animate.shift(DOWN * 2), run_time=1)
            self.play(
                AnimationGroup(
                    FadeOut(three),
                    ReplacementTransform(five, fifteen))
                )
                

            self.wait_until_bookmark("output")
            self.play(fifteen.animate.shift(DOWN * 3), run_time=1)
            self.play(Indicate(fifteen))
            self.play(FadeOut(box), FadeOut(times_three), FadeOut(fifteen))

        with self.voiceover(
            """
                            <bookmark mark='model'/>x times y equals z, is an example of algebraic model,
                            where <bookmark mark='x'/>x represents the number of hours of work you did,
                            <bookmark mark='y'/>y represents your hourly rate,
                            and <bookmark mark='z'/>z represents the total amount of money you earn.
                            """
        ) as tracker:

            self.wait_until_bookmark("model")
            self.play(Write(model))

            self.wait_until_bookmark("x")
            self.play(Indicate(model[0][0]))

            self.wait_until_bookmark("y")
            self.play(Indicate(model[0][2]))

            self.wait_until_bookmark("z")
            self.play(Indicate(model[0][4]))

            self.wait()

        with self.voiceover(
            """
                            let's say you worked for <bookmark mark='five_tag'/>5 hours, and your hourly rate is <bookmark mark='twenty_tag'/>20 dollars,
                            by <bookmark mark='mult'/>multiplying 5 and 20, you get <bookmark mark='hundred_tag'/>100 dollars, which is the total amount of money you earn.
                            """
        ) as tracker:
            
            transformed_model = MathTex("5 \\times 20 = 100").set_color(text_color).scale(2)
            transformed_model[0][0].move_to(x_element.get_center())
            transformed_model[0][2:4].move_to(y_element.get_center()).shift(UP * 0.15)
            transformed_model[0][5:8].move_to(z_element.get_center()).shift(UP * 0.05 + RIGHT * 0.1)

            self.wait_until_bookmark("five_tag")
            self.play(
                Transform(x_element, transformed_model[0][0]),
            )

            self.wait_until_bookmark("twenty_tag")
            self.play(
                Transform(y_element, transformed_model[0][2:4]),
            )

            self.wait_until_bookmark("mult")
            self.play(
                Indicate(times),
            )
            rect_100 = SurroundingRectangle(transformed_model[0][5:8], buff=0.1).set_color(GREEN)

            self.wait_until_bookmark("hundred_tag")
            self.play(
                AnimationGroup(
                    Transform(z_element, transformed_model[0][5:8]), 
                    Create(rect_100)
                )
            )

            self.wait()
            self.play(
                AnimationGroup(
                    FadeOut(rect_100),
                    FadeOut(transformed_model),
                    FadeOut(model)
                )

            )
        self.wait(1)
        with self.voiceover(
                """
                            Algebraic models are also called formulas,
                            <bookmark mark='formulas'/>and they can range from simple to more and more complex,
                            as you can see here.
                        """):
            pass
                
            linear_eq = MathTex("y = mx + c")
            quadratic_eq = MathTex("ax^2 + bx + c = 0")
            pythagorean = MathTex("a^2 + b^2 = c^2")

            exponential_growth = MathTex("P(t) = P_0 e^{rt}")
            system_eq = MathTex(
                r"""
                \begin{cases}
                a_1 x + b_1 y = c_1 \\
                a_2 x + b_2 y = c_2
                \end{cases}
                """
            )
            binomial_theorem = MathTex("(a + b)^n = \\sum_{k=0}^n \\binom{n}{k} a^{n-k} b^k")

            schrodinger_eq = MathTex("i\\hbar \\frac{\partial \\psi}{\\partial t} = \\hat{H} \\psi")
            einstein_eq = MathTex("G_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = \\frac{8\\pi G}{c^4} T_{\\mu\\nu}")

            self.wait_until_bookmark("formulas")
            self.play(Write(linear_eq))
            self.play(ReplacementTransform(linear_eq, quadratic_eq))
            self.wait(0.5)
            self.play(ReplacementTransform(quadratic_eq, pythagorean))
            self.wait(0.5)

            self.play(ReplacementTransform(pythagorean, exponential_growth))
            self.wait(0.5)

            self.play(ReplacementTransform(exponential_growth, system_eq))
            self.wait(0.5)

            self.play(ReplacementTransform(system_eq, binomial_theorem))
            self.wait(0.5)

            self.play(ReplacementTransform(binomial_theorem, schrodinger_eq))
            self.wait(0.5)

            self.play(ReplacementTransform(schrodinger_eq, einstein_eq))
            self.wait(2)
