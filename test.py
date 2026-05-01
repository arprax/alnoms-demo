import mock_database as db

def process_stripe_reconciliation(event_payload: dict):
    if event_payload.get("type") != "billing.reconciliation.requested":
        return "Ignored"

    stripe_events = event_payload["data"]["object"]["recent_charges"]
    local_transactions = db.get_all_transactions()
    missing_transactions = []

    local_transaction_ids = {tx['stripe_charge_id'] for tx in local_transactions}

    for charge in stripe_events:
        charge_id = charge['id']

        if charge_id not in local_transaction_ids:
            missing_transactions.append(charge)

    print(f"Reconciliation complete. Found {len(missing_transactions)} missing.")
    return missing_transactions

if __name__ == "__main__":
    mock_stripe_payload = {
        "type": "billing.reconciliation.requested",
        "data": {
            "object": {
                "recent_charges": [
                    {"id": "ch_1OzX9A2eZvKYlo2ZZ"},
                    {"id": "ch_1OzX9B2eZvKYlo2YY"},
                    {"id": "ch_1OzX9C2eZvKYlo2XX"},
                    {"id": "ch_1OzX9D2eZvKYlo2WW"},
                    {"id": "ch_1OzX9E2eZvKYlo2VV"}
                ]
            }
        }
    }
    process_stripe_reconciliation(mock_stripe_payload)