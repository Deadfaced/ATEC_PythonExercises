def VerifyTransactions():
    """
    Checks NIFs used in recent transactions and compares with blacklisted NIFs
    """

    BLACKLISTED_VENDORS = {"213643547", "156354157", "218687416"}
    RECENT_TRANSACTIONS = {
        "213643547",
        "209348572",
        "546466545",
        "218687416",
        "654654564"
    }
    possible_threats = RECENT_TRANSACTIONS.intersection(BLACKLISTED_VENDORS)
    if len(possible_threats) > 0:
        for _ in possible_threats:
            print(f"Auditoria necessária!NIF: {_}")

VerifyTransactions()