import reflex as rx
import datetime

import  El_Blog_de_Maria.styles.styles as style

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.text(f'2020-{datetime.date.today().year} El Blog de Maria by Maria',
                font_size=style.Spacer.MEDIUM.value),
        margin_y=style.Spacer.BIG.value,
        margin_x=style.Spacer.SMALL.value,
        width='100%',
        align_items='center'
    )