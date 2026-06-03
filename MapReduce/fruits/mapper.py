
import sys

for raw_line in sys.stdin:

    clean_line = raw_line.strip()  
    token_list = clean_line.split()
    for token in token_list:
       
        print('%s\t%s' % (token, "1"))