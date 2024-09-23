import reflex as rx 
import El_Blog_de_Maria.styles.styles as styles
from El_Blog_de_Maria.styles.colors import Color, Text_Color

def link_button(name:str, body: str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src=f'{name.lower()}.svg',
                        width=styles.Spacer.BIG.value,
                        height=styles.Spacer.BIG.value,
                        margin_y=styles.Spacer.SMALL.value),
                rx.vstack(
                    rx.text(name, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items='start',
                    spacing=styles.ZERO
                )
                ),
                color_scheme='amber',
                spacing=styles.ZERO,
                padding=styles.Spacer.SMALL.value
                ),
        href=url,
        is_external=True,
        width='100%'
        
    )