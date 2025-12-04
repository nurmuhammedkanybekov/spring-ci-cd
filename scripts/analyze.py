import os
import sys

def scan_code(directory):
    todo_count = 0
    print(f"Scanning directory: {directory}")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if "TODO" in line:
                                print(f"⚠️  TODO found in {file} at line {i+1}")
                                todo_count += 1
                except Exception as e:
                    print(f"Error reading {file}: {e}")

    return todo_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze.py <directory_to_scan>")
        sys.exit(1)

    project_dir = sys.argv[1]
    count = scan_code(project_dir)

    print("-" * 30)
    print(f"📊 Total TODOs found: {count}")
    
    if count > 5:
        print("FAILED: Too many TODOs left in the code! Clean up before shipping.")
        sys.exit(1)
    else:
        print("PASSED: Code looks clean enough.")
        sys.exit(0)