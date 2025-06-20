#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import legendre_symbol

def epsilon_p(p):
    """
    ε_p = 1  if p ≡ 1 (mod 4),
         = i  if p ≡ 3 (mod 4).
    (i: imaginary unit)
    """
    return 1 if (p % 4 == 1) else 1j  # 1j = i

def quadratic_residues(p, k):
    """
    Returns the list of quadratic residues modulo p^k
    i.e. S_{p^k} = { x^2 mod (p^k) : x = 0,1,2,…,p^k - 1 }.
    """
    mod = p**k
    residues = set()
    for x in range(mod):
        residues.add((x * x) % mod)
    return sorted(residues)


def formula_3AP(p, k):
    """
    Calculates the number of non-trivial 3-term APs in S_{p^k} according to the given formula.
    
    Formula:
    - If k is even:
        part1 = [ p^(2k+7) - p^(2k+5) + p^(2k+4) - p^(2k+2)
                  - p^(k+7) + p^(k+6) + 2 p^(k+5) + p^(k+3)
                  - p^(k+2) - 2 p^(k+1) - p^6 - p^5 - p^4 - p^3 + 2 p^2 + 2 p ]
                / [8 (p+1)^3 (p^4 - 1)]

        part2 = [ -p^(2k+4) + p^(2k+3) + p^(k+5) + p^(k+4)
                  - p^(k+3) + p^(k+2) - 2 p^(k+1) - p^5 - p^2 + 2 p ]
                / [4 (p+1) (p^4 - 1)]

        Result = part1 + ε_p^2 * (½ + (−2∣p)_L) * part2

    - If k is odd:
        part1 = [ p^(2k+7) - p^(2k+5) + p^(2k+4) - p^(2k+2)
                  + 2 p^(k+7) + p^(k+6) - p^(k+5) - 2 p^(k+3)
                  - p^(k+2) + p^(k+1) - 2 p^6 - 2 p^5 + p^4 + p^3 + p^2 + p ]
                / [8 (p+1)^3 (p^4 - 1)]

        part2 = [ -p^(2k+4) + p^(2k+3) + 2 p^(k+5) - p^(k+4) + p^(k+3)
                  - p^(k+2) - p^(k+1) - 2 p^4 + p^3 + 1 ]
                / [4 (p+1) (p^4 - 1)]

        Result = part1 + ε_p^2 * (½ + (−2∣p)_L) * part2

    Here (−2∣p)_L = Legendre symbol. ε_p = 1 or i.
    """

    # Legendre symbol: (−2 / p)_L
    # sympy.legendre_symbol(z, p) z^( (p-1)/2 ) mod p  = ±1 or 0
    L = legendre_symbol(-2, p)

    eps = epsilon_p(p)
    eps2 = eps * eps  # ε_p^2

    # Calculate big powers one by one
    p2k7 = p ** (2*k + 7)
    p2k5 = p ** (2*k + 5)
    p2k4 = p ** (2*k + 4)
    p2k3 = p ** (2*k + 3)
    p2k2 = p ** (2*k + 2)

    pk7 = p ** (k + 7)
    pk6 = p ** (k + 6)
    pk5 = p ** (k + 5)
    pk4 = p ** (k + 4)
    pk3 = p ** (k + 3)
    pk2 = p ** (k + 2)
    pk1 = p ** (k + 1)

    p6 = p ** 6
    p5 = p ** 5
    p4 = p ** 4
    p3 = p ** 3
    p2 = p ** 2
    p1 = p

    denom1 = 8 * (p + 1)**3 * (p**4 - 1)
    denom2 = 4 * (p + 1) * (p**4 - 1)

    if k % 2 == 0:
        # --- k even ---
        part1 = (
            p2k7 - p2k5 + p2k4 - p2k2
            - pk7 + pk6 + 2*pk5 + pk3
            - pk2 - 2*pk1 - p6 - p5 - p4 - p3
            + 2*p2 + 2*p1
        ) / denom1

        part2 = (
            -p2k4 + p2k3 + pk5 + pk4
            - pk3 + pk2 - 2*pk1 - p5 - p2 + 2*p1
        ) / denom2

    else:
        # --- k odd ---
        part1 = (
            p2k7 - p2k5 + p2k4 - p2k2
            + 2*pk7 + pk6 - pk5 - 2*pk3
            - pk2 + pk1 - 2*p6 - 2*p5
            + p4 + p3 + p2 + p1
        ) / denom1

        part2 = (
            -p2k4 + p2k3 + 2*pk5 - pk4 + pk3
            - pk2 - pk1 - 2*p4 + p3 + 1
        ) / denom2

    val = part1 + eps2 * (0.5 + L) * part2

    # If val is a complex valued, (eps2 = i^2 = -1) take the real part
    if isinstance(val, complex):
        val = val.real

    return val


def brute_force_3AP_count(S, mod):
    """
  This counts the number of 3-term arithmetic progressions among ordered triples (x,y,z) in a given set S, 
    where each triple is counted individually. The element x,y,z must be distinct and satisfy 
    the condition of forming an arithmetic progression.
    """

    count = 0
    S_list = S  # S: actually this is an ordered list
    n = len(S_list)

    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            for l in range(n):
                if l == i or l == j:
                    continue
                x = S_list[i]
                y = S_list[j]
                z = S_list[l]
                # AP condition:
                if (y - x) % mod == (z - y) % mod:
                    count += 1

    return count


def test_compare(p, k):
    """
    p = odd prime, k = positive integer.
    1) S_{p^k} create the set.
    2) Find the number of 3AP with Brute-force.
    3) Find the number of 3AP with formula.
    4) Write the results.
    """
    mod = p**k
    S = quadratic_residues(p, k)

    true_val = brute_force_3AP_count(S, mod)
    formula_val = formula_3AP(p, k)

    print(f"------ p = {p}, k = {k}, mod = {mod} ------")
    print(f"S_{mod} (quadratic residues): {S}")
    print(f"Actual 3-AP count (brute force): {true_val}")
    print(f"Value derived from the formula: {formula_val}")
    print(f"Difference = |{true_val} - {formula_val}| = {abs(true_val - formula_val)}\n")


# ---------------------------
# Sample Tests:
# ---------------------------
examples = [(3, 1), (3, 2), (5, 1), (5, 2), (7,3)]

for (p, k) in examples:
    test_compare(p, k)


# In[ ]:




