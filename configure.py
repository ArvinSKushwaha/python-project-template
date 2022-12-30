#!/bin/env python3

import shutil

if __name__ == "__main__":
    # Get package name
    package_name = input("Enter package name: ").strip()
    description = input("Enter package description: ").strip().encode().decode("unicode_escape")
    long_desc = input("Enter long description: ").strip().encode().decode("unicode_escape")
    keywords = ",".join([f"'{i.encode().decode('unicode_escape')}'" for i in input("Enter keywords (separated by comma): ").strip().split(',')])

    replacements = {
        '<name>': package_name,
        '<description>': description,
        '<long-desc>': long_desc,
        "'<keywords...>'": f"[{keywords}]",
    }

    shutil.copyfile("setup.py", "setup.py.bak")
    with open("setup.py.bak", "r") as r, open("setup.py", "w") as w:
        for line in r:
            for src, target in replacements.items():
                line = line.replace(src, target)
            w.write(line)

    shutil.move("src/<name>", f"src/{package_name}")
