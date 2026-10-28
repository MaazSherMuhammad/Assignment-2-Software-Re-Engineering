# analyse.py - same for every variant. Keep it next to variant_data.py; run: python3 analyse.py
import sys, zlib
from variant_data import REG_NO, CHANGES, RELEASES, PROFILE, MY_CLASS

CATS = ["corrective", "adaptive", "perfective", "preventive"]
if REG_NO.startswith("PUT"):
    sys.exit("Edit REG_NO in variant_data.py first.")
bad = [cid for cid, *_ in CHANGES if MY_CLASS.get(cid) not in CATS]
if bad:
    sys.exit("Not classified (or misspelt): " + ", ".join(bad))

print("Registration number:", REG_NO, "| system:", PROFILE["name"])
hours = dict.fromkeys(CATS, 0)
for cid, rel, h, text in CHANGES:
    hours[MY_CLASS[cid]] += h
total = sum(hours.values())
print(f"\n== PART 1: effort by maintenance category == {REG_NO}")
for c in CATS:
    print(f"{c:11s} {hours[c]:4d} h {100 * hours[c] / total:5.1f} %")
print("TOTAL      ", total, "h")
print("run stamp:", zlib.crc32((REG_NO + str(sorted(hours.items()))).encode()) % 100000)

print(f"\n== PART 2: evidence for Lehman's laws == {REG_NO}")
rels = sorted(RELEASES)
hr = {r: sum(h for _, rr, h, _ in CHANGES if rr == r) for r in rels}
pv = {r: sum(h for i, rr, h, _ in CHANGES
              if rr == r and MY_CLASS[i] == "preventive") for r in rels}
dens = {r: RELEASES[r]["defects"] / RELEASES[r]["kloc"] for r in rels}
print("rel    kloc    cc defects defects/kloc hours preventive_h")
for r in rels:
    d = RELEASES[r]
    print(f"{r:4s} {d['kloc']:5d} {d['cc']:5.1f} {d['defects']:7d} {dens[r]:11.3f} "
          f"{hr[r]:6d} {pv[r]:9d}")
mean = sum(hr.values()) / len(rels)
f, l = RELEASES[rels[0]], RELEASES[rels[-1]]
grew = all(RELEASES[b]["kloc"] > RELEASES[a]["kloc"] for a, b in zip(rels, rels[1:]))
dev = 100 * max(abs(v - mean) for v in hr.values()) / mean
print(f"complexity (cc) change, first to last release : {100 * (l['cc'] / f['cc'] - 1):+.1f} %")
print(f"largest release-hours deviation from the mean : {dev:.1f} %")
print(f"size grew in every release: {grew}; last/first = {l['kloc'] / f['kloc']:.2f}")
dchg = 100 * (dens[rels[-1]] / dens[rels[0]] - 1)
print(f"defect-density change, first to last release : {dchg:+.1f} %")
pshare = 100 * hours["preventive"] / total
print(f"preventive share of all hours                  : {pshare:.1f} %")

print(f"\n== PART 3: legacy evaluation == {REG_NO}")
q = sum(PROFILE["quality"].values()) / len(PROFILE["quality"])
v = sum(PROFILE["value"].values()) / len(PROFILE["value"])
print(f"technical quality mean {q:.2f} -> {'High' if q >= 3 else 'Low'}")
print(f"business value mean    {v:.2f} -> {'High' if v >= 3 else 'Low'}")
for k in ("rules_still_valid_pct", "alternative_fit_pct",
          "platform_end_of_support_months", "key_expert_leaving_months"):
    print(f"{k:32s}: {PROFILE[k]}")
