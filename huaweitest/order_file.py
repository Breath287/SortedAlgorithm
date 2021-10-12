file_path = '/automation/test_input.txt'
lis = []
date_map = {}
def get_data(path):
    with open(file_path, mode='r') as f:
        for line in f.readlines():
            line.strip()
            if line != "":
                word = line.split()
                flag = word[-1]
                number = word[-2]
                daytime = word[1]
                clocktime = word[2]
            time = daytime + " " + clocktime
            if number not in date_map:
                date_map[number] = ["", ""]
            if flag == 'start':
                date_map[number][0] = time
            if flag == 'end':
                date_map[number][1] = time
    return date_map







