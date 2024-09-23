import reflex as rx 
import El_Blog_de_Maria.styles.styles as styles
from El_Blog_de_Maria.components.link_icon import link_icon
import El_Blog_de_Maria.styles.colors as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.tablet_and_desktop(
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
                    rx.text('Contacto para negocios: ', size='2'),
                    link_icon(f'mailto:{styles.Url.EMAIL.value}'),
                    align_items='center'
                ),
                spacing=styles.Spacer.SMALL.value
                
                ),
                spacing=styles.Spacer.BIG.value,          
            ),
        rx.heading(
            '¡Hola, amantes de la creatividad y la organización!', 
            size='5',
            text_align='left', 
            margin_y=styles.Spacer.DEFAULT.value
            ),
        rx.spacer(),
        rx.text('''
                Si te apasionan las libretas decoradas, el bullet journal, el ArtJournal y el scrapbooking, estás en el lugar perfecto.
                Mi comunidad está llena de inspiración para darle vida a tus ideas, organizar tus días con estilo y disfrutar de la papelería bonita.
                Te invito a seguirme en mis redes para explorar juntas nuevas técnicas, proyectos y mucho más. ¡Vamos a crear algo hermoso!
                ''', text_align='justify', ),
        spacing=styles.Spacer.DEFAULT.value
    ),
        rx.mobile_only(
            rx.hstack(
            rx.avatar(src='avatar4.jpg',fallback="MR",radius="full", size='8',padding=styles.Spacer.SMALL.value, background=Color.Color.CONTENT),
            rx.vstack(
                rx.heading('El Block de María', 
                           size='7',
                           margin_top=f'{styles.Spacer.MEDIUM_BIG.value} !important',
                           margin_bottom='0px !important'
                           ),
                        
                rx.text('Papelería bonita, bullet journal, ArtJournal y scrapbooking ✨', 
                        margin_top='0px !important',
                        margin_right='8px',
                        size='3',
                        text_align='left'),
                rx.hstack(
                    rx.text('Contacto para negocios: ', size='2'),
                    link_icon(f'mailto:{styles.Url.EMAIL.value}'),
                    align_items='center'
                ),
                spacing=styles.Spacer.SMALL.value
                
                ),
                spacing=styles.Spacer.SMALL.value,
                align_items='center',
                margin_x='4px'            
            ),
        rx.heading(
            '¡Hola, amantes de la creatividad y la organización!', size='4', padding=styles.Spacer.DEFAULT.value
            ),
        rx.text('''
                Si te apasionan las libretas decoradas, el bullet journal, el ArtJournal y el scrapbooking, estás en el lugar perfecto.
                Mi comunidad está llena de inspiración para darle vida a tus ideas, organizar tus días con estilo y disfrutar de la papelería bonita.
                Te invito a seguirme en mis redes para explorar juntas nuevas técnicas, proyectos y mucho más. ¡Vamos a crear algo hermoso!
                ''', size='3', text_align='justify',padding=styles.Spacer.DEFAULT.value),
        spacing=styles.Spacer.DEFAULT.value
    )
        )
        
    