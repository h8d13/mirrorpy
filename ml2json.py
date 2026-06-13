#!/usr/bin/env python3
# Convert the Arch "mirrorlist" file to JSON: {country: [url, ...]}.
import re
import json
import argparse

import getml

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--stats", action="store_true", help="print summary stats instead of JSON")
ap.add_argument("--no-fetch", action="store_true", help="parse local mirrorlist instead of fetching latest")
ap.add_argument("-o", "--out", metavar="FILE", help="write JSON to FILE instead of stdout")
args = ap.parse_args()

if args.no_fetch:
        lines = open("mirrorlist")
else:
        lines = getml.fetch().splitlines()

data, country = {}, None
for line in lines:
        if m := re.match(r'## (\S.*)', line):
                country = m[1].strip()
        elif s := re.search(r'Server\s*=\s*(\S+)', line):
                data.setdefault(country, []).append(s[1])

if args.stats:
        total = sum(len(v) for v in data.values())
        top = max(data, key=lambda k: len(data[k]))
        print(f"countries: {len(data)}")
        print(f"mirrors:   {total}")
        print(f"largest:   {top} ({len(data[top])})")
elif args.out:
        with open(args.out, "w") as f:
                json.dump(data, f, indent=2)
        print(f"wrote {args.out} ({len(data)} countries)")
else:
        print(json.dumps(data, indent=2))
