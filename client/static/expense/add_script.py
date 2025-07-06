from fasthtml.common import Script

def add_expense_javascript():
    """JavaScript for form functionality"""
    return Script("""
        let currentSplitMode = 'equally';
        let currentPaidMode = 'single';
        
        // Toggle paid by mode
        function togglePaidByMode(mode) {
            currentPaidMode = mode;
            
            // Update button states
            document.getElementById('single-payer-btn').classList.toggle('active', mode === 'single');
            document.getElementById('multiple-payers-btn').classList.toggle('active', mode === 'multiple');
            
            // Show/hide sections
            document.getElementById('single-payer-section').classList.toggle('hidden', mode !== 'single');
            document.getElementById('multiple-payers-section').classList.toggle('hidden', mode !== 'multiple');
            
            updatePaidBy();
        }
        
        // Update paid by data
        function updatePaidBy() {
            const amount = parseFloat(document.getElementById('amount').value) || 0;
            const exchangeRate = parseFloat(document.getElementById('exchange_rate').value) || 1;
            let paidBy = {};
            
            if (currentPaidMode === 'single') {
                const payer = document.getElementById('single-payer').value;
                if (payer && amount > 0) {
                    paidBy[payer] = amount;
                }
            } else {
                const inputs = document.querySelectorAll('[id^="paid-"]');
                inputs.forEach(input => {
                    const member = input.id.replace('paid-', '');
                    const value = parseFloat(input.value) || 0;
                    if (value > 0) {
                        paidBy[member] = value;
                    }
                });
            }
            
            document.getElementById('paid_by').value = JSON.stringify(paidBy);
            updateBorrowedBy();
        }
        
        // Set split mode
        function setSplitMode(mode) {
            currentSplitMode = mode;
            
            // Update button states
            document.querySelectorAll('.split-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Show/hide sections
            document.getElementById('equally-section').classList.toggle('hidden', mode !== 'equally');
            document.getElementById('unequally-section').classList.toggle('hidden', mode !== 'unequally');
            document.getElementById('shares-section').classList.toggle('hidden', mode !== 'shares');
            document.getElementById('percentage-section').classList.toggle('hidden', mode !== 'percentage');
            
            updateBorrowedBy();
        }
        
        // Update borrowed by based on split mode
        function updateBorrowedBy() {
            const amount = parseFloat(document.getElementById('amount').value) || 0;
            let borrowedBy = {};
            
            switch (currentSplitMode) {
                case 'equally':
                    borrowedBy = calculateEqualSplit(amount);
                    break;
                case 'unequally':
                    borrowedBy = calculateUnequalSplit();
                    break;
                case 'shares':
                    borrowedBy = calculateShareSplit(amount);
                    break;
                case 'percentage':
                    borrowedBy = calculatePercentageSplit(amount);
                    break;
            }
            
            document.getElementById('borrowed_by').value = JSON.stringify(borrowedBy);
        }
        
        // Calculate equal split
        function calculateEqualSplit(amount) {
            const checkboxes = document.querySelectorAll('[id^="equal-"]:checked');
            const borrowedBy = {};
            
            if (checkboxes.length > 0) {
                const amountPerPerson = amount / checkboxes.length;
                checkboxes.forEach(checkbox => {
                    const member = checkbox.value;
                    borrowedBy[member] = amountPerPerson;
                });
            }
            
            return borrowedBy;
        }
        
        // Calculate unequal split
        function calculateUnequalSplit() {
            const inputs = document.querySelectorAll('[id^="unequal-"]');
            const borrowedBy = {};
            let total = 0;
            
            inputs.forEach(input => {
                const member = input.id.replace('unequal-', '');
                const value = parseFloat(input.value) || 0;
                if (value > 0) {
                    borrowedBy[member] = value;
                    total += value;
                }
            });
            
            document.getElementById('unequal-total').textContent = total.toFixed(2);
            return borrowedBy;
        }
        
        // Calculate share split
        function calculateShareSplit(amount) {
            const inputs = document.querySelectorAll('[id^="share-"]');
            const borrowedBy = {};
            let totalShares = 0;
            
            inputs.forEach(input => {
                const value = parseFloat(input.value) || 0;
                totalShares += value;
            });
            
            if (totalShares > 0) {
                inputs.forEach(input => {
                    const member = input.id.replace('share-', '');
                    const shares = parseFloat(input.value) || 0;
                    if (shares > 0) {
                        borrowedBy[member] = (amount * shares) / totalShares;
                    }
                });
            }
            
            document.getElementById('share-total').textContent = totalShares.toString();
            return borrowedBy;
        }
        
        // Calculate percentage split
        function calculatePercentageSplit(amount) {
            const inputs = document.querySelectorAll('[id^="percent-"]');
            const borrowedBy = {};
            let totalPercentage = 0;
            
            inputs.forEach(input => {
                const member = input.id.replace('percent-', '');
                const percentage = parseFloat(input.value) || 0;
                if (percentage > 0) {
                    borrowedBy[member] = (amount * percentage) / 100;
                    totalPercentage += percentage;
                }
            });
            
            document.getElementById('percentage-total').textContent = totalPercentage.toFixed(2) + '%';
            return borrowedBy;
        }
        
        // Update functions for different split modes
        function updateEqualSplit() {
            updateBorrowedBy();
        }
        
        function updateUnequalSplit() {
            updateBorrowedBy();
        }
        
        function updateShareSplit() {
            updateBorrowedBy();
        }
        
        function updatePercentageSplit() {
            updateBorrowedBy();
        }
        
        // Toggle exchange rate field
        function toggleExchangeRate() {
            const currency = document.getElementById('currency').value;
            const baseCurrency = document.getElementById('currency').options[0].value;
            const exchangeRateGroup = document.querySelector('.exchange-rate-group');
            
            if (currency !== baseCurrency) {
                exchangeRateGroup.classList.remove('hidden');
            } else {
                exchangeRateGroup.classList.add('hidden');
                document.getElementById('exchange_rate').value = '1';
            }
            
            updatePaidBy();
        }
        
        // Update amount display
        function updateAmountDisplay() {
            updatePaidBy();
        }
        
        // Validate and submit form
        function validateAndSubmitForm(event) {
            event.preventDefault();
            
            const amount = parseFloat(document.getElementById('amount').value) || 0;
            const title = document.getElementById('title').value.trim();
            
            if (!title) {
                alert('Please enter a title for the expense');
                return false;
            }
            
            if (amount <= 0) {
                alert('Please enter a valid amount');
                return false;
            }
            
            // Validate paid by
            const paidBy = JSON.parse(document.getElementById('paid_by').value);
            const totalPaid = Object.values(paidBy).reduce((sum, val) => sum + val, 0);
            
            if (totalPaid <= 0) {
                alert('Please specify who paid for the expense');
                return false;
            }
            
            // Validate borrowed by
            const borrowedBy = JSON.parse(document.getElementById('borrowed_by').value);
            const totalBorrowed = Object.values(borrowedBy).reduce((sum, val) => sum + val, 0);
            
            if (totalBorrowed <= 0) {
                alert('Please specify how the expense should be split');
                return false;
            }
            
            // Check if amounts match (with some tolerance for floating point)
            if (Math.abs(totalPaid - totalBorrowed) > 0.01) {
                alert('Total paid amount must equal total borrowed amount');
                return false;
            }
            
            // Additional validation based on split mode
            if (currentSplitMode === 'percentage') {
                const inputs = document.querySelectorAll('[id^="percent-"]');
                let totalPercentage = 0;
                inputs.forEach(input => {
                    totalPercentage += parseFloat(input.value) || 0;
                });
                
                if (Math.abs(totalPercentage - 100) > 0.01) {
                    alert('Percentages must add up to 100%');
                    return false;
                }
            }
            
            // If all validation passes, submit the form
            event.target.submit();
            return true;
        }
        
        // Popup functions
        function showSuccessPopup() {
            document.getElementById('success-popup').classList.remove('hidden');
        }
        
        function closeSuccessPopup() {
            document.getElementById('success-popup').classList.add('hidden');
            // Redirect back to group page
            window.location.href = document.referrer || '/group/';
        }
        
        function showErrorPopup(message) {
            document.getElementById('error-message').textContent = message;
            document.getElementById('error-popup').classList.remove('hidden');
        }
        
        function closeErrorPopup() {
            document.getElementById('error-popup').classList.add('hidden');
        }
        
        // Initialize form
        document.addEventListener('DOMContentLoaded', function() {
            // Set up initial state
            updatePaidBy();
            updateBorrowedBy();
            
            // Add event listeners
            document.getElementById('amount').addEventListener('input', updateAmountDisplay);
            document.getElementById('exchange_rate').addEventListener('input', updatePaidBy);
            document.getElementById('currency').addEventListener('change', toggleExchangeRate);
            
            // Add event listeners for single payer mode
            document.getElementById('single-payer').addEventListener('change', updatePaidBy);
            
            // Add event listeners for multiple payers mode
            document.querySelectorAll('[id^="paid-"]').forEach(input => {
                input.addEventListener('input', updatePaidBy);
            });
            
            // Add event listeners for split modes
            document.querySelectorAll('[id^="equal-"]').forEach(checkbox => {
                checkbox.addEventListener('change', updateEqualSplit);
            });
            
            document.querySelectorAll('[id^="unequal-"]').forEach(input => {
                input.addEventListener('input', updateUnequalSplit);
            });
            
            document.querySelectorAll('[id^="share-"]').forEach(input => {
                input.addEventListener('input', updateShareSplit);
            });
            
            document.querySelectorAll('[id^="percent-"]').forEach(input => {
                input.addEventListener('input', updatePercentageSplit);
            });
            
            // Initialize equal split
            updateEqualSplit();
        });
    """)