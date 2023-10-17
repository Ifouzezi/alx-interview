import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}

# Define a function to print the metrics
def print_metrics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")

# Define a function to reset the metrics
def reset_metrics():
    global total_file_size
    global status_code_counts
    total_file_size = 0
    status_code_counts = {}

# Handle keyboard interruption (CTRL + C)
def signal_handler(signal, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        # Parse the line with a regular expression
        import re
        match = re.match(r'^\S+ - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)
        if match:
            status_code, file_size = int(match.group(1)), int(match.group(2))
            total_file_size += file_size

            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    status_code_counts[status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics()
                reset_metrics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C) and print metrics
    print_metrics()
