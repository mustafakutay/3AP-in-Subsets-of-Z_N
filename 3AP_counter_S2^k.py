#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -----------------------------------------
# 1) Quadratic Residues mod 2^k
# -----------------------------------------
def quadratic_residues_2power(k):
    """
   Returns the list of quadratic residues modulo p^k
    i.e. S_{2^k} = { x^2 mod 2^k : x = 0,1,2,...,2^k - 1 }.
    """
    mod = 2**k
    residues = set()
    for x in range(mod):
        residues.add((x * x) % mod)
    return sorted(residues)


# -----------------------------------------
# 2) Counts the number of 3APs using Brute‐Force 
# -----------------------------------------
def brute_force_3AP_count(S, mod):
    """
 This counts the number of 3-term arithmetic progressions among ordered triples (x,y,z) in a given set S, 
    where each triple is counted individually. The element x,y,z must be distinct and satisfy 
    the condition of forming an arithmetic progression.
    """
    count = 0
    for x in S:
        for y in S:
            d = (y - x) % mod
            if d == 0:
                # d=0 ise trivial ilerleme, atla
                continue
            for z in S:
                if (z - y) % mod == d:
                    # Eğer (z - y) mod d ise bu bir 3-AP
                    count += 1
    return count


# -----------------------------------------
# 3) Calculates the number of non-trivial 3-term APs in S_{p^k} according to the given formula.
# -----------------------------------------
def formula_3AP_2power(k):
    """
    Teorem: Let k be a positive integer. The number of non-trivial 
    three-term arithmetic progressions in S_{2^k} is:
    
      • If k is odd:
          (2^{2k-2} - 5·2^{k-1} + 34) / 15

      • If k is even:
          (2^{2k-1} + 25·2^{2k-2} - 135·2^{k-1} + 162) / 405

Since the result is already given to be exactly divisible, we use the `//` operator to obtain an integer.
    """
    if k % 2 == 1:
        # k is odd
        numerator   = 2**(2*k - 2)  - 5 * 2**(k - 1)   + 34
        denominator = 15
    else:
        # k is even
        numerator   = 2**(2*k - 1) + 25 * 2**(2*k - 2) - 135 * 2**(k - 1) + 162
        denominator = 405

    return numerator // denominator


# -----------------------------------------
# 4) Comparing Function
# -----------------------------------------
def test_compare_2power(k):
    """
    1) mod = 2^k, S = quadratic_residues_2power(k)
    2) brute_force_3AP_count(S, mod)  → The number of actual 3-APs  
    3) formula_3AP_2power(k)          →  Result in the theorem 
    4) Printing both of them and difference
    """
    mod = 2 ** k
    S = quadratic_residues_2power(k)

    true_val    = brute_force_3AP_count(S, mod)
    formula_val = formula_3AP_2power(k)

    print(f"------ k = {k}, mod = 2^{k} = {mod} ------")
    print(f"S_{mod} (quadratic residues): {S}")
    print(f"Actual 3-AP count (brute force): {true_val}")
    print(f"Value derived from the formula : {formula_val}")
    print(f"Difference = |{true_val} - {formula_val}| = {abs(true_val - formula_val)}\n")


# -----------------------------------------
# 5) Sample Tests
# -----------------------------------------
# By adding the desired k values below, you can easily compare the brute-force and formula results.

examples = [1, 2, 3, 4, 5, 6]  

for k in examples:
    test_compare_2power(k)


# In[ ]:




