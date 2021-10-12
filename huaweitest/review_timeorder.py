from dateutil.parser import parse


data = {}
col = []


def get_data():
    with open(r'/Users/jieli/Desktop/python_project2/huaweitest/test_input.txt', 'r') as f:
        # read file line by line
        lines = f.readlines()
        for line in lines:
            # remove space at the beginning and the end
            line = line.strip()
            # put non-empty line into the dictionary
            if len(line) != 0:
                symbols = line.split()
                flags = symbols[-1]
                nums = symbols[-2]
                daytime = symbols[0]
                clocktime = symbols[1]
                realtime = daytime + ' ' + clocktime
                if nums not in data:
                    data[nums] = ['', '']
                if flags == 'start':
                    data[nums][0] = realtime
                elif flags == 'end':
                    data[nums][1] = realtime
    return data


def refine_data(datetime):
    for key, value in datetime.items():
        # filter the value only containing the start or end time
        if datetime[key][0] == '' or datetime[key][1] == '':
            continue
        # parse the start and the end time, then calculate the time difference
        time_start = parse(datetime[key][0])
        time_end = parse(datetime[key][1])
        # for better output, parse the time difference into microsecond
        time_difference = int((time_end - time_start).microseconds/1000)
        pair = (time_difference, key)
        col.append(pair)
    return col


def get_rank(lis):
    # sort the list in descending order by the list[1]
    lis.sort(reverse=True)
    # print the number first, then elapsed time
    for item in lis:
        print(item[1], end=' ')
        print(item[0])
        print('')


if __name__ == '__main__':
    get_data()
    refine_data(data)
    get_rank(col)
