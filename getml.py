#!/usr/bin/env python3
# Fetch the latest Arch "mirrorlist" from the packaging repo.
# Importable: fetch() returns the text. As a script: writes ./mirrorlist.
import urllib.request

LINK = "https://gitlab.archlinux.org/archlinux/packaging/packages/pacman-mirrorlist/-/raw/main/mirrorlist"

def fetch():
        with urllib.request.urlopen(LINK) as data:
                return data.read().decode()

if __name__ == "__main__":
        text = fetch()
        with open("mirrorlist", "w") as f:
                f.write(text)
        print(f"wrote mirrorlist ({len(text)} bytes)")
