import sys
active_ip = None
running_total = 0

for line in sys.stdin:
    ip_address, line_count = line.strip().split('\t')
    line_count = int(line_count)

    if active_ip == ip_address:
        running_total += line_count
    else:
        if active_ip:
            print(f"{active_ip}\t{running_total}")

        active_ip = ip_address
        running_total = line_count

if active_ip:
    print(f"{active_ip}\t{running_total}")