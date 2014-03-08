import os
from metadata import device_ids


os.mkdir('data')

# create files
for i in device_ids:
    f = open("./data/" +str(i)+".csv", 'w')
    f.close()



with open("train.csv") as train_file:
    temp = train_file.readline()
    prev_e = "7"
    user_file = open("./data/" + "7" +".csv", "a")
    for line in train_file:
        a,b,c,d,e = line.split(',')
        e = e[:-1]
        if e == prev_e:
        #with open("/media/ankit/E/kaggle/accbio/code/numpy/data/" + e +".csv", "a") as user_file:
            user_file.write(a + "," + b + "," + c + "," + d + '\n')
        else:
            user_file = open("./data/" + e +".csv", "a")
            prev_e = e


