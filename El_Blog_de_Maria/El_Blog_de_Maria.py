"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from El_Blog_de_Maria.components.navbar import navbar
from El_Blog_de_Maria.components.footer import footer
from El_Blog_de_Maria.views.header.header import header
from El_Blog_de_Maria.views.links.links import links


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        navbar(),
        header(),
        links(), 
        footer()
    )

app = rx.App()
app.add_page(index)
