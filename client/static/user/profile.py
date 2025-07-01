from fasthtml.common import Style

def profile_styles():
    """Additional styles for profile page"""
    return Style("""
        .row {
            display: flex;
            flex-wrap: wrap;
            margin: 0 -0.5rem;
        }
        
        .col-12 {
            flex: 0 0 100%;
            max-width: 100%;
            padding: 0 0.5rem;
        }
        
        .col-md-4 {
            flex: 0 0 33.333333%;
            max-width: 33.333333%;
            padding: 0 0.5rem;
        }
        
        .col-md-8 {
            flex: 0 0 66.666667%;
            max-width: 66.666667%;
            padding: 0 0.5rem;
        }
        
        @media (max-width: 768px) {
            .col-md-4, .col-md-8 {
                flex: 0 0 100%;
                max-width: 100%;
                margin-bottom: 1rem;
            }
        }
        
        article {
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        article:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .modal-overlay {
            backdrop-filter: blur(2px);
            animation: fadeIn 0.3s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        form label {
            margin-bottom: 0.5rem;
            font-weight: 600;
        }
        
        form input, form select {
            margin-bottom: 1rem;
        }
        
        .profile-avatar {
            background-color: var(--primary);
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }
        
        .profile-avatar:hover {
            transform: scale(1.05);
        }
                 
        .profile-header-text {
            color: white;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }
    """)