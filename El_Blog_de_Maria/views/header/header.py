import reflex as rx 
import El_Blog_de_Maria.styles.styles as styles
from El_Blog_de_Maria.components.link_icon import link_icon
import El_Blog_de_Maria.styles.colors as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src='avatar4.jpg',fallback="MR",radius="full", size='9',padding=styles.Spacer.SMALL.value, background=Color.Color.CONTENT),
            rx.vstack(
                rx.heading('El Block de María', 
                           size='7',
                           margin_top=f'{styles.Spacer.MEDIUM_BIG.value} !important',
                           margin_bottom='0px !important'
                           ),
                        
                rx.text('Papelería bonita, bullet journal, ArtJournal y scrapbooking ✨', margin_top='0px !important'),
                rx.hstack(
                    link_icon('https://www.youtube.com/watch?v=n2YrGsXJC6Y&t=12397s'),
                ),
                spacing=styles.Spacer.SMALL.value
                
                ),
                spacing=styles.Spacer.BIG.value,          
            ),
        rx.text('''
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                Hola soy maria, Hola soy maria, Hola soy maria, Hola soy maria,
                '''),
        spacing=styles.Spacer.BIG.value
    )