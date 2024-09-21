import reflex as rx
import  El_Blog_de_Maria.styles.styles as style




def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            'El Blog de Maria',
            height='40px'
        ),
        position='sticky',
        bg='lightgray',
        padding_x=style.Spacer.DEFAULT.value,
        padding_y=style.Spacer.SMALL.value, 
        z_index='999',
        top='0'
    )