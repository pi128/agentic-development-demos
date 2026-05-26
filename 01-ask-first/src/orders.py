from typing import Optional

_ORDERS: list[dict] = []

def seed(n: int = 50_000) -> None:
    """Populate with fake orders for demo purposes."""
    import random, string
    customers = ["alice", "bob", "carol", "dave", "eve"]
    statuses = ["pending", "processing", "shipped", "delivered"]
    _ORDERS.clear()
    for i in range(n):
        _ORDERS.append({
            "id": i,
            "customer": random.choice(customers),
            "items": [
                "".join(random.choices(string.ascii_lowercase, k=5))
                for _ in range(random.randint(1, 4))
            ],
            "status": random.choice(statuses),
        })

def find_orders(customer: str, status: Optional[str] = None) -> list[dict]:
    results = []
    for order in _ORDERS:
        if order["customer"] == customer:
            if status is None or order["status"] == status:
                results.append(order)
    return results

def count_by_status() -> dict[str, int]:
    counts: dict[str, int] = {}
    for order in _ORDERS:
        s = order["status"]
        counts[s] = counts.get(s, 0) + 1
    return counts
