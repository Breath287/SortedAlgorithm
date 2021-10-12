import psutil

def getMemcpu():
    data = psutil.virtual_memory()
    # total memory, unit is defined by byte
    total = data.total
    print('total ', total)
    free = data.available
    print('free ', free)

    # memory usage
    memory = int(round(data.percent))
    print('memory: {}%'. format(memory))
    # cpu usage
    cpu = psutil.cpu_percent(interval=1)
    print('cpu: {}%'.format(cpu))




if __name__=='__main__':
    getMemcpu()