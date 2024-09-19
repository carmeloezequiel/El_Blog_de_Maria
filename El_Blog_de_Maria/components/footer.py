import reflex as rx
import datetime



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.text(f'2018-{datetime.date.today().year} El Blog de Maria by Maria')
    )