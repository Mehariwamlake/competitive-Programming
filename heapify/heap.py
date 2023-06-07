def heappush(heap, value):
    heap.append(value)
    current = len(heap)
    heapify_up(heap, current)

def heapify_up(heap, current):
    