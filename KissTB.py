import FuckedTB

print("FuckedTB module:", FuckedTB.__file__)
print("Available functions:", [
    name for name in dir(FuckedTB)
    if not name.startswith("_")
])

if hasattr(FuckedTB, "main") and callable(FuckedTB.main):
    FuckedTB.main()
elif hasattr(FuckedTB, "again") and callable(FuckedTB.again):
    FuckedTB.again()
else:
    print("Error: No callable main() or again() function found.")
