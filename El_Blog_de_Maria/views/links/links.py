import reflex as rx 
from El_Blog_de_Maria.components.linkbutton import link_button
from El_Blog_de_Maria.components.title import title
import El_Blog_de_Maria.styles.styles as style


def links() -> rx.Component:
    return rx.vstack(
        title('Comunidad'),
        link_button('Instagram','Sigueme para mas contenido', 'https://www.instagram.com/elblockdemaria/'),
        link_button('Youtube', 'Sigueme para mas contenido','https://www.youtube.com/@elblockdemaria'),
        link_button('Youtube', 'Sigueme para mas contenido','https://www.youtube.com/@elblockdemaria'),
        width='100%',
        spacing=style.Spacer.SMALL.value
        
    )
    