# def multiplication_table(rows=13):
#     for i in range(rows):
#         print ' ' *(rows + 13) + 'i*1' *(rows)
# multiplication_table(13)

import pprint
n = 12
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
pprint.pprint(m)

max_width = len(str(m[-1][-1])) + 1
for i in m:
    i = [str(j).rjust(max_width) for j in i]
    print(''.join(i))