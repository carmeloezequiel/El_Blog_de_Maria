"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from El_Blog_de_Maria.components.navbar import navbar
from El_Blog_de_Maria.components.footer import footer
from El_Blog_de_Maria.views.header.header import header
from El_Blog_de_Maria.views.links.links import links
import El_Blog_de_Maria.styles.styles as styles


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        #navbar(),
        rx.center(
        rx.vstack(
        header(),
        links(), 
        max_width=styles.MAX_WIDTH,
        width='100%',
        margin_y=styles.Spacer.BIG
    )),
        footer()
    )
    

app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)
