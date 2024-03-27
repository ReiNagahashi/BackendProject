import sys
import validator

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
    # 🚨argvには最初のpython3というコマンドは含まれていない
    if not validator.validator(sys.argv[1], len(sys.argv[1:])):
        print("Validation error: type correctly.")
        sys.exit(1)

    # reverseの実行
    reverse(sys.argv[2], sys.argv[3])

    # copyの実行
    copy(sys.argv[2], sys.argv[3])

    # dupulicate-contentsの実行
    dupulicateContents(sys.argv[2], sys.argv[3])

    # replace-stringの実行
    replaceString(sys.argv[2], sys.argv[3], sys.argv[4])



