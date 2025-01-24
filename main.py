from manim_imports_ext import *


class MainScene(VoiceoverScene,ThreeDScene):

    def construct(self):
        self.set_speech_service(
            KokoroService(
                voice=voice_artist,
                volume=1.5,
            ))
        
        title = Title("Algebraic Modeling").set_color(RED)
        self.add(title)

        box = Square().set_color(RED).set_fill(RED, opacity=1)
        model = MathTex("x \\times y = z").set_color(text_color).scale(2.5)
        five = Text("5").set_color(text_color).next_to(box, UP * 3)
        fifteen = Text("15").set_color(text_color)

        with self.voiceover("""
                            think of algebraic model as a <bookmark mark='box'/>box, which you put some values <bookmark mark='input'/>inside, and it <bookmark mark='output'/>returns the result.
                            """) as tracker:
            
            self.wait_until_bookmark("box")
            self.add(box)

            self.wait_until_bookmark("input")
            self.play(five.animate.shift(DOWN * 2), run_time=1)
            self.play(ReplacementTransform(five, fifteen))

            self.wait_until_bookmark("output")
            self.play(fifteen.animate.shift(DOWN * 3), run_time=1)
            self.play(Indicate(fifteen))
            self.play(FadeOut(box), FadeOut(fifteen))

        with self.voiceover("""
                            <bookmark mark='model'/>x times y equals z, is an example of algebraic model,
                            where <bookmark mark='x'/>x represents the number of hours of work you did, <bookmark mark='y'/>y represents the amount of money you earn per hour, and <bookmark mark='z'/>z represents the total amount of money you earn.
                            """) as tracker:

            self.wait_until_bookmark("model")
            self.play(Write(model))

            self.wait_until_bookmark("x")
            self.play(Indicate(model[0][0]))

            self.wait_until_bookmark("y")
            self.play(Indicate(model[0][2]))

            self.wait_until_bookmark("z")
            self.play(Indicate(model[0][4]))

            self.wait()