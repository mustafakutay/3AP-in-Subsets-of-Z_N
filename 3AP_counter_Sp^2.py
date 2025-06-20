#!/usr/bin/env python
# coding: utf-8

# In[2]:


def quadratic_residues(p):
    """Returns the list of quadratic residues modulo p^2."""
    mod = p ** 2
    return sorted(set((x * x) % mod for x in range(mod)))

def brute_force_3AP_count(S, mod):
    """
    This counts the number of 3-term arithmetic progressions among ordered triples (x,y,z) in a given set S, 
    where each triple is counted individually. The element x,y,z must be distinct and satisfy 
    the condition of forming an arithmetic progression.
    """
    count = 0
    n = len(S)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                x = S[i]
                y = S[j]
                z = S[k]
                if (y - x) % mod == (z - y) % mod:
                    count += 1
    return count

def formula_3ap_S_p2(p):
    """Returns formula-based 3-AP count in S_{p^2}, depending on p mod 8."""
    if p % 8 == 1:
        return p * (p - 1) * (p**2 - 5*p + 8) // 8
    elif p % 8 == 3:
        return p * (p - 1) * (p**2 + p - 4) // 8
    elif p % 8 == 5:
        return (p**2) * (p - 1)**2 // 8
    elif p % 8 == 7:
        return p * (p - 1) * (p**2 - 3*p + 4) // 8
    else:
        return None  # p should be odd prime

def analyze_p(p):
    mod = p ** 2
    S = quadratic_residues(p)
    brute = brute_force_3AP_count(S, mod)
    formula = formula_3ap_S_p2(p)
    print(f"---- p = {p}, mod = {mod} ----")
    print(f"S_{mod} (quadratic residues): {S}")
    print(f"Actual 3-AP count (brute force): {brute}")
    print(f"Value derived from the formula:      {formula}")
    print(f"Difference: {abs(brute - formula)}")
    print(f"Consistency Check: {'✅' if brute == formula else '❌'}\n")

# Sample tests
for p in [3, 5, 7, 11, 13, 17, 19, 23]:
    analyze_p(p)


# In[ ]:




