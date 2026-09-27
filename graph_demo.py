from manim import *
import numpy as np

class GraphDemo(Scene):
    def construct(self):
        # Axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-2, 2, 0.5],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": True},
        )
        labels = axes.get_axis_labels("x", "y")
        self.play(Create(axes), FadeIn(labels))

        # 1) Plot y = sin(x)
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        sin_label = MathTex("y=\\sin x").next_to(axes, UP + RIGHT)
        self.play(Create(sin_graph), FadeIn(sin_label))

        # Dot sliding along sin(x)
        t = ValueTracker(0)
        dot = always_redraw(
            lambda: Dot(axes.c2p(t.get_value(), np.sin(t.get_value())))
        )
        self.play(FadeIn(dot))
        self.play(t.animate.set_value(8), run_time=4, rate_func=linear)
        self.wait(0.3)

        # 2) Morph into a damped, faster sine: y = e^{-0.2x} sin(kx)
        k = ValueTracker(1.0)
        damped = always_redraw(
            lambda: axes.plot(
                lambda x: np.exp(-0.2 * x) * np.sin(k.get_value() * x),
                color=YELLOW,
            )
        )
        damped_label = MathTex(r"y=e^{-0.2x}\sin(kx)").next_to(axes, UP + RIGHT)

        # Swap labels and graph smoothly
        self.play(ReplacementTransform(sin_graph, damped), FadeTransform(sin_label, damped_label))
        self.play(k.animate.set_value(2.5), run_time=3)
        self.wait(0.3)

        # 3) Add cos(x), then fade it
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        cos_label = MathTex("y=\\cos x").next_to(axes, RIGHT)
        self.play(Create(cos_graph), FadeIn(cos_label))
        self.wait(0.5)
        self.play(FadeOut(cos_graph), FadeOut(cos_label))
        self.wait(0.3)

        # Wrap up
        self.play(*map(FadeOut, [damped, damped_label, dot, axes, labels]))
