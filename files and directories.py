from pathlib import Path
path = Path()
for file in path.glob("*.py"):
    print(file)
# Absolute path
# relative path
path = Path("ecommerce")
print(path.exists())  # exists method checks the presence of a directory
# print(path.mkdir())  # to make a directory
# print(path.rmdir())  # this is to remove a directory
# glob method ro search files in a directory

