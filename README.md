
# ROTH’S THEOREM FOR CERTAIN SUBSETS OF FINITE RINGS

This repository contains the Python source codes developed for the computations and experiments in the article:

> **[ROTH’S THEOREM FOR CERTAIN SUBSETS OF FINITE RINGS]**  
> *Author: Sadık Eyidoğan, Haydar Göral, Mustafa Kutay Kutlu*  
> *Year: 2025*


# Verification of 3-Term Arithmetic Progression Counts in Quadratic Residues Modulo \( p^k \)

There are Python implementations that verify explicit formulas for counting non-trivial three-term arithmetic progressions (3-APs) within sets of quadratic residues modulo powers of primes. These codes correspond to different theorems and formulas depending on the modulus and the prime's residue class.

## Overview

The main objective is to computationally confirm mathematical theorems that provide closed-form expressions for the number of 3-APs in sets:

\[
S_{p^k} = \{ x^2 \bmod p^k \mid x \in \mathbb{Z}_{p^k} \},
\]

where \( p \) is an odd prime and \( k \) is a positive integer, or for powers of 2.

The repository includes implementations for the following cases:

- \( S_{p^k} \) for general \( k \) (Theorem 1.2),
- \( S_{2^k} \) with formulas depending on parity of \( k \) (Theorem 1.3),
- \( S_{p^2} \), \( S_{p^3} \), and \( S_{p^4} \) with formulas determined by \( p \mod 8 \).

Each script:

- Generates the quadratic residues modulo the specified modulus,
- Enumerates all ordered triples to count non-trivial 3-APs via brute force,
- Calculates the number of 3-APs predicted by the corresponding formula,
- Compares both values to verify correctness.---

## 📂 Code Files

This repository contains the following scripts:

| File Name                   | Description |
|----------------------------|-------------|
| 3AP_counter_S2^k.py`       | The code verifies the correctness of Theorem 1.3, which gives a closed formula for the number of non-trivial three-term arithmetic progressions in \( S_{2^k} \), depending on whether \( k \) is odd or even. It computes the actual number of such progressions by brute-force enumeration of all ordered triples in \( S_{2^k} \) that satisfy the arithmetic progression condition modulo \( 2^k \), and compares this count with the value predicted by the corresponding formula. |

| 3AP_counter_Sp^2.py`       | The code verifies the correctness of several exact formulas for the number of non-trivial three-term arithmetic progressions in \( S_{p^2} \), where the formula used depends on the congruence class of the odd prime \( p \) modulo 8. For each such prime, the code computes the actual number of 3-term arithmetic progressions in \( S_{p^2} \) via brute-force and compares it with the corresponding theoretical value.|

| 3AP_counter_Sp^3.py`       | This code tests explicit formulas for the number of non-trivial three-term arithmetic progressions in \( S_{p^3} \), where the formula to be applied depends on the congruence class of the odd prime \( p \) modulo 8. It computes the set of quadratic residues modulo \( p^3 \), counts all valid arithmetic progressions via brute-force, and verifies that this count agrees with the predicted value from the formula.|

| 3AP_counter_Sp^4.py`       | This code confirms the accuracy of exact formulas for the number of non-trivial 3-term arithmetic progressions in \( S_{p^4} \), with the formula selected based on the value of \( p \mod 8 \), where \( p \) is an odd prime. It computes the set of quadratic residues modulo \( p^3 \), counts all valid arithmetic progressions via brute-force, and verifies that this count agrees with the predicted value from the formula.|

| 3AP_counter_Sp^k.py`       | The code verifies the correctness of Theorem 1.2, which provides a formula for the number of non-trivial three-term arithmetic progressions in \( S_{p^k} \), depending on whether \( k \) is odd or even. It computes the exact number of such progressions by exhaustively checking all ordered triples in \( S_{p^k} \) that satisfy the arithmetic progression condition modulo \( p^k \), and then compares this empirical count with the value predicted by the theorem’s formula. |

---

## How to Run
Make sure you have Python 3.x installed. Most codes require only standard libraries; some may need:

sympy (for number theory and modular arithmetic)
numpy (for arrays and numeric handling)



## Example Output for "3AP_counter_Sp^k"

------ p = 5, k = 2, mod = 25 ------
S_25 (quadratic residues): [0, 1, 4, 6, 9, 11, 14, 16, 19, 21, 24]
Actual 3-AP count (brute force): 50
Value derived from the formula: 50.0
Difference = |50 - 50.0| = 0.0

--

