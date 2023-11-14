"""Welcome to Reflex!."""

from test_project import styles

# Import all the pages.
from test_project.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
