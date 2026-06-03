
import sys

active_token = None
running_total_count = 0

for raw_line in sys.stdin:
    clean_line = raw_line.strip()

    incoming_token, segment_count_str = clean_line.split("\t")
    segment_count = int(segment_count_str)

    if active_token == incoming_token:
        running_total_count += segment_count

    else:
        if active_token is not None:
            print(f"{active_token}\t{running_total_count}")

        active_token = incoming_token
        running_total_count = segment_count

if active_token is not None:
    print(f"{active_token}\t{running_total_count}")