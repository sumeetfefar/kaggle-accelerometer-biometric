import numpy as np

from metadata import seq_ids_list

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
        #e_index = seq_ids_list.index(int(e))
        if count < 300:
            b_array[count - 1] = np.double(b)
            c_array[count - 1] = np.double(c)
            d_array[count - 1] = np.double(d)
        elif count==300:
            b_array[count - 1] = np.double(b)
            c_array[count - 1] = np.double(c)
            d_array[count - 1] = np.double(d)
            """
            hist_x, bin_edgex = np.histogram(np.clip(b_array, -15, 15), 30)
            hist_y, bin_edgey = np.histogram(np.clip(c_array, -15, 15), 30)
            hist_z, bin_edgez = np.histogram(np.clip(d_array, -15, 15), 30)

            sequence_features1[e_index, 0:30] = np.double(hist_x) / b_array.shape[0]
            sequence_features1[e_index, 30:60] = np.double(hist_y) / b_array.shape[0]
            sequence_features1[e_index, 60:90] = np.double(hist_z) / b_array.shape[0]
            """
            sequence_features1[int(e), 0] = np.mean(b_array)
            sequence_features1[int(e), 1] = np.mean(c_array)
            sequence_features1[int(e), 2] = np.mean(d_array)

            count = 0
            if int(e) % 1000 == 0:
                print "Sequence done : " + e

np.savetxt("sequence_features2.csv", sequence_features1, delimiter=",")
