import re
from collections import defaultdict, Counter

# Define the path to your log file
LOG_FILE_PATH = 'path/to/your/access.log'

# Regular expression pattern to parse the log lines (Common Log Format)
log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\S+)'
)

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

def analyze_log_file(log_file_path):
    ip_counter = Counter()
    page_counter = Counter()
    status_counter = Counter()

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            parsed_line = parse_log_line(line)
            if parsed_line:
                ip = parsed_line['ip']
                request = parsed_line['request']
                status = parsed_line['status']
                page = request.split()[1] if len(request.split()) > 1 else None

                ip_counter[ip] += 1
                if page:
                    page_counter[page] += 1
                status_counter[status] += 1

    return ip_counter, page_counter, status_counter

def print_summary(ip_counter, page_counter, status_counter):
    print("Top 10 IP addresses with the most requests:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count} requests")

    print("\nTop 10 most requested pages:")
    for page, count in page_counter.most_common(10):
        print(f"{page}: {count} requests")

    print("\nHTTP Status Codes:")
    for status, count in status_counter.items():
        print(f"{status}: {count} times")

    print("\nNumber of 404 errors:")
    print(status_counter.get('404', 0))

if __name__ == "__main__":
    ip_counter, page_counter, status_counter = analyze_log_file(LOG_FILE_PATH)
    print_summary(ip_counter, page_counter, status_counter)

