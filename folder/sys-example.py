import sys


if len(sys.argv) == 1:
    print("Error!")
    sys.exit(1)

print(sys.argv)
print ("Working...")

file_path = sys.argv[1]
print(file_path)