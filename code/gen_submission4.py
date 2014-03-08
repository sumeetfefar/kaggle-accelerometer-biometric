import numpy as np

from metadata import train_lengths, device_ids



device_features = np.zeros((1038, 20, 20, 20))

#count = 0
for i in device_ids:
    device_data = np.loadtxt(open("./data/" + str(i) +".csv","rb"), delimiter=",")

    #t = device_data[:, 0]
    #tsort = np.sort(t)

    """
    dt = t[1:] - t[:-1]
    dt_good = (dt > 0) & (dt < 1000)
    dt = dt[dt_good]

    mean_dt = np.double(np.sum(dt))/dt.shape[0]
    """

    hist, bin_edges = np.histogramdd(np.clip(device_data[:,1:], -15, 15), bins=20)
    #hist_x, bin_edgex = np.histogram(np.clip(device_data[:, 1], -15, 15), 40)
    #hist_y, bin_edgey = np.histogram(np.clip(device_data[:, 2], -15, 15), 40)
    #hist_z, bin_edgez = np.histogram(np.clip(device_data[:, 3], -15, 15), 40)


    #device_features[i, :40] = np.double(hist_x) / device_data.shape[0]
    #device_features[i, 40:80] = np.double(hist_y) / device_data.shape[0]
    #device_features[i, 80:120] = np.double(hist_z) / device_data.shape[0]
    #count += 1
    device_features[i] = hist

#device_features = np.loadtxt(open("features.csv","rb"),delimiter=",")
#seq_features = np.loadtxt(open("sequence_features12.csv","rb"),delimiter=",")


sequence_features1 = np.zeros((1000000, 3))

with open("test.csv") as test_file:
    temp = test_file.readline()
    #b_array = np.zeros((300))
    #c_array = np.zeros((300))
    #d_array = np.zeros((300))
    t_array = np.zeros((300))
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
            #t_array[count - 1] = np.double(a)

        elif count==300:
            b_array[count - 1] = np.double(b)
            c_array[count - 1] = np.double(c)
            d_array[count - 1] = np.double(d)
            #t_array[count - 1] = np.double(a)
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
            #dt = t_array[1:] - t_array[:-1]
            #dt_good = (dt > 0) & (dt < 1000)
            #dt = dt[dt_good]

            #mean_dt = np.double(np.sum(dt))/dt.shape[0]
            #sequence_features1[int(e)] = mean_dt
            count = 0
            if int(e) % 1000 == 0:
                print "Sequences done : " + e


submission_file = open("submission4.csv", 'a')
submission_file.write("QuestionId,IsTrue\n")

"""
def gaussian_probability(x, mean, std):
    return (1./(np.sqrt(2*np.pi)*std))*np.exp(-(((x - mean)/std)**2)/2)
"""

with open("questions.csv") as questions_file:
    temp = questions_file.readline()
    for line in questions_file:
        question_id, seq_id, dev_id = line.split(',')
        dev_id = dev_id[:-1]

        seq_id_int = int(seq_id)
        dev_id_int = int(dev_id)

        x_m = np.clip(seq_features[seq_id_int, 0], -15., 14.9)
        y_m = np.clip(seq_features[seq_id_int, 1], -15., 14.9)
        z_m = np.clip(seq_features[seq_id_int, 2], -15., 14.9)

        x_bin = 10 + np.floor((2./3)*x_m)
        y_bin = 10 + np.floor((2./3)*y_m)
        z_bin = 10 + np.floor((2./3)*z_m)
        """
        dev_dt = device_features[dev_id_int]
        seq_dt = seq_features[seq_id_int]
        prob = 1./(dev_dt - seq_dt)**2
        """

        prob_xyz = device_features[dev_id_int, x_bin, y_bin, z_bin]
        #prob_y = device_features[dev_id_int, y_bin]
        #prob_z = device_features[dev_id_int, z_bin]

        #seq_id_features = seq_features[seq_id_int, :]

        #prob_x = np.sum((dev_id_features[:30]/np.sqrt(np.sum(dev_id_features[:30]**2)))*(seq_id_features[:30]/np.sqrt(np.sum(seq_id_features[:30]**2))))
        #prob_y = np.sum((dev_id_features[30:60]/np.sqrt(np.sum(dev_id_features[30:60]**2)))*(seq_id_features[30:60]/np.sqrt(np.sum(seq_id_features[:30]**2))))
        #prob_z = np.sum((dev_id_features[60:90]/np.sqrt(np.sum(dev_id_features[60:90]**2)))*(seq_id_features[60:90]/np.sqrt(np.sum(seq_id_features[:30]**2))))

        #prob_x = gaussian_probability(seq_features[seq_id_int, 0], device_features[dev_id_int, 0], device_features[dev_id_int, 3])
        #prob_y = gaussian_probability(seq_features[seq_id_int, 1], device_features[dev_id_int, 1], device_features[dev_id_int, 4])
        #prob_z = gaussian_probability(seq_features[seq_id_int, 2], device_features[dev_id_int, 2], device_features[dev_id_int, 5])


        posterior = prob_xyz*train_lengths[device_ids.index(dev_id_int)]

        submission_file.write(question_id + "," + str(posterior)+'\n')

        if int(question_id)%1000 == 0:
            print question_id

