if __name__ == '__main__': 
    cutoff = 37 
    with open('./tinyshevchenko.txt', 'r') as f: 
        lines = f.readlines() 
    filter_lines = [line for line in lines if len(line.rstrip('\n')) <= cutoff]

    with open('./tinyshevchenko.txt', 'w') as f: 
        f.write(''.join(filter_lines)) 


# # HOW THE CUTOFF NUMBER WAS FOUND: 
# import numpy as np

# if __name__ == '__main__':
#     with open('./tinyshevchenko.txt', 'r') as f:
#         lines = f.readlines()
#     len_lines = np.array([len(line.rstrip('\n')) for line in lines])
#     print('lines count: ', len(lines))
#     print('mean: ', int(len_lines.mean()))
#     for p, v in zip([50, 90, 95, 99, 100], np.percentile(len_lines, [50, 90, 95, 99, 100])):
#         print(f'p{p}: {v:.0f}')
#     # gives: 
#     # lines count:  22728
#     # mean:  21
#     # p50: 21
#     # p90: 28
#     # p95: 30
#     # p99: 37
#     # p100: 1542