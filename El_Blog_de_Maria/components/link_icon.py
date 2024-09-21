import reflex as rx
import  El_Blog_de_Maria.styles.styles as style


def link_icon(url:str) -> rx.Component:
    return rx.link(
        rx.icon(tag='facebook'),
        href=url,
        is_external=True
    )