from manim import *
from yamlns import ns

translations = ns.load('locale-es.yaml')

def _(x):
    return translations.get(x, x)

class AxesTemplate(Scene):
    def construct(self):
        graph = Axes(
            x_range=[-1,10,1],
            y_range=[-1,10,1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip":False}
        )
        labels = graph.get_axis_labels()
        self.add(graph, labels)

polling_example = ns(
    Insoc = 304093,
    FPJ = 224331,
    FJP = 101091,
    PInt = 64030,
    PExt = 37317,
)

def dhont_sort(polling, seats):
    return list(sorted(
        (
            (float(votes)/seat, party, seat)
            for seat in range(1, seats+1)
            for party, (name, votes) in enumerate(polling_example.items())
        ),
        key=lambda x: -x[0],
    ))

class GreaterDivisors(MovingCameraScene):

    def dhondt_table(self, nseats, shown):
        table = Table(
            [
                [
                    f"{votes/(i+1.):,.1f}"
                    for i in range(nseats)
                ]
                for votes in polling_example.values()
            ],
            row_labels=[Text(party) for party in polling_example.keys()],
            col_labels=[
                Text("{}/{}".format(_("VOTES"), i+1))
                for i in range(nseats)
            ],
            top_left_entry=Text(_("PARTY")),
            include_background_rectangle=True,
            line_config=dict(
                stroke_width=1,
                color=ManimColor('#444444'),
            ),
            arrange_in_grid_config=dict(
                cell_alignment=RIGHT,
            ),
            entries_background_color=ManimColor('#666666'),
        )
        for seat in range(1, nseats):
            column = table.get_columns()[seat+1]
            for cell in column:
                cell.set_opacity(0)
        return table

    def construct(self):
        nseats=5
        table = self.dhondt_table(nseats=nseats, shown=1)
        table.scale(.5)
        self.play(FadeIn(table), scale=.5, shift=DOWN)  # animate the creation of the square
        self.wait()

        for seat in range(2, nseats+1):
            table.get_columns()[seat][0].set_opacity(1)
            self.play(FadeIn(table.get_columns()[seat][0], run_time=.2))
            table.get_columns()[seat][1:].set_opacity(1)
            self.play(FadeIn(table.get_columns()[seat][1:], lag_ratio=.2, run_time=.2))

        highlights = [
            table.get_highlighted_cell((iparty+2, seat+1), color=GREEN)
            for price, iparty, seat in dhont_sort(polling_example, nseats)[:nseats+3]
        ]
        for highlight in highlights:
            table.add_to_back(highlight)
        self.play(AnimationGroup(
            *[GrowFromCenter(h) for h in highlights],
            lag_ratio=.2,
        ))

        self.play(*[FadeOut(o) for o in self.mobjects])








class borrame(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))
