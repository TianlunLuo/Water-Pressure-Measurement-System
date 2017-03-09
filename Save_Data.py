import datetime

def write_to_csvfile(depth_float,pressure_float):

    # change local time into ISO 8601 format
    # which is the format required by ThingSpeak
    isoDate = datetime.datetime.now().isoformat()
    dt = datetime.datetime.now().isoformat()
    # initiate a List[] to store each
    # line in the csv file
    data_list = []
    # open a csv file and read whole
    # file into the List[]
    with open('data.csv') as csvData:
        for line in csvData:
            row = line.split(',')
            length = len (row)
            # create a List[] to store each
            # column in the line
            data = []
            for i in range(length):
                data.append(row[i])

            data_list.append(data)

    # take in the parameters and store it in the data_list
    # wait for writing to file
    newData = [dt, str(depth_float), str(pressure_float)]
    data_list.append(newData)

    csvData = open('data.csv','wb')

    line_list = []
    # write the entire list into the original csv file
    for row in data_list:
        line = ''
        for i in range(3):
            line = line + row[i] + ','

        line = line + '\n'
        line_list.append(line)

    csvData.writelines(line_list)
    csvData.close()

    print ("File saved successfully!")
