from fasthtml.common import Script

def delete_expense_script():
    return Script("""
        function showDeleteModal() {
            document.getElementById('deleteModal').style.display = 'block';
        }

        function hideDeleteModal() {
            document.getElementById('deleteModal').style.display = 'none';
        }

        async function confirmDeleteExpense(groupId, expenseId) {
            try {
                const response = await fetch(`/group/${groupId}/expense/${expenseId}/delete`, {
                    method: "DELETE"
                });

                if (response.ok) {
                    window.location.href = `/group/${groupId}`; // redirect to group page after delete
                } else {
                    const result = await response.json();
                    alert(result.detail || "Deletion failed");
                    hideDeleteModal();
                }
            } catch (err) {
                console.log(err);
                alert("Something went wrong");
                hideDeleteModal();
            }
        }

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') hideDeleteModal();
        });
    """)
