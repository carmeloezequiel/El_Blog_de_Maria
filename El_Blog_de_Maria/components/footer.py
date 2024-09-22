import reflex as rx
import datetime

import  El_Blog_de_Maria.styles.styles as style

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='banner_maria_c.jpg', max_width=style.MAX_WIDTH, border_radius=style.Spacer.SMALL),
        rx.text(f'2020-{datetime.date.today().year} El Block de Maria by Maria',
                font_size=style.Spacer.MEDIUM.value,
                position='absolute',  # Establece la posición absoluta para superponer el texto
                bottom=0,  # Ajusta la posición vertical del texto (puedes experimentar con diferentes valores)
                padding=style.Spacer.SMALL.value),  # Agrega un poco de espacio alrededor del texto
        margin_y=style.Spacer.BIG.value,
        margin_x=style.Spacer.SMALL.value,
        width='99%',
        align_items='center'
    )