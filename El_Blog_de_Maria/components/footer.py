import reflex as rx
import datetime

import  El_Blog_de_Maria.styles.styles as style
from El_Blog_de_Maria.styles.colors import Text_Color

def footer() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
        rx.vstack(
        rx.image(src='banner_maria_c.jpg', max_width=style.MAX_WIDTH, border_radius=style.Spacer.SMALL, padding=style.Spacer.SMALL.value, margin_bottom=f'{style.Spacer.MEDIUM_BIG.value} !important',),
        rx.hstack(
        rx.text(f'2020-{datetime.date.today().year} El Block de Maria by Maria',
                font_size=style.Spacer.MEDIUM.value,
                #position='absolute',  # Establece la posición absoluta para superponer el texto
                bottom=0,  # Ajusta la posición vertical del texto (puedes experimentar con diferentes valores)
                padding=style.Spacer.SMALL.value), # Agrega un poco de espacio alrededor del texto
        
        rx.box('Powered by ' ,
               rx.link('Cartech', href='https://github.com/carmeloezequiel/', is_external=True, color=Text_Color.HEADER.value),
                font_size=style.Spacer.MEDIUM.value,
                padding=style.Spacer.SMALL.value), # Agrega un poco de espacio alrededor del texto
        spacing="9",
        position='absolute',
        bottom=0

        
        ),
        margin_top=style.Spacer.BIG.value,
        margin_x=style.Spacer.SMALL.value,
        width='99%',
        align_items='center'
    )
        ),
    rx.mobile_only(
        rx.vstack(
        rx.image(src='banner_maria_c.jpg', max_width='400px', border_radius=style.Spacer.SMALL, padding=style.Spacer.SMALL.value, margin_bottom=f'{style.Spacer.MEDIUM_BIG.value} !important',),
        rx.hstack(
        rx.text(f'2020-{datetime.date.today().year} El Block de Maria by Maria',
                font_size=style.Spacer.SMALL.value,
                #position='absolute',  # Establece la posición absoluta para superponer el texto
                bottom=0,  # Ajusta la posición vertical del texto (puedes experimentar con diferentes valores)
                padding=style.Spacer.SMALL.value), # Agrega un poco de espacio alrededor del texto
        
        rx.box('Powered by ' ,
               rx.link('Cartech', href='https://github.com/carmeloezequiel/', is_external=True, color=Text_Color.HEADER.value),
                font_size=style.Spacer.SMALL.value,
                padding=style.Spacer.SMALL.value), # Agrega un poco de espacio alrededor del texto
        spacing="9",
        position='absolute',
        bottom=0

        
        ),
        margin_top=style.Spacer.SMALL.value,
        #margin_x=style.Spacer.SMALL.value,
        #margin_y=style.Spacer.SMALL.value,
        width='100%',
        align_items='center'
    )
        )
        
    )