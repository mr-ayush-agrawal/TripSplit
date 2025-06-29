from client.components.layout import auth_layout
from client.components.auth.form import login_form, signup_form
from client.components.home.layout import home_base_layout

def login_page():
    content = auth_layout("Login", login_form())
    return home_base_layout(title='Login', content = content, nav_auth_button=False)

def signup_page():
    content =  auth_layout("Sign Up", signup_form())
    return home_base_layout(title='Signup', content = content, nav_auth_button=False)

