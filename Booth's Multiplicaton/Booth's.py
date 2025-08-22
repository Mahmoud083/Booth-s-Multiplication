def booth_algorithm(m, r):
    # Converting to 64-bit representation
    def to_twos_complement(val, bits):
        if val < 0:
            val = (1 << bits) + val
        return val

    def from_twos_complement(val, bits):
        if val & (1 << (bits - 1)):
            val = val - (1 << bits)
        return val

    # Initializing variables
    n = 64
    m = to_twos_complement(m, n)
    r = to_twos_complement(r, n)
    A = 0
    Q = r
    Q_minus_1 = 0
    M = m

    for _ in range(n):
        if (Q & 1) == 1 and Q_minus_1 == 0:
            # A = A - M
            A = (A - M) & ((1 << (n + 1)) - 1)
        elif (Q & 1) == 0 and Q_minus_1 == 1:
            # A = A + M
            A = (A + M) & ((1 << (n + 1)) - 1)

        # Arithmetic right shift A, Q, Q-1
        Q_minus_1 = Q & 1
        combined = ((A << n) | Q) >> 1
        A = (combined >> n) & ((1 << n) - 1)
        Q = combined & ((1 << n) - 1)

    # Combining A and Q to get the final result
    result = (A << n) | Q

    # Adjusting for negative result
    result = from_twos_complement(result, 2 * n)

    return result

# Example usage:
m = -7
r = 3
print(booth_algorithm(m, r))  # In here, we expect the output should be the multiplication of -7 and 3
