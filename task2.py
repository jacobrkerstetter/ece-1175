import psutil

while True:
    # step 1: measure utilization ratio
    utils = []
    for x in range(3):
        utils.append(psutil.cpu_percent(interval=1, percpu=True))
        print('CPU{}: {}%'.format(x, utils[x]))
        
    # step 2: calculate nextFreq
    maxUtil = max(utils)
    print('max util: {}%'.format(maxUtil))

    nextFreq = 1.25 * maxFreq * maxUtil

    # step 3: set nextFreq