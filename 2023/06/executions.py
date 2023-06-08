def safety(N: int, K: int) -> int:
    if N == 1:
        return 0
    else:
        return (safety(N - 1, K) + K) % N
    # return ((K - 1) % N + 1)
    
print(safety(9, 2))
print(safety(9, 3))
print(safety(7, 2))