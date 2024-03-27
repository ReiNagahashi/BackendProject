import sys

def reverse(inputPath, outputPath):
    with open(inputPath) as f:
        contents = f.read()
    with open(outputPath, 'w') as f:
        f.write(contents[::-1])

def copy(inputPath, outputPath):
    with open(inputPath) as f:
        contents = f.read()
    with open(outputPath, 'w') as f:
        f.write(contents)

def dupulicateContents(inputPath, n):
    with open(inputPath) as f:
        contents = f.read() * n
    with open(inputPath, 'w') as f:
        f.write(contents)

def replaceString(inputPath, originString, newString):
    with open(inputPath) as f:
        contents = f.read()
    with open(inputPath, 'w') as f:
        f.write(contents.replace(originString, newString))


if __name__ == "__main__":
    # if not validator():
    # reverse(sys.argv[2], sys.argv[3])
    # copy(sys.argv[2], sys.argv[3])
    # dupulicateContents(sys.argv[2], 5)
    replaceString(sys.argv[2], "ll", "kk")



