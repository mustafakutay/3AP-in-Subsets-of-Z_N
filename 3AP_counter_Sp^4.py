#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def quadratic_residues(p, power=4):
    """Returns the list of quadratic residues modulo p^power."""
    mod = p ** power
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
                x, y, z = S[i], S[j], S[k]
                if (y - x) % mod == (z - y) % mod:
                    count += 1
    return count

def formula_3ap_S_p4(p):
    """Returns formula-based 3-AP count in S_{p^4}, depending on p mod 8."""
    if p % 8 == 1:
        return (p**8 - 6*p**7 + 11*p**6 - 11*p**5 + 15*p**4 - 14*p**3 + 13*p**2 - 8*p) // 8
    elif p % 8 == 3:
        return ((p - 1) * (p**7 + p**6 - 3*p**3 + p**2 - 4*p)) // 8
    elif p % 8 == 5:
        return (p**2 * (p - 1)**2 * (p**2 + 1)**2) // 8
    elif p % 8 == 7:
        return (p**8 - 4*p**7 + 7*p**6 - 8*p**5 + 9*p**4 - 8*p**3 +7*p**2 - 4*p) // 8
    else:
        return None

def analyze_p_fourth(p):
    mod = p ** 4
    S = quadratic_residues(p, power=4)
    brute = brute_force_3AP_count(S, mod)
    formula = formula_3ap_S_p4(p)
    print(f"==== p = {p}, mod = {mod} ====")
    print(f"S_{mod} (quadratic residues): {len(S)}")
    print(f"Actual 3-AP count (brute force): {brute}")
    print(f"Value derived from the formula:  {formula}")
    print(f"Difference: {abs(brute - formula)}")
    print(f"Consistency Check: {'✅' if brute == formula else '❌'}\n")

# Sample tests (note that computations may take longer for larger values of p)
for p in [3, 5, 7, 11]:  # This value may be increased if required
    
    analyze_p_fourth(p)


# In[ ]:




