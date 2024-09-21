import reflex as rx 
import El_Blog_de_Maria.styles.styles as styles

def link_button(name:str, body: str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag=name.lower(),
                        width=styles.Spacer.BIG.value,
                        height=styles.Spacer.BIG.value),
                rx.vstack(
                    rx.text(name, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items='start',
                    spacing='0px'
                )
                )
                ),
        href=url,
        is_external=True,
        width='100%'
        
    )