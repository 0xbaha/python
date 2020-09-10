# How do you split a list into evenly sized chunks?

import pprint

def chunks(l, n):
    # Yield successive n-sized chunks from l.
    for i in range(0, len(l), n):
        yield l[i:i + n]

pprint.pprint(list(chunks(range(10, 125), 10)))


# OUTPUT #
# D:\Git\learn-py\examples>python split-list.py
# [range(10, 20),
#  range(20, 30),
#  range(30, 40),
#  range(40, 50),
#  range(50, 60),
#  range(60, 70),
#  range(70, 80),
#  range(80, 90),
#  range(90, 100),
#  range(100, 110),
#  range(110, 120),
#  range(120, 125)]
#
# D:\Git\learn-py\examples>
