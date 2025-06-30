from fasthtml.common import Style

def dropdown_styles():
    """CSS styles for the user dropdown"""
    return Style("""
        .dropdown-hover span {
            transition: background-color 0.3s ease;
        }
        
        .dropdown-hover span:hover {
            background: var(--primary-hover) !important;
        }
        
        .dropdown-hover ul {
            position: absolute;
            top: 100%;
            right: 0;
            background: white;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            min-width: 150px;
            z-index: 1000;
            margin-top: 0.5rem;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0.3s ease;
        }
        
        .dropdown-hover:hover ul {
            opacity: 1;
            visibility: visible;
        }
        
        .dropdown-hover ul li {
            margin: 0;
        }
        
        .dropdown-hover ul li a {
            display: block;
            padding: 0.75rem 1rem;
            text-decoration: none;
            color: var(--color);
            border-radius: 0;
        }
        
        .dropdown-hover ul li a:hover {
            background: var(--background-color);
        }
        
        .dropdown-hover ul li:first-child a {
            border-radius: 0.5rem 0.5rem 0 0;
        }
        
        .dropdown-hover ul li:last-child a {
            border-radius: 0 0 0.5rem 0.5rem;
        }
    """)