codes = ['aa99', 'xy4332', 'ab1111', 'pq3223']


def extract_num(v):
    return v[2:]


for n in sorted(codes, key=extract_num):
    print(n, end=' ')
