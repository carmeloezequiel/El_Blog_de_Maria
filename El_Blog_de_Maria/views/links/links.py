import reflex as rx 
from El_Blog_de_Maria.components.linkbutton import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button('Instagram', 'https://www.instagram.com/elblockdemaria/'),
        link_button('Youtube', 'https://www.youtube.com/@elblockdemaria'),
        link_button('TikTok', 'https://www.youtube.com/@elblockdemaria')
        
    )