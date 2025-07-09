from fasthtml.common import *

def error_message_div(error: str):
    """Display error message"""
    if not error:
        return None
    return Div(
        error,
        cls="alert alert-danger",
        style="margin-bottom: 1rem; padding: 1rem; background-color: #f8d7da; color: #721c24; border-radius: 4px;"
    )
