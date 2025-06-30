from client.components.auth.layout import auth_layout
from client.components.auth.form import login_form, signup_form, login_script
from client.components.home.layout import home_base_layout

def login_page(error_message = None):
    content = auth_layout("Login", login_form(error_message), script = login_script())
    return home_base_layout(title='Login', content = content, nav_auth_button=False)

def signup_page(error_message = None):
    content =  auth_layout("Sign Up", signup_form(error_message))
    return home_base_layout(title='Signup', content = content, nav_auth_button=False)

