# https://www.hackerrank.com/challenges/re-split/tutorial

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))