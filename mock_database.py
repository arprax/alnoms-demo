# mock_database.py

def get_all_transactions():
    """
    Simulates a database query returning local transactions.
    We return 12 items here so your Alnoms CLI output perfectly matches
    the "M=12" test workload you saw in your earlier successful run.
    """
    return [
        {"id": 1001, "stripe_charge_id": "ch_1OzX9q2eZvKYlo2C0"},
        {"id": 1002, "stripe_charge_id": "ch_1OzX9r2eZvKYlo2C1"},
        {"id": 1003, "stripe_charge_id": "ch_1OzX9s2eZvKYlo2C2"},
        {"id": 1004, "stripe_charge_id": "ch_1OzX9t2eZvKYlo2C3"},
        {"id": 1005, "stripe_charge_id": "ch_1OzX9u2eZvKYlo2C4"},
        {"id": 1006, "stripe_charge_id": "ch_1OzX9v2eZvKYlo2C5"},
        {"id": 1007, "stripe_charge_id": "ch_1OzX9w2eZvKYlo2C6"},
        {"id": 1008, "stripe_charge_id": "ch_1OzX9x2eZvKYlo2C7"},
        {"id": 1009, "stripe_charge_id": "ch_1OzX9y2eZvKYlo2C8"},
        {"id": 1010, "stripe_charge_id": "ch_1OzX9z2eZvKYlo2C9"},
        {"id": 1011, "stripe_charge_id": "ch_1OzX9A2eZvKYlo2CA"},
        {"id": 1012, "stripe_charge_id": "ch_1OzX9B2eZvKYlo2CB"}
    ]