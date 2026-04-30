import json
import mock_database as db


def process_stripe_reconciliation(event_payload: dict):
    """
    Service layer function to reconcile incoming Stripe events
    against our local database to find missing payments.
    """
    if event_payload.get("type") != "billing.reconciliation.requested":
        return "Ignored"

    stripe_events = event_payload["data"]["object"]["recent_charges"]
    local_transactions = db.get_all_transactions()
    missing_transactions = []

    # 🚨 THE VILLAIN: The O(N * M) Shadow Loop
    # The developer used a List `[]` instead of a Set `{}`.
    # This will pass SonarQube, but it will crash the server under load.
    local_transaction_ids = set([tx['stripe_charge_id'] for tx in local_transactions])

    for charge in stripe_events:
        charge_id = charge['id']

        # Linear search inside a loop!
        if charge_id not in local_transaction_ids:
            missing_transactions.append(charge)

    print(f"Reconciliation complete. Found {len(missing_transactions)} missing.")
    return missing_transactions


# 🛰️ THE DATA GENERATOR CONTRACT
# Alnoms looks for this to know how to scale 'N' for Empirical Analysis
def data_gen(n):
    """
    Generates a mock Stripe payload with 'n' charges so Alnoms
    can run empirical doubling tests.
    """
    mock_charges = [{"id": f"ch_mock_{i}"} for i in range(n)]

    mock_stripe_payload = {
        "type": "billing.reconciliation.requested",
        "data": {
            "object": {
                "recent_charges": mock_charges
            }
        }
    }

    # Must return a tuple representing the arguments for the target function
    return (mock_stripe_payload,)

if __name__ == "__main__":
    # Simulate an incoming webhook payload for the Alnoms profiler
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

    # This executes instantly, allowing Alnoms to finish and print the report.
    process_stripe_reconciliation(mock_stripe_payload)