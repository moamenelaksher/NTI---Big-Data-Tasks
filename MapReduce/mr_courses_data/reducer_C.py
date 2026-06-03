
import sys
import math

active_province = None
running_score_sum = 0
running_record_count = 0
collected_scores = []

for raw_line in sys.stdin:
    clean_line = raw_line.strip()

    province_name, score_str, count_str = clean_line.split("\t")

    current_score = float(score_str)
    current_count = int(count_str)

    if active_province == province_name:
        running_score_sum += current_score
        running_record_count += current_count
        collected_scores.append(current_score)

    else:
        if active_province is not None:
            mean_average = running_score_sum / running_record_count

            squared_diff_sum = sum((score - mean_average) ** 2 for score in collected_scores)
            variance = squared_diff_sum / running_record_count

            standard_deviation = math.sqrt(variance)

            print(f"{active_province}\t{running_record_count}\t{mean_average:.2f}\t{standard_deviation:.2f}")

        active_province = province_name
        running_score_sum = current_score
        running_record_count = current_count
        collected_scores = [current_score]

if active_province is not None:
    mean_average = running_score_sum / running_record_count

    squared_diff_sum = sum((score - mean_average) ** 2 for score in collected_scores)
    variance = squared_diff_sum / running_record_count

    standard_deviation = math.sqrt(variance)

    print(f"{active_province}\t{running_record_count}\t{mean_average:.2f}\t{standard_deviation:.2f}")