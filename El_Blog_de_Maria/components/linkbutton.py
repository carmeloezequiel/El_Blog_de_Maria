import reflex as rx 

def link_button(name:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(name),
        href=url,
        is_external=True
    )