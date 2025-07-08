from fasthtml.common import Script
import json

def expense_edit_initialization_script(expense_data):
    """JavaScript to initialize the form with existing data"""
    paid_by_data = expense_data.get("paid_by_original", {})
    borrowed_by_data = expense_data.get("borrowed_by_original", {})
    
    return Script(f"""
        document.addEventListener('DOMContentLoaded', function() {{
            // Set initial paid by data
            document.getElementById('paid_by').value = '{json.dumps(paid_by_data)}';
            
            // Set initial borrowed by data
            document.getElementById('borrowed_by').value = '{json.dumps(borrowed_by_data)}';
            
            // Trigger updates to sync UI
            updatePaidBy();
            updateAmountDisplay();
            
            // Initialize split mode based on data
            const borrowedByData = {json.dumps(borrowed_by_data)};
            const nonZeroBorrowers = Object.keys(borrowedByData).filter(k => borrowedByData[k] > 0);
            
            if (nonZeroBorrowers.length > 0) {{
                // Update the appropriate split section totals
                updateEqualSplit();
                updateUnequalSplit();
                updateShareSplit();
                updatePercentageSplit();
            }}
        }});
    """)
