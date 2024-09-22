import reflex as rx
from El_Blog_de_Maria.styles.colors import Color, Text_Color


def link_icon(url:str) -> rx.Component:
    return rx.link(
        rx.icon(tag='mail', color=Text_Color.HEADER.value),
        href=url,
        is_external=True,
        
    )