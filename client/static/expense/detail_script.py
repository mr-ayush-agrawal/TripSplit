from fasthtml.common import Script

def expense_detail_scripts():
    """
    JavaScript for expense actions
    """
    return Script("""
        function confirmDelete(expenseId, groupId) {
            if (confirm('Are you sure you want to delete this expense? This action cannot be undone.')) {
                // Make DELETE request to backend
                fetch(`/api/group/${groupId}/expense/${expenseId}`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                .then(response => {
                    if (response.ok) {
                        alert('Expense deleted successfully');
                        window.location.href = `/group/${groupId}`;
                    } else {
                        alert('Failed to delete expense');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while deleting the expense');
                });
            }
        }
    """)
