from typing import Dict, List, Tuple
import heapq
from collections import defaultdict

def simplify_debts(member_balances: Dict[str, float]) -> Dict[str, List[Tuple[str, float]]]:
    paid_heap = []      
    borrowed_heap = [] 

    for user, balance in member_balances.items():
        if balance > 0:
            heapq.heappush(paid_heap, (-balance, user)) 
        elif balance < 0:
            heapq.heappush(borrowed_heap, (balance, user)) 

    transactions = defaultdict(list)

    while paid_heap and borrowed_heap:
        p_amt, p_user = heapq.heappop(paid_heap)
        b_amt, b_user = heapq.heappop(borrowed_heap)

        p_amt = -p_amt 

        if p_amt == abs(b_amt):
            transactions[b_user].append((p_user, p_amt))
        elif p_amt > abs(b_amt):
            transactions[b_user].append((p_user, abs(b_amt)))
            heapq.heappush(paid_heap, (-(p_amt - abs(b_amt)), p_user))
        else:
            transactions[b_user].append((p_user, p_amt))
            heapq.heappush(borrowed_heap, ((b_amt + p_amt), b_user))

    return dict(transactions)
