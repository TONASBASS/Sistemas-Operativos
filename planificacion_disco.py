# Simulacion de algoritmos de planificacion de disco (ASCII puro)

requests = [95, 180, 34, 119, 11, 123, 62, 64]
head_start = 50
MIN_TRACK, MAX_TRACK = 0, 199

from typing import List, Tuple

def fcfs(reqs: List[int], head: int) -> Tuple[List[int], int]:
    order = list(reqs)
    total = 0
    pos = head
    for r in order:
        total += abs(pos - r)
        pos = r
    return order, total

def sstf(reqs: List[int], head: int) -> Tuple[List[int], int]:
    pending = list(reqs)
    order = []
    pos = head
    total = 0
    while pending:
        nearest = min(pending, key=lambda r: abs(r - pos))
        total += abs(pos - nearest)
        pos = nearest
        order.append(nearest)
        pending.remove(nearest)
    return order, total

def scan(reqs: List[int], head: int, direction: str, edge: bool) -> Tuple[List[int], int]:
    """
    SCAN (elevador).
    direction: 'up'  -> atender hacia MAX_TRACK primero
               'down'-> atender hacia MIN_TRACK primero
    edge=True  -> llegar al borde fisico (SCAN clasico)
    edge=False -> no llegar al borde si no hay peticiones (LOOK)
    """
    order = []
    pos = head
    total = 0
    upper = sorted([r for r in reqs if r >= head])
    lower = sorted([r for r in reqs if r < head], reverse=True)

    if direction == 'up':
        for r in upper:
            total += abs(pos - r)
            pos = r
            order.append(r)
        if edge:
            total += abs(pos - MAX_TRACK)
            pos = MAX_TRACK
        for r in lower:
            total += abs(pos - r)
            pos = r
            order.append(r)
    else:  # 'down'
        for r in lower:
            total += abs(pos - r)
            pos = r
            order.append(r)
        if edge:
            total += abs(pos - MIN_TRACK)
            pos = MIN_TRACK
        for r in upper:
            total += abs(pos - r)
            pos = r
            order.append(r)
    return order, total

if __name__ == "__main__":
    fcfs_order, fcfs_seek = fcfs(requests, head_start)
    sstf_order, sstf_seek = sstf(requests, head_start)
    scan_up_order, scan_up_seek = scan(requests, head_start, direction='up', edge=True)
    scan_down_order, scan_down_seek = scan(requests, head_start, direction='down', edge=True)
    look_up_order, look_up_seek = scan(requests, head_start, direction='up', edge=False)
    look_down_order, look_down_seek = scan(requests, head_start, direction='down', edge=False)

    print("FCFS      -> orden:", fcfs_order, " | movimiento_total:", fcfs_seek)
    print("SSTF      -> orden:", sstf_order, " | movimiento_total:", sstf_seek)
    print("SCAN_up   -> orden:", scan_up_order, " | movimiento_total:", scan_up_seek, " (hacia 199 primero)")
    print("SCAN_down -> orden:", scan_down_order, " | movimiento_total:", scan_down_seek, " (hacia 0 primero)")
    print("LOOK_up   -> orden:", look_up_order, " | movimiento_total:", look_up_seek, " (referencia)")
    print("LOOK_down -> orden:", look_down_order, " | movimiento_total:", look_down_seek, " (referencia)")