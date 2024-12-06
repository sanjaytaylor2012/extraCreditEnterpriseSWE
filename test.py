from inmemoryDB import inmemoryDB

inmemoryDB = inmemoryDB()

print("Get 'A':", inmemoryDB.get("A"))  # Expected output: None

try:
    inmemoryDB.put("A", 5)
except Exception as e:
    print("Put 'A' without transaction:", str(e))  # Expected output: Error message

inmemoryDB.begin_transaction()
print("Transaction started")

inmemoryDB.put("A", 5)
print("Put 'A', 5 (within transaction)")

print("Get 'A' (within transaction, not committed):", inmemoryDB.get("A"))  # Expected output: None

inmemoryDB.put("A", 6)
print("Put 'A', 6 (within transaction)")

inmemoryDB.commit()
print("Transaction committed")

print("Get 'A' (after commit):", inmemoryDB.get("A"))  # Expected output: 6

try:
    inmemoryDB.commit()
except Exception as e:
    print("Commit without transaction:", str(e))  # Expected output: Error message

try:
    inmemoryDB.rollback()
except Exception as e:
    print("Rollback without transaction:", str(e))  # Expected output: Error message

print("Get 'B':", inmemoryDB.get("B"))  # Expected output: None

inmemoryDB.begin_transaction()
print("Transaction started")

inmemoryDB.put("B", 10)
print("Put 'B', 10 (within transaction)")

inmemoryDB.rollback()
print("Transaction rolled back")

print("Get 'B' (after rollback):", inmemoryDB.get("B"))  # Expected output: None
