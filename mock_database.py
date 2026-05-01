# mock_database.py
DB_SIZE = 12

def get_all_transactions():
    # This looks like a standard SQLAlchemy or Django mock return
    return [
        {"id": i, "stripe_charge_id": f"ch_mock_{i}", "status": "processed"}
        for i in range(DB_SIZE)
    ]