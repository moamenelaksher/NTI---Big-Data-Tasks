

import sys

for raw_line in sys.stdin:
    clean_line = raw_line.strip()

    if not clean_line:
        continue

    record_segments = clean_line.split("***")
    metric_score = float(record_segments[0])
    province_name = record_segments[1].split("_")[1]

    print(f"{province_name}\t{metric_score}\t1")