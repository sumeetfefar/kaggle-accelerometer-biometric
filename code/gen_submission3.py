import numpy as np

from metadata import train_lengths, device_ids


device_features = np.loadtxt(open("features3.csv","rb"),delimiter=",")
seq_features = np.loadtxt(open("sequence_features3.csv","rb"),delimiter=",")


submission_file = open("submission3.csv", 'a')
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

        lon_m = seq_features[seq_id_int, 0]
        lat_m = seq_features[seq_id_int, 1]
        R_m = np.clip(seq_features[seq_id_int, 2], 5, 14.9)

        lon_bin = 20 + np.floor((4./36)*lon_m)
        lat_bin = 60 + np.floor((4./18)*lat_m)
        R_bin = 90 + np.floor(2*(R_m - 10))

        dev_id_features = device_features[dev_id_int, :]

        prob_lon = device_features[dev_id_int, lon_bin]
        prob_lat = device_features[dev_id_int, lat_bin]
        prob_R = device_features[dev_id_int, R_bin]

        #seq_id_features = seq_features[seq_id_int, :]

        #prob_x = np.sum((dev_id_features[:30]/np.sqrt(np.sum(dev_id_features[:30]**2)))*(seq_id_features[:30]/np.sqrt(np.sum(seq_id_features[:30]**2))))
        #prob_y = np.sum((dev_id_features[30:60]/np.sqrt(np.sum(dev_id_features[30:60]**2)))*(seq_id_features[30:60]/np.sqrt(np.sum(seq_id_features[:30]**2))))
        #prob_z = np.sum((dev_id_features[60:90]/np.sqrt(np.sum(dev_id_features[60:90]**2)))*(seq_id_features[60:90]/np.sqrt(np.sum(seq_id_features[:30]**2))))

        #prob_x = gaussian_probability(seq_features[seq_id_int, 0], device_features[dev_id_int, 0], device_features[dev_id_int, 3])
        #prob_y = gaussian_probability(seq_features[seq_id_int, 1], device_features[dev_id_int, 1], device_features[dev_id_int, 4])
        #prob_z = gaussian_probability(seq_features[seq_id_int, 2], device_features[dev_id_int, 2], device_features[dev_id_int, 5])


        posterior = prob_lat*prob_lon*prob_R*train_lengths[device_ids.index(dev_id_int)]
        #posterior = prob_lat*prob_lon*train_lengths[device_ids.index(dev_id_int)]
        
        submission_file.write(question_id + "," + str(posterior)+'\n')

        if int(question_id)%1000 == 0:
            print question_id

