from fasthtml.common import *

# def login_form():
    # return Form(
    #     H2("Login"),
    #     Label("Email", Input(type="email", name="email", required=True, placeholder="Enter your email")),
    #     Label("Password", Input(type="password", name="password", required=True, placeholder="Enter your password")),
    #     Button("Login", type="submit"),
    #     P(A("Don't have an account? Sign up", href="/user/signup")),
    #     method="post",
    #     action="/user/login"
    # )

def login_form():
    return Body(
            Main(
                Section(
                    Form(
                        H2("Login"),

                        # Switch Toggle between Email and Username
                        Div(
                            Label("Email", For="loginSwitch"),
                            Input(type="checkbox", role="switch", id="loginSwitch", onchange="updateLoginType()"),
                            Label("Username", For="loginSwitch"),
                            cls="grid",
                            style="grid-template-columns: auto auto auto; align-items: center; gap: 1rem; margin-bottom: 1rem;"
                        ),

                        # Dynamic Input Field (initially email)
                        Div(
                            Label("Email", id="loginLabel"),
                            Input(type="email", name="identifier", placeholder="Enter your email", required=True, id="loginInput"),
                            id="inputContainer"
                        ),

                        Label("Password"),
                        Input(type="password", name="password", placeholder="Enter your password", required=True),

                        Button("Login", type="submit", cls="contrast"),

                        P(A("Don't have an account? Sign up", href="/user/signup")),

                        method="post",
                        action="/user/login"
                    )
                )
            ),

            Script(
                """
                function updateLoginType() {
                    const toggle = document.getElementById('loginSwitch');
                    const input = document.getElementById('loginInput');
                    const label = document.getElementById('loginLabel');

                    if (toggle.checked) {
                        label.innerText = 'Username';
                        input.placeholder = 'Enter your username';
                        input.type = 'text';
                    } else {
                        label.innerText = 'Email';
                        input.placeholder = 'Enter your email';
                        input.type = 'email';
                    }
                }
                """
            )
        )


def signup_form():
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
        Label('Currency', Select(*[curr_opt for curr_opt in curr_list], name = 'currency', id= 'currency')),
        Button("Sign Up", type="submit"),
        P(A("Already have an account? Login", href="/user/login")),
        method="post",
        action="/user/signup"
    )