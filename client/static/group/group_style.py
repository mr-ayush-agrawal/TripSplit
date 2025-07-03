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

                 
        .add-members-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .add-members-header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .add-members-form {
            background: var(--card-bg, #2a2a2a);
            color: var(--text-color, #ffffff);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            border: 1px solid var(--border-color, #404040);
            margin-bottom: 30px;
        }
        
        .form-label {
            color: var(--text-color, #ffffff);
            font-weight: 500;
            margin-bottom: 8px;
            display: block;
        }
        
        .form-textarea {
            width: 100%;
            min-height: 100px;
            padding: 12px;
            border: 2px solid var(--border-color, #404040);
            border-radius: 8px;
            font-family: inherit;
            font-size: 14px;
            resize: vertical;
            transition: border-color 0.3s ease;
            background: var(--input-bg, #1a1a1a);
            color: var(--text-color, #ffffff);
        }
        
        .form-textarea::placeholder {
            color: var(--placeholder-color, #888888);
        }
        
        .form-textarea:focus {
            outline: none;
            border-color: var(--primary-color, #007bff);
            background: var(--input-focus-bg, #252525);
        }
        
        .form-help {
            font-size: 12px;
            color: var(--muted-text, #888888);
            margin-bottom: 8px;
        }
        
        .form-actions {
            display: flex;
            gap: 12px;
            justify-content: flex-end;
            margin-top: 20px;
        }
        
        .btn {
            padding: 10px 20px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid transparent;
            display: inline-block;
            text-align: center;
            height: 40px;
            line-height: 18px;
            box-sizing: border-box;
        }
        
        .btn-primary {
            background: var(--primary-color, #007bff);
            color: white;
            border-color: var(--primary-color, #007bff);
        }
        
        .btn-primary:hover {
            background: var(--primary-hover, #0056b3);
            border-color: var(--primary-hover, #0056b3);
        }
        
        .btn-secondary {
            background: transparent;
            color: var(--danger-color, #dc3545);
            border-color: var(--danger-color, #dc3545);
        }
        
        .btn-secondary:hover {
            background: var(--danger-color, #dc3545);
            color: white;
        }
        
        .btn-success {
            background: var(--success-color, #28a745);
            color: white;
            border-color: var(--success-color, #28a745);
        }
        
        .btn-success:hover {
            background: var(--success-hover, #218838);
            border-color: var(--success-hover, #218838);
        }
        
        .finish-group-action {
            margin-top: 20px;
            text-align: center;
        }
        
        .existing-members-section {
            background: var(--card-bg, #2a2a2a);
            color: var(--text-color, #ffffff);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            border: 1px solid var(--border-color, #404040);
            margin-bottom: 20px;
        }
        
        .section-title {
            color: var(--text-color, #ffffff);
            margin-bottom: 16px;
        }
        
        .members-list {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 12px;
        }
        
        .member-item {
            background: var(--primary-color, #007bff);
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 14px;
        }
        
        .add-members-info {
            background: var(--info-bg, #1a2332);
            color: var(--text-color, #ffffff);
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid var(--primary-color, #007bff);
        }
        
        .info-list {
            margin-top: 12px;
        }
        
        .info-list li {
            margin-bottom: 8px;
            color: var(--muted-text, #cccccc);
        }
        
        .alert {
            padding: 12px 16px;
            border-radius: 6px;
            margin-bottom: 20px;
        }
        
        .alert-success {
            background-color: var(--success-bg, #1e4d2b);
            color: var(--success-color, #4caf50);
            border: 1px solid var(--success-border, #4caf50);
        }
        
        .alert-error {
            background-color: var(--error-bg, #4a1e1e);
            color: var(--error-color, #f44336);
            border: 1px solid var(--error-border, #f44336);
        }
        
        @media (max-width: 768px) {
            .add-members-container {
                padding: 15px;
            }
            
            .add-members-form {
                padding: 20px;
            }
            
            .form-actions {
                flex-direction: column;
            }
            
            .members-list {
                justify-content: center;
            }
        }   
    """)
