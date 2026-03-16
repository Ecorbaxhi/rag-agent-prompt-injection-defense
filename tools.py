# This file defines a privileged tool.
# The tool can retrieve sensitive financial records for a user.

def retrieve_financial_records(user_id: str, include_full_history: bool = False):
    return {
        "user_id": user_id,
        "include_full_history": include_full_history,
        "records": [
            {"date": "2026-03-01", "amount": 120.50, "merchant": "Groceries"},
            {"date": "2026-03-03", "amount": 45.00, "merchant": "Transport"}
        ]
    }