from fasthtml.common import Style

def edit_expense_styles():
    """Styles for edit expense page"""
    return Style("""
        .edit-expense-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .page-header {
            background: var(--card-background);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-light);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .header-left {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .back-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: var(--secondary-color);
            color: white;
            border-radius: 50%;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        
        .back-button:hover {
            background: var(--primary-color);
            transform: translateX(-2px);
        }
        
        .page-title {
            margin: 0;
            color: var(--text-primary);
            font-size: 24px;
            font-weight: 600;
        }
        
        .group-name {
            color: var(--text-secondary);
            font-size: 14px;
            background: var(--background-light);
            padding: 8px 12px;
            border-radius: 20px;
        }
        
        .form-container {
            background: var(--card-background);
            border-radius: 12px;
            padding: 30px;
            box-shadow: var(--shadow-light);
        }
        
        .expense-form {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }
        
        .form-section {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
        }
        
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .form-label {
            font-weight: 500;
            color: var(--text-primary);
            font-size: 14px;
        }
        
        .form-input, .form-select, .form-textarea {
            padding: 12px;
            border: 2px solid var(--border-light);
            border-radius: 8px;
            font-size: 14px;
            background: var(--background-light);
            color: var(--text-primary);
            transition: border-color 0.3s ease;
        }
        
        .form-input:focus, .form-select:focus, .form-textarea:focus {
            outline: none;
            border-color: var(--primary-color);
        }
        
        .form-textarea {
            resize: vertical;
            min-height: 80px;
        }
        
        .section-title {
            color: var(--text-primary);
            font-size: 18px;
            font-weight: 600;
            margin: 0 0 15px 0;
        }
        
        .members-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .member-input-group {
            display: grid;
            grid-template-columns: 1fr 120px auto;
            gap: 12px;
            align-items: center;
        }
        
        .remove-btn {
            padding: 8px 12px;
            background: var(--danger-color);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .remove-btn:hover {
            background: var(--danger-hover);
        }
        
        .add-member-btn {
            align-self: flex-start;
            padding: 10px 16px;
            background: var(--secondary-color);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .add-member-btn:hover {
            background: var(--secondary-hover);
        }
        
        .split-equally-btn {
            align-self: flex-start;
            padding: 10px 16px;
            background: transparent;
            color: var(--primary-color);
            border: 2px solid var(--primary-color);
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .split-equally-btn:hover {
            background: var(--primary-color);
            color: white;
        }
        
        .form-actions {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }
        
        .submit-btn {
            padding: 12px 24px;
            background: var(--primary-color);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .submit-btn:hover {
            background: var(--primary-hover);
        }
        
        .cancel-btn {
            padding: 12px 24px;
            background: var(--secondary-color);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 500;
            text-decoration: none;
            transition: background 0.3s ease;
        }
        
        .cancel-btn:hover {
            background: var(--secondary-hover);
        }
        
        @media (max-width: 768px) {
            .form-row {
                grid-template-columns: 1fr;
            }
            
            .member-input-group {
                grid-template-columns: 1fr;
                gap: 8px;
            }
            
            .form-actions {
                flex-direction: column;
            }
        }
    """)
