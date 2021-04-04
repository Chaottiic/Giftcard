# Imports
import itertools
import settings

# List of possible codes.
# This works as, if you can not tell if it's B or 8.
# If you know the letter, place it alone.
# Dashes are not required.
codes = list(
    itertools.product(
        ["B", "8"],
        ["1"],
        ["Q", "0"],
        ["S", "5"],
        ["-"],
        ["Y", "V"],
        ["A"],
        ["B"],
        ["9", "7"],
        ["-ABCD-ABCD"]
    )
)

codes = list(map(''.join, codes))
output = f"Possible Codes - {len(codes)}\n- " + \
    '\n\n- '.join([str(elem) for elem in codes])

if settings.WRITE == "FILE":
    with open(settings.FILE, "w" if settings.OVERWRITE else "a") as file:
        file.write(output)
        file.close()
    print(f"Successfully wrote to {settings.FILE}")
elif settings.WRITE == "CONSOLE":
    print(output)
