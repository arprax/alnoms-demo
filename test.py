import mock_database as db

def data_gen(n):
    # We scale the Mock DB and the input list to N
    # This turns O(N*M) into a pure O(N^2) trap
    db.DB_SIZE = n
    mock_events = [{"stripe_id": f"ch_mock_{i}"} for i in range(n)]
    return (mock_events,)

def run_transaction_audit(events):
    matches = []
    db_records = db.get_all_transactions()

    # ✅ THE FIX: O(M) Pre-indexing
    # We create a hash-map for O(1) lookups.
    db_lookup = {r['stripe_charge_id']: r for r in db_records}

    for event in events:
        if event['stripe_id'] in db_lookup:
            matches.append(event)

    print(f"Audit complete. Verified {len(matches)} transactions.")
    return matches

if __name__ == "__main__":
    # Small test for local run
    e, = data_gen(10)
    run_transaction_audit(e)