from fasthtml.common import Style

def expense_detail_styles():
    """
    CSS styles for the expense detail page - Dark theme
    """
    return Style("""
        .expense-detail-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #1a1a1a;
            color: #e0e0e0;
            min-height: 100vh;
        }
        
        .back-button {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 6px;
            text-decoration: none;
            margin-bottom: 20px;
            font-size: 14px;
            font-weight: 500;
        }
        
        .back-button:hover {
            text-decoration: none;
        }
        
        .expense-header {
            margin-bottom: 30px;
        }
        
        .expense-header-content {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 20px;
        }
        
        .expense-header-left {
            flex: 1;
        }
        
        .expense-header-right {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 15px;
        }
        
        .expense-title {
            font-size: 2.2rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 10px;
        }
        
        .expense-description {
            color: #b0b0b0;
            font-size: 1.1rem;
            margin-bottom: 15px;
        }
        
        .expense-meta {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 0.95rem;
        }
        
        .label {
            color: #b0b0b0;
            font-weight: 500;
        }
        
        .expense-owner {
            color: #4a9eff;
            font-weight: 600;
        }
        
        .expense-actions-inline {
            display: flex;
            gap: 10px;
        }
        
        .btn-action-inline {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            font-size: 0.9rem;
            font-weight: 500;
            border-radius: 6px;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        
        .btn-action-inline:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            text-decoration: none;
        }
        
        .card {
            background: #2d2d2d;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            margin-bottom: 25px;
            border: 1px solid #404040;
        }
        
        .card-header {
            background: #333333;
            border-bottom: 1px solid #404040;
            padding: 20px;
            border-radius: 12px 12px 0 0;
        }
        
        .card-title {
            margin: 0;
            font-size: 1.4rem;
            font-weight: 600;
            color: #ffffff;
        }
        
        .card-body {
            padding: 25px;
        }
        
        .summary-content {
            display: flex;
            gap: 20px;
        }
        
        .amount-item {
            flex: 1;
            text-align: center;
            padding: 20px;
            background: #3a3a3a;
            border-radius: 8px;
            border: 1px solid #404040;
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 120px;
        }
        
        .amount-label {
            display: block;
            font-size: 0.9rem;
            color: #b0b0b0;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        .amount-display {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 5px;
        }
        
        .amount-primary {
            font-size: 1.8rem;
            font-weight: 700;
            color: #ffffff;
        }
        
        .amount-secondary {
            font-size: 0.85rem;
            color: #b0b0b0;
        }
        
        .members-table {
            margin-bottom: 0;
            background: transparent;
        }
        
        .table-header th {
            background: #333333;
            font-weight: 600;
            color: #ffffff;
            border-bottom: 2px solid #404040;
            padding: 15px;
            text-align: center;
        }
        
        .member-col {
            text-align: left !important;
        }
        
        .member-row {
            background: #2d2d2d;
            border-bottom: 1px solid #404040;
        }
        
        .member-row:hover {
            background: #3a3a3a;
        }
        
        .member-row td {
            padding: 15px;
            vertical-align: middle;
            border-color: #404040;
        }
        
        .member-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .member-icon {
            color: #4a9eff;
            font-size: 1.2rem;
        }
        
        .member-name {
            font-weight: 500;
            color: #ffffff;
        }
        
        .amount-cell {
            text-align: center;
        }
        
        .amount-paid {
            color: #28a745;
            font-weight: 600;
        }
        
        .amount-borrowed {
            color: #dc3545;
            font-weight: 600;
        }
        
        .amount-net {
            font-weight: 700;
            font-size: 1.05rem;
        }
        
        .amount-zero {
            color: #6c757d;
            font-style: italic;
        }
        
        .balance-cell {
            text-align: center;
        }
        
        .balance-status {
            display: block;
            font-size: 0.8rem;
            color: #b0b0b0;
            margin-top: 2px;
        }
        
        .non-involved-section {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #404040;
        }
        
        .non-involved-title {
            color: #b0b0b0;
            font-size: 1.1rem;
            margin-bottom: 15px;
        }
        
        .non-involved-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .non-involved-member {
            display: flex;
            align-items: center;
            gap: 5px;
            background: #3a3a3a;
            padding: 8px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
            color: #b0b0b0;
            border: 1px solid #404040;
        }
        
        .text-success {
            color: #28a745 !important;
        }
        
        .text-danger {
            color: #dc3545 !important;
        }
        
        .text-muted {
            color: #6c757d !important;
        }
        
        .btn-secondary {
            background-color: #6c757d;
            border-color: #6c757d;
            color: #ffffff;
        }
        
        .btn-secondary:hover {
            background-color: #5a6268;
            border-color: #545b62;
            color: #ffffff;
        }
        
        .btn-primary {
            background-color: #007bff;
            border-color: #007bff;
            color: #ffffff;
        }
        
        .btn-primary:hover {
            background-color: #0056b3;
            border-color: #004085;
            color: #ffffff;
        }
        
        .btn-danger {
            background-color: #dc3545;
            border-color: #dc3545;
            color: #ffffff;
        }
        
        .btn-danger:hover {
            background-color: #c82333;
            border-color: #bd2130;
            color: #ffffff;
        }
        
        @media (max-width: 768px) {
            .expense-detail-container {
                padding: 15px;
            }
            
            .expense-header-content {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .expense-header-right {
                width: 100%;
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
            
            .expense-title {
                font-size: 1.8rem;
            }
            
            .summary-content {
                flex-direction: column;
                gap: 15px;
            }
            
            .expense-actions-inline {
                flex-direction: column;
            }
            
            .table-responsive {
                font-size: 0.9rem;
            }
        }

        .exchange-rate-display {
            font-size: 1.3rem;
            font-weight: 700;
            color: #1976d2;
        }
    """)