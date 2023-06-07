#!/usr/bin/python3

def heappop(heap):
    if not heap:
        return None

    min_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    current = 0
    heapify_down(heap, len(heap), current)
    return min_value

def heapify_down(arr, n, current, heap):
    small_child = current
    left = 2 * current + 1
    right = 2 * current + 2

    if left < n and heap[left] < heap[small_child]:
        small_child = left

    if right < n and heap[right] < heap[small_child]:
        small_child = right
    
    if small_child != current:
        swap(heap,current,small_child)
        heapify_down(heap, n, small_child)

def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def test():
    heap = [2, 4, 5, 7, 9, 10]
    min_val = heappop(heap)
    assert min_val == 2, f"Error: expected 2, but got {min_val}"
    assert heap == [4, 7, 5, 10, 9], f"Error: expected [4, 7, 5, 10, 9], but got {heap}"
   
    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    min_val = heappop(heap)
    assert min_val == 1, f"Error: expected 1, but got {min_val}"
    assert heap == [2, 4, 3, 8, 5, 6, 7, 9], f"Error: expected [2, 4, 3, 8, 5, 6, 7, 9], but got {heap}"
   
    print("Great Job !!!")
test()


