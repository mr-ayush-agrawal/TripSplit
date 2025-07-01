from fasthtml.common import *
from client.components.user.cards import profile_info_card, profile_stats_card, password_change_card

def profile_header(name, username):
    """Profile header with user avatar and basic info"""
    return Section(
        Div(
            Div(
                Div(
                    # Profile Avatar (using initials)
                    Div(
                        Span(name[0].upper() if name else "U", 
                            style="font-size: 3rem; font-weight: bold; color: white; text-shadow: 1px 1px 3px rgba(0,0,0,0.6);"),
                        style="width: 100px; height: 100px; border-radius: 50%; background: var(--primary); display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);"
                    ),
                    H2(name, style="text-align: center; margin-bottom: 0.5rem; color: white;"),
                    P(f"@{username}", style="text-align: center; color: #ddd; font-size: 1.1rem;"),
                ),
                cls="col-12"
            ),
            cls="row"
        ),
        style="""
            margin-bottom: 3rem;
            padding: 2rem 0;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: 1rem;
        """
    )


def profile_grid(personal_info, account_info, total_groups=0):
    """Main profile information grid"""
    return Div(
        Div(
            profile_info_card(
                title="Personal Information",
                fields=personal_info,
                edit_button_id="edit-personal",
                edit_modal_id="personal-info-modal"
            ),
            profile_info_card(
                title="Account Information", 
                fields=account_info,
                edit_button_id="edit-account",
                edit_modal_id="account-info-modal"
            ),
            cls="col-md-8"
        ),
        Div(
            *( [profile_stats_card(total_groups=total_groups)] if total_groups is not None else [] ),
            password_change_card(),
            cls="col-md-4"
        ),
        cls="row"
    )
