import reflex as rx
import  El_Blog_de_Maria.styles.styles as style




def title(text:str) -> rx.Component:
    return rx.heading(
        text,
        size='7',
        style=style.title_style    
    )