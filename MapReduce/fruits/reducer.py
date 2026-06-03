
from operator import itemgetter
import sys

frequency_registry = {}

for raw_line in sys.stdin:
    clean_line = raw_line.strip()
 
    term, occurrence_str = clean_line.split('\t', 1)

    try:
        occurrence_count = int(occurrence_str)
        frequency_registry[term] = frequency_registry.get(term, 0) + occurrence_count
    except ValueError:

        pass

ordered_frequencies = sorted(frequency_registry.items(), key=itemgetter(0))

for term, total_count in ordered_frequencies:
    print('%s\t%s' % (term, total_count))