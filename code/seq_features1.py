import numpy as np

sequence_features1 = np.zeros((1000000, 3))

with open("test.csv") as test_file:
    temp = test_file.readline()
    b_array = np.zeros((300))
    c_array = np.zeros((300))
    d_array = np.zeros((300))

    count = 0
    for line in test_file:
        count = count + 1
        a,b,c,d,e = line.split(',')
        e = e[:-1]
        if count < 300:
            b_array[count - 1] = np.double(b)
            c_array[count - 1] = np.double(c)
            d_array[count - 1] = np.double(d)
        elif count==300:
            b_array[count - 1] = np.double(b)
            c_array[count - 1] = np.double(c)
            d_array[count - 1] = np.double(d)
            sequence_features1[e, 0] = np.mean(b_array)
            sequence_features1[e, 1] = np.mean(c_array)
            sequence_features1[e, 2] = np.mean(d_array)
            count = 0

np.savetxt("sequence_features1.csv", sequence_features1, delimiter=",")
