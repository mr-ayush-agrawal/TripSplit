from fasthtml.common import *



def signup_form(error_message=None):
    curr_list = [
        Option('INR', value = 'INR'),
        Option('USD', value = 'USD'),
        Option('EUR', value = 'EUR'),
        Option('AED', value = 'AED')
    ]
    return Form(
        H2("Create Account"),
        Label("Name", Input(type="text", name="name", required=True, placeholder="Enter your name")),
        Label("Email", Input(type="email", name="email", required=True, placeholder="Enter your email")),
        Label("Username", Input(type="text", name="user_name", required=True, placeholder="Enter a unique username")),
        Label("Password", Input(type="password", name="password", required=True, placeholder="Create a password")),
        Label("Re-Enter Password", Input(type="password", name="re_password", required=True, placeholder="Re-enter the password")),
        Label('Currency', Select(*[curr_opt for curr_opt in curr_list], name = 'currency', id= 'currency')),
        Button("Sign Up", type="submit"),
        P(A("Already have an account? Login", href="/user/login")),
        Div(error_message, cls="error-message") if error_message else None,
        method="post",
        action="/user/signup"
    )

def login_toggle():
    return Div(
        Label("Email", For="loginSwitch"),
        Input(type="checkbox", role="switch", id="loginSwitch", onchange="updateLoginType()"),
        Label("Username", For="loginSwitch"),
        cls="grid",
        style="grid-template-columns: auto auto auto; align-items: left; gap: 1rem; margin-bottom: 1rem;"
    )

def login_fields():
    return Div(
        Label("Email", id="loginLabel"),
        Input(type="email", name="email", placeholder="Enter your email", required=True, id="loginInput"),  # ✅ name changed from identifier to email
        id="inputContainer"
    )

def login_script():
    return Script(
        """
        function updateLoginType() {
            const toggle = document.getElementById('loginSwitch');
            const input = document.getElementById('loginInput');
            const label = document.getElementById('loginLabel');

            if (toggle.checked) {
                label.innerText = 'Username';
                input.placeholder = 'Enter your username';
                input.type = 'text';
                input.name = 'user_name';  // ✅ updated for FastAPI
            } else {
                label.innerText = 'Email';
                input.placeholder = 'Enter your email';
                input.type = 'email';
                input.name = 'email';  // ✅ updated for FastAPI
            }
        }
        """
    )


def login_form(error_message=None):
    return Form(
        H2("Login"),
        login_toggle(),
        login_fields(),
        Label("Password"),
        Input(type="password", name="password", placeholder="Enter your password", required=True),
        Button("Login", type="submit", cls="contrast"),
        P(A("Don't have an account? Sign up", href="/user/signup")),
        Div(error_message, cls="error-message") if error_message else None,
        method="post",
        action="/user/login"
    )