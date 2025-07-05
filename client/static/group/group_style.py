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
        
        /* Members Section - Dark Theme Fixed */
        .members-section {
            background: var(--card-bg, #2a2a2a);
            color: var(--text-color, #ffffff);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        .members-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .section-title {
            color: var(--text-color, #ffffff);
            margin: 0;
            font-size: 1.5rem;
            font-weight: 600;
        }

        .members-count {
            color: var(--text-muted, #adb5bd);
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
            background: var(--member-item-bg, #3a3a3a);
            border-radius: 8px;
            transition: background-color 0.2s ease;
            border: 1px solid var(--border-color, #4a4a4a);
        }

        .member-item:hover {
            background: var(--hover-bg, #4a4a4a);
            border-color: var(--accent-color, #007bff);
        }

        .member-info {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .member-name {
            font-weight: 600;
            color: var(--text-color, #ffffff);
            font-size: 1rem;
        }

        .member-role {
            font-size: 0.8rem;
            color: var(--accent-color, #ffc107);
            margin-top: 2px;
        }

        .member-balance-container {
            text-align: right;
        }

        .member-balance {
            font-size: 0.9rem;
            font-weight: 500;
        }

        .balance-positive {
            color: #28a745;
        }

        .balance-negative {
            color: #dc3545;
        }

        .balance-zero {
            color: var(--text-muted, #6c757d);
        }

        .member-actions {
            display: flex;
            gap: 8px;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color, #4a4a4a);
        }

        /* Expenses Section - Dark Theme Fixed */
        .expenses-section {
            background: var(--card-bg, #2a2a2a);
            color: var(--text-color, #ffffff);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        .expenses-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 12px;
        }

        .user-balance-summary {
            font-size: 1.1rem;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 20px;
            background: var(--summary-bg, #3a3a3a);
            border: 1px solid var(--border-color, #4a4a4a);
        }

        .net-balance {
            font-weight: 600;
        }

        .net-positive {
            color: #28a745;
            background: rgba(40, 167, 69, 0.1);
            border-color: rgba(40, 167, 69, 0.3);
        }

        .net-negative {
            color: #dc3545;
            background: rgba(220, 53, 69, 0.1);
            border-color: rgba(220, 53, 69, 0.3);
        }

        .net-zero {
            color: var(--text-muted, #6c757d);
            background: rgba(108, 117, 125, 0.1);
            border-color: rgba(108, 117, 125, 0.3);
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
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
        }

        .expense-card-inner {
            background: var(--expense-card-bg, #3a3a3a);
            border-radius: 8px;
            padding: 16px;
            border-left: 4px solid var(--accent-color, #007bff);
            border: 1px solid var(--border-color, #4a4a4a);
            border-left: 4px solid var(--accent-color, #007bff);
        }

        .expense-content {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 16px;
        }

        .expense-info {
            flex: 1;
            min-width: 0;
        }

        .expense-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-color, #ffffff);
            margin: 0 0 4px 0;
        }

        .expense-description {
            color: var(--text-muted, #adb5bd);
            font-size: 0.9rem;
            margin: 0 0 4px 0;
        }

        .expense-date {
            color: var(--text-muted, #6c757d);
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
            color: var(--text-color, #ffffff);
            margin-bottom: 4px;
        }

        .expense-balance {
            font-size: 0.9rem;
            font-weight: 500;
        }

        .expense-positive {
            color: #28a745;
        }

        .expense-negative {
            color: #dc3545;
        }

        .expense-zero {
            color: var(--text-muted, #6c757d);
        }

        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 40px 20px;
            color: var(--text-muted, #adb5bd);
        }

        .empty-icon {
            font-size: 3rem;
            margin-bottom: 16px;
            display: block;
        }

        .empty-title {
            color: var(--text-color, #ffffff);
            margin-bottom: 8px;
            font-size: 1.25rem;
        }

        .empty-description {
            color: var(--text-muted, #adb5bd);
            margin-bottom: 20px;
            font-size: 0.9rem;
        }        

        /* Responsive Design */
        @media (max-width: 768px) {
            .member-item {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
            
            .member-balance-container {
                text-align: left;
                width: 100%;
            }
            
            .expense-content {
                flex-direction: column;
                gap: 12px;
            }
            
            .expense-amounts {
                text-align: left;
            }
            
            .expenses-header {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .member-actions {
                flex-direction: column;
                gap: 8px;
            }
            
            .member-actions .btn {
                width: 100%;
                text-align: center;
            }
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
                 

                 
        /* Remove Members Page Styles - Dark Theme */
        .remove-members-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: var(--bg-color, #1a1a1a);
            color: var(--text-color, #ffffff);
            min-height: 100vh;
        }
        
        .remove-members-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-top: 30px;
        }
        
        @media (max-width: 768px) {
            .remove-members-content {
                grid-template-columns: 1fr;
                gap: 20px;
            }
        }
        
        .members-overview {
            display: grid;
            gap: 15px;
        }
        
        .member-card {
            background: var(--card-bg, #2d2d2d);
            border: 1px solid var(--border-color, #404040);
            border-radius: 8px;
            padding: 16px;
            transition: all 0.2s ease;
            color: var(--text-color, #ffffff);
        }
        
        .member-card:hover {
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            border-color: var(--accent-color, #007bff);
        }
        
        .member-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .member-name {
            font-weight: 600;
            font-size: 16px;
            color: var(--text-color, #ffffff);
        }
        
        .member-details {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 14px;
        }
        
        .badge {
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .badge-owner {
            background: #ffd700;
            color: #b8860b;
        }
        
        .badge-balance {
            background: #dc3545;
            color: #ffffff;
        }
        
        .badge-settled {
            background: #28a745;
            color: #ffffff;
        }
        
        .status-warning {
            color: #ffc107;
            font-size: 12px;
        }
        
        .status-success {
            color: #28a745;
            font-size: 12px;
        }
        
        .balance-positive {
            color: #28a745;
        }
        
        .balance-negative {
            color: #dc3545;
        }
        
        .balance-zero {
            color: #6c757d;
        }
        
        .remove-member-form {
            background: var(--card-bg, #2d2d2d);
            border: 1px solid var(--border-color, #404040);
            border-radius: 8px;
            padding: 24px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: var(--text-color, #ffffff);
        }
        
        .form-select {
            width: 100%;
            padding: 10px;
            border: 1px solid var(--border-color, #404040);
            border-radius: 4px;
            font-size: 14px;
            background: var(--input-bg, #1a1a1a);
            color: var(--text-color, #ffffff);
        }
        
        .form-select:focus {
            outline: none;
            border-color: var(--accent-color, #007bff);
            box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
        }
        
        .form-select option {
            background: var(--input-bg, #1a1a1a);
            color: var(--text-color, #ffffff);
        }
        
        .form-actions {
            display: flex;
            gap: 12px;
            margin-top: 20px;
        }
        
        .btn-danger {
            background: #dc3545;
            color: white;
            border: 1px solid #dc3545;
            padding: 10px 20px;
            border-radius: 4px;
            text-decoration: none;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s ease;
        }
        
        .btn-danger:hover {
            background: #c82333;
            border-color: #c82333;
        }
        
        .alert {
            padding: 12px 16px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
        
        .alert-success {
            background: rgba(40, 167, 69, 0.2);
            color: #28a745;
            border: 1px solid rgba(40, 167, 69, 0.3);
        }
        
        .alert-error {
            background: rgba(220, 53, 69, 0.2);
            color: #dc3545;
            border: 1px solid rgba(220, 53, 69, 0.3);
        }
        
        .alert-warning {
            background: rgba(255, 193, 7, 0.2);
            color: #ffc107;
            border: 1px solid rgba(255, 193, 7, 0.3);
        }
        
        .alert-info {
            background: rgba(23, 162, 184, 0.2);
            color: #17a2b8;
            border: 1px solid rgba(23, 162, 184, 0.3);
        }
        
        .no-removable-info {
            text-align: center;
            padding: 40px;
            color: var(--text-muted, #888);
        }
        
        .section-title {
            color: var(--text-color, #ffffff);
            margin-bottom: 20px;
            font-size: 18px;
            font-weight: 600;
        }
        
        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border-color, #404040);
        }
        
        .page-title {
            color: var(--text-color, #ffffff);
            margin: 0;
            font-size: 24px;
        }
        
        .page-subtitle {
            color: var(--text-muted, #888);
            margin: 5px 0 0 0;
            font-size: 14px;
        }
        
        .header-actions .btn {
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            transition: all 0.2s ease;
        }
        
        .btn-secondary {
            background: var(--btn-secondary-bg, #6c757d);
            color: white;
            border: 1px solid var(--btn-secondary-bg, #6c757d);
        }
        
        .btn-secondary:hover {
            background: var(--btn-secondary-hover, #5a6268);
            border-color: var(--btn-secondary-hover, #5a6268);
        }         

                         
    """)
