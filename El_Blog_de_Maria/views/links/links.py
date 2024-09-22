import reflex as rx 
from El_Blog_de_Maria.components.linkbutton import link_button
from El_Blog_de_Maria.components.title import title
import El_Blog_de_Maria.styles.styles as style


def links() -> rx.Component:
    return rx.vstack(
        title('Comunidad'),
        link_button('Instagram','Carrusels y reels semanales', style.Url.INSTAGRAM.value),
        link_button('Youtube', 'Contenido exclusivo, ¡no te lo pierdas!',style.Url.YOUTUBE.value),
        link_button('TikTok', 'Risas, creatividad y diversión',style.Url.TIKTOK.value),
        width='100%',
        spacing=style.Spacer.SMALL.value
        
    )
    