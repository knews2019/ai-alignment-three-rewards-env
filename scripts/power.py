#!/usr/bin/env python3
"""Episodes per arm needed to detect a drop in an event rate.

Two-proportion z-test, normal approximation, two-sided alpha, given power.
Episodes are treated as independent here, which they are NOT across seeds:
the unit of replication is the training run. Use this for a floor, then
budget >= 3 seeds per cell and fit a mixed-effects model.

    python scripts/power.py 0.20 0.10            # 20% -> 10%
    python scripts/power.py 0.10 0.05 --power 0.9
"""
from __future__ import annotations

import argparse
import math


def _z(p: float) -> float:
    """Inverse standard normal CDF (Acklam's approximation; adequate here)."""
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p <= phigh:
        q = p - 0.5
        r = q*q
        return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)
    q = math.sqrt(-2 * math.log(1 - p))
    return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)


def n_per_arm(p1: float, p2: float, alpha: float = 0.05, power: float = 0.80) -> int:
    za = _z(1 - alpha / 2)
    zb = _z(power)
    pbar = (p1 + p2) / 2
    num = (za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p1 - p2) ** 2)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("p1", type=float, help="baseline event rate, e.g. 0.20")
    ap.add_argument("p2", type=float, help="target event rate, e.g. 0.10")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.80)
    args = ap.parse_args()
    n = n_per_arm(args.p1, args.p2, args.alpha, args.power)
    print(f"{args.p1:.0%} -> {args.p2:.0%}  alpha={args.alpha} power={args.power}:  ~{n} episodes per arm")
    print("Reminder: episodes are not independent across seeds. Budget >= 3 seeds per cell.")


if __name__ == "__main__":
    main()
