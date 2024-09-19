import reflex as rx 

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="MR", size='7'),
        rx.text('@elblogdemaria'),
        rx.heading('Hola soy Maria'),
        rx.text('''
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                ''')
    )