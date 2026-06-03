
import sys
import re

for raw_line in sys.stdin:
    normalized_line = raw_line.strip().lower()

    extracted_tokens = re.findall(r'\b\w+\b', normalized_line)

    for token in extracted_tokens:
        print(f"{token}\t1")