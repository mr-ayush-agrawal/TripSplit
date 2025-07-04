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
                 

        .single-group-container {
            max-width: 100%;
            margin: 0 auto;
            padding: 1rem;
        }
        
        .group-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #e9ecef;
        }
        
        .group-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #2c3e50;
            margin: 0;
        }
        
        .group-description {
            color: #6c757d;
            margin: 8px 0 0 0;
            font-size: 1.1rem;
        }
        
        .group-actions {
            display: flex;
            gap: 12px;
        }
        
        .group-layout {
            display: grid;
            # grid-template-columns: 1fr 320px;
            grid-template-columns: 2fr 320px;
            gap: 30px;
        }
        
        .main-content {
            min-width: 0;
        }
        
        .sidebar {
            position: sticky;
            top: 20px;
            height: fit-content;
        }
        
    
        /* Group Stats */
        .group-stats-section {
            margin-bottom: 40px;
        }
        
        .section-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
            gap: 20px;
        }
        
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            padding: 24px;
            color: white;
            display: flex;
            align-items: center;
            gap: 16px;
            transition: transform 0.2s ease;
        }
        
        .stat-card:hover {
            transform: translateY(-2px);
        }
        
        .stat-icon {
            font-size: 2rem;
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: 700;
        }
        
        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
        }
        
        /* Members Section */
        .members-section {
            # background: var(--card-bg, #2a2a2a);
            # background: #f8f9fa;
            color: var(--text-color, #ffffff);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .members-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        
        .members-count {
            color: #6c757d;
            font-size: 0.9rem;
        }
        
        .members-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .member-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px;
            background: #f8f9fa;
            border-radius: 8px;
            transition: background-color 0.2s ease;
        }
        
        .member-item:hover {
            background: #e9ecef;
            # background: var(--hover-bg, #2d2d2d);
            colour : #fff;
        }
        
        .member-name {
            font-weight: 600;
            color: #2c3e50;
        }
        
        .member-role {
            font-size: 0.8rem;
            color: #f39c12;
            margin-top: 2px;
        }
        
        .member-balance {
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        .balance-positive {
            color: #27ae60;
        }
        
        .balance-negative {
            color: #e74c3c;
        }
        
        .balance-zero {
            color: #6c757d;
        }
        
        .member-actions {
            display: flex;
            gap: 8px;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #e9ecef;
        }
        
        /* Expenses Section */
        .expenses-section {
            # background: var(--card-bg, #2a2a2a);
            background: #001018;
            color: var(--text-color, #ffffff);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .expenses-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        
        .user-balance-summary {
            font-size: 1.1rem;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 20px;
            background: #f8f9fa;
        }
        
        .net-positive {
            color: #27ae60;
            background: #d4edda;
        }
        
        .net-negative {
            color: #e74c3c;
            background: #f8d7da;
        }
        
        .net-zero {
            color: #6c757d;
        }
        
        .expenses-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .expense-card {
            display: block;
            text-decoration: none;
            color: inherit;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .expense-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        
        .expense-card-inner {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 16px;
            border-left: 4px solid #007bff;
        }
        
        .expense-content {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        
        .expense-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
            margin: 0 0 4px 0;
        }
        
        .expense-description {
            color: #6c757d;
            font-size: 0.9rem;
            margin: 0 0 4px 0;
        }
        
        .expense-date {
            color: #adb5bd;
            font-size: 0.8rem;
            margin: 0;
        }
        
        .expense-amounts {
            text-align: right;
            flex-shrink: 0;
        }
        
        .expense-amount {
            font-size: 1.2rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 4px;
        }
        
        .expense-balance {
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        .expense-positive {
            color: #27ae60;
        }
        
        .expense-negative {
            color: #e74c3c;
        }
        
        .expense-zero {
            color: #6c757d;
        }
        
        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #6c757d;
        }
        
        .empty-icon {
            font-size: 4rem;
            margin-bottom: 20px;
        }
        
        .empty-title {
            font-size: 1.5rem;
            color: #495057;
            margin-bottom: 12px;
        }
        
        .empty-description {
            font-size: 1rem;
            margin-bottom: 30px;
        }
        
        /* Error Pages */
        .error-page {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 50vh;
        }
        
        .error-content {
            text-align: center;
            max-width: 500px;
            padding: 40px;
        }
        
        .error-title {
            font-size: 2rem;
            color: #e74c3c;
            margin-bottom: 16px;
        }
        
        .error-message {
            font-size: 1.1rem;
            color: #6c757d;
            margin-bottom: 30px;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .single-group-container {
                padding: 15px;
            }
            
            .group-header {
                flex-direction: column;
                gap: 20px;
                align-items: stretch;
            }
            
            .group-actions {
                justify-content: center;
                flex-wrap: wrap;
            }
            
            .group-layout {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .sidebar {
                position: static;
                order: -1;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
            
            .group-title {
                font-size: 2rem;
            }
            
            .expense-content {
                flex-direction: column;
                gap: 12px;
            }
            
            .expense-amounts {
                text-align: left;
            }
        }
        
        @media (max-width: 480px) {
            .group-actions {
                flex-direction: column;
            }
            
            .member-actions {
                flex-direction: column;
            }
        }
                 
        .btn-sm {
            font-size: 13px;
            padding: 6px 14px;
            height: auto;
            line-height: 1.4;
        }
    """)
