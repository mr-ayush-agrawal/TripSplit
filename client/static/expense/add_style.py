from fasthtml.common import Style

def add_expense_styles():
    """CSS styles for add expense page"""
    return Style("""
        .add-expense-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .add-expense-header {
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #404040;
        }
        
        .header-content h1 {
            color: #e0e0e0;
            margin: 10px 0;
        }
        
        .form-container {
            background: #1a1a1a;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 30px;
        }
        
        .expense-form {
            max-width: 90%;
            margin: 0 auto;
        }
        
        .form-content > div {
            margin-bottom: 30px;
        }
                 
        .form-content {
            display: flex;
            flex-direction: column;  
            gap: 30px;
        }
                 
        .form-split-row {
            display: flex;
            gap: 30px;
        }

        .expense-paid-by, .expense-split-by {
            flex: 1;
        }
                 
        .form-row {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }

        .form-group {
            flex: 1;
            min-width: 200px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #e0e0e0;
            font-weight: 600;
        }
                 
        .form-group input{
            height: 38px; /* for title */
            font-size: 14px;
        }

        .form-group input, .form-group select{
            width: 100%;
            padding: 10px;
            border: 1px solid #404040;
            border-radius: 4px;
            font-size: 14px;
            font-family: inherit;
            background: #2d2d2d;
            color: #f1f1f1;
            box-sizing: border-box;
        }
        
        .form-group input:focus, .form-group select:focus{
            outline: none;
            border-color: #007bff;
            box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
        }
        
        .help-text {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
            display: block;
        }
        
        .exchange-rate-group.hidden {
            display: none;
        }
        
        .mode-toggle, .split-mode-toggle {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .mode-btn, .split-btn {
            padding: 6px 12px; /* Slightly smaller */
            font-size: 14px;   /* Uniform text size */
            line-height: 1.2;  /* Fix vertical centering */
            border: 1px solid #404040;
            background: #2d2d2d;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .mode-btn.active, .split-btn.active {
            background: #007bff;
            color: white;
            border-color: #007bff;
        }
        
        .mode-btn:hover, .split-btn:hover {
            background: #2d2d2d;
        }
        
        .mode-btn.active:hover, .split-btn.active:hover {
            background: #0056b3;
        }
        
        .payer-section.hidden, .split-section.hidden {
            display: none;
        }
        
        .split-section .member-input {
            display: flex;
            flex-direction: row;  /* switch from column to row */
            align-items: center;
            gap: 10px;
        }
                 
        .expense-paid-by, .expense-split-by {
            flex: 1;
        }

        .member-inputs {
            display: flex;
            flex-direction: column; /* stack members vertically */
            gap: 15px;
        }
        
        .member-input {
            width: 100%;
            display: flex;
            align-items: center;
            gap: 30px; /* increased from 10px to 16px for better spacing */
        }
        
        .member-input label {
            flex: 0 0 120px;  /* same width for all labels */
            font-weight: 500;
            color: #e0e0e0;
            min-width: 100px;
        }
        
        .member-input input {
            flex: 1;
            padding: 6px 10px;   /* reduced vertical padding */
            height: 32px;        /* reduce height from default 38px */
            border: 1px solid #404040;
            border-radius: 4px;
            font-size: 14px;
            background: #2d2d2d;
            color: #f1f1f1;
            font-family: inherit;
        }
        
        .form-group-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #404040;
            border-radius: 4px;
            font-size: 14px;
            background: #2d2d2d;
            color: #f1f1f1;
            font-family: inherit;
        }

        .percent-input {
            position: relative;
        }
        
        .percent-symbol {
            position: absolute;
            right: 10px;
            color: #666;
        }
        
        .checkbox-group {
            display: flex;
            flex-direction: column; /* changed from wrap to list */
            gap: 10px;
        }
        
        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            color: #e0e0e0;
        }
        
        .checkbox-item input[type="checkbox"] {
            width: 18px;
            height: 18px;
        }
        
        .total-display {
            background: #2d2d2d; /* Dark background */
            color: #f1f1f1;
            border: 1px solid #404040;
        }
        
        .total-label {
            font-weight: 500;
        }
        
        .total-value {
            font-weight: bold;
            color: #007bff;
        }
        
        .form-actions {
            display: flex;
            gap: 15px;
            justify-content: center;
            margin-top: 30px;
        }
        
        .submit-btn, .cancel-btn {
            padding: 12px 30px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .submit-btn {
            background: #198754;
            color: white;
        }
        
        .submit-btn:hover {
            background: #218838;
        }
        
        .cancel-btn {
            background: #495057;
            color: white;
        }
        
        .cancel-btn:hover {
            background: #5a6268;
        }
        
        .popup-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
        }
        
        .popup-overlay.hidden {
            display: none;
        }
        
        .popup-modal {
            background: #2d2d2d;
            border-radius: 8px;
            max-width: 400px;
            width: 90%;
        }
        
        .popup-content {
            padding: 30px;
            text-align: center;
        }
        
        .popup-content h3 {
            margin-bottom: 15px;
            color: #e0e0e0;
        }
        
        .popup-content p {
            margin-bottom: 20px;
            color: #b0b0b0;
        }
        
        .popup-btn {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        .popup-btn:hover {
            background: #0056b3;
        }
        
        @media (max-width: 768px) {
            .form-row {
                flex-direction: column;
                gap: 0;
            }
            
            .member-inputs {
                grid-template-columns: 1fr;
            }
            
            .mode-toggle, .split-mode-toggle {
                 display: flex;
                gap: 10px;
                margin-bottom: 15px;
                flex-wrap: wrap; /* Helps with small screens */
            }
            
            .form-actions {
                flex-direction: column;
                align-items: center;
            }
                 
            .form-split-row {
                flex-direction: column;
            }
        }
                 
        .back-btn {
            display: inline-block;
            padding: 6px 12px;
            background: #444;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-weight: 500;
            transition: background 0.2s;
            font-size: 14px;
        }

        .back-btn:hover {
            background: #0056b3;
            text-decoration: none;
        }

        .header-content h1 {
            color: #ffffff;  /* Change from #333 to #ffffff */
            margin: 10px 0;
            font-size: 24px;
            font-weight: 600;
        }
    """)
