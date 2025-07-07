from fasthtml.common import Style

def simplified_debts_styles():
    """CSS styles for simplified debts page"""
    return Style("""
        .simplified-debts-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #1a202c;
            color: #e2e8f0;
        }
        
        .simplified-debts-header {
            background: linear-gradient(135deg, #4a5568 0%, #2d3748 100%);
            color: white;
            padding: 1rem 2rem 2rem 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            position: relative;
            border-bottom: 2px solid #404040;
        }
        
        .header-content {
            display: flex;
            align-items: center;
            gap: 1rem;
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
                 
        .header-title {
            margin-top: 1rem;
        }
                 
        .header-title h1 {
            margin: 0;
        }
        
        .simplified-debts-content {
            display: grid;
            gap: 2rem;
        }
        
        .summary-section {
            background: #2d3748;
            color: #e2e8f0;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .summary-section h2 {
            margin-bottom: 1rem;
            color: #e2e8f0;
        }
        
        .summary-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }
        
        .summary-card {
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
        }
        
        .owe-card {
            background: linear-gradient(135deg, #ff6b6b, #ee5a52);
            color: white;
        }
        
        .receive-card {
            background: linear-gradient(135deg, #51cf66, #40c057);
            color: white;
        }
        
        .summary-card h3 {
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }
        
        .summary-card p {
            margin: 0;
            opacity: 0.9;
        }
        
        .payments-section {
            background: #2d3748;
            color: #e2e8f0;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .payments-section h2 {
            margin-bottom: 1.5rem;
            color: #e2e8f0;
        }
        
        .payments-list {
            display: grid;
            gap: 1rem;
        }
        
        .payment-item {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1rem;
            transition: all 0.3s;
            background: #2d3748;
            border-color: #4a5568;
            color: #e2e8f0;
        }
                 
        .count-card {
            background: linear-gradient(135deg, #3182ce, #2c5282);
            color: white;
        }
                 
        .settled-card {
            background: linear-gradient(135deg, #4a5568, #2d3748);
            color: white;
        }
        
        .payment-item:hover {
            border-color: #cbd5e0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        
        .user-involved {
            border-color: #63b3ed;
            background: #1a365d;
        }
        
        .payment-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
        }
        
        .payment-info {
            flex: 1;
        }
        
        .payment-parties {
            font-size: 1rem;
            margin-bottom: 0.5rem;
        }
        
        .payment-amount {
            font-size: 1.2rem;
            font-weight: 600;
            color: #e2e8f0;
        }
        
        .settle-button {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 6px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            min-width: 120px;
            text-decoration: none;        /* NEW */
            display: inline-block;        /* NEW */
            text-align: center;          /* NEW */
        }
        
        .pay-button {
            background: #ff6b6b;
            color: white;
        }
        
        .pay-button:hover {
            background: #ee5a52;
            transform: translateY(-1px);
        }
        
        .receive-button {
            background: #51cf66;
            color: white;
        }
        
        .receive-button:hover {
            background: #40c057;
            transform: translateY(-1px);
        }
        
        .payment-spacer {
            width: 120px;
        }
        
        .no-payments {
            text-align: center;
            padding: 3rem;
            color: #a0aec0;
        }
        
        .no-payments p {
            font-size: 1.2rem;
            margin: 0;
        }
        
        @media (max-width: 768px) {
            .simplified-debts-container {
                padding: 1rem;
            }
            
            .payment-content {
                flex-direction: column;
                align-items: stretch;
                gap: 1rem;
            }
            
            .settle-button {
                width: 100%;
            }
            
            .payment-spacer {
                display: none;
            }
        }
    """)
