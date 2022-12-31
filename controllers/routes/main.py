from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    # at.TextBox22.styles._fontFamily="'IBM Plex Sans', sans-serif;"
    # at._TextBox15.styles={'weight':'bold'}
    # at.TextBox22.styles.color=['linear-gradient(108deg, #b16cea 8%, #ff5e69 40%, #ff8a56 77%, #ffa84b 91%)']
    # at.TextBox25.styles.color="#9D9D9D"
    # at.TextBox26.styles.color="#9D9D9D"
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass