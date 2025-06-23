import os, sys
files = ["index.html", "intro.html"]
missing = [f for f in files if not os.path.exists(f)]
if missing:
    print("Missing files: " + ", ".join(missing))
    sys.exit(1)
print("All HTML files found.")
