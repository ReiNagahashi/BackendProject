import markdown
import sys
import validator

def fileConverter(inputPath, outputPath):
    with open(inputPath) as f:
        html = markdown.markdown(f.read())
    with open(outputPath, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    # 🚨argvには最初のpython3というコマンドは含まれていない
    if not validator.validator(sys.argv[1], len(sys.argv[1:])):
        print("Validation error: type correctly.")
        sys.exit(1)
    fileConverter(sys.argv[2],sys.argv[3])