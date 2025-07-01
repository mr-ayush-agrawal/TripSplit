from fasthtml.common import *

def logout_modal():
    """Logout confirmation modal"""
    return Div(
        Div(
            Article(
                Header(
                    H3("Confirm Logout", style="margin: 0; text-align: center;"),
                    style="border-bottom: 1px solid var(--border-color); margin-bottom: 1.5rem;"
                ),
                P("Are you sure you want to logout?", style="text-align: center; margin: 1.5rem 0;"),
                Footer(
                    Div(
                        Button(
                            "Cancel", 
                            type="button", 
                            cls="outline", 
                            onclick="hideLogoutModal()", 
                            style="width: 120px; height: 60px;"
                        ),
                        Button(
                            "Logout",
                            type="button",
                            onclick="window.location.href='/user/logout'",
                            style="background-color: #dc3545; border: 1px solid #dc3545; color: white; width: 120px; height: 60px; border-radius: 0.5rem;"
                        ),
                        style="display: flex; justify-content: center; gap: 1rem;"
                    ),
                    style="display: flex; justify-content: center; gap: 1.5rem;"
                ),
                style="max-width: 550px; width: 90%; margin: 0 auto; position: relative;"
            ),
            style="display: flex; align-items: center; justify-content: center; height: 100vh; padding: 2rem;"
        ),
        id="logoutModal",
        style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999;",
        onclick="if(event.target.id === 'logoutModal') hideLogoutModal()"
    )