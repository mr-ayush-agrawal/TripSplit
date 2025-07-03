from fasthtml.common import Style

def groups_styles():
    """CSS styles for groups pages"""
    return Style("""
                 
        .full-width-wrapper {
        width: 100%;
        max-width: 100%;
        margin-left: auto;
        margin-right: auto;
        }

        .row {
            display: flex;
            flex-wrap: wrap;
            margin: 0 -0.5rem;
        }
        
        .col-md-4 {
            flex: 0 0 33.333333%;
            max-width: 33.333333%;
            padding: 0 0.5rem;
            margin-bottom: 1rem;
        }
        
        .col-md-6 {
            flex: 0 0 50%;
            max-width: 50%;
            padding: 0 0.5rem;
        }
        
        .col-sm-6 {
            flex: 0 0 50%;
            max-width: 50%;
        }
        
        @media (max-width: 768px) {
            .col-md-4, .col-md-6 {
                flex: 0 0 100%;
                max-width: 100%;
            }
            .col-sm-6 {
                flex: 0 0 100%;
                max-width: 100%;
            }
        }
        
        @media (max-width: 576px) {
            .col-sm-6 {
                flex: 0 0 100%;
                max-width: 100%;
            }
        }
        
        article {
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        article:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        /* Create group card special styling */
        article[style*="dashed"]:hover {
            border-color: var(--primary-hover);
            background: var(--background-color);
        }
        
        /* Balance styling */
        .balance-positive {
            color: var(--success-color, #28a745);
        }
        
        .balance-negative {
            color: var(--danger-color, #dc3545);
        }
        
        .balance-zero {
            color: var(--success-color, #28a745);
        }
        
        /* Form styling */
        form {
            background: white;
            border-radius: 0.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        /* Steps indicator */
        .steps-indicator {
            margin-bottom: 3rem;
        }
        
        .step-active {
            background: var(--primary) !important;
            color: white !important;
        }
        
        .step-inactive {
            background: var(--muted-color) !important;
            color: white !important;
        }
                 

        .group-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
            width: 100%;
        }

        .group-left {
            flex: 1;
            min-width: 180px;
        }

        .group-center {
            flex: 1;
            text-align: center;
            min-width: 120px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            line-height: 1.4;
        }

        .group-right {
            flex: 1;
            text-align: right;
            display: flex;
            justify-content: flex-end;
            gap: 0.5rem;
            min-width: 150px;
            flex-wrap: wrap;
        }

        .group-right a[role="button"] {
            padding: 0.35rem 1rem;
            font-size: 0.85rem;
            min-width: 80px;
            border-radius: 6px;
        }

        .group-footer {
            margin-top: 0.5rem;
        }
                 
    """)
