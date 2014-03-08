import numpy as np

from metadata import train_lengths, device_ids


device_features = np.loadtxt(open("features1.csv","rb"),delimiter=",")
seq_features = np.loadtxt(open("sequence_features1.csv","rb"),delimiter=",")


submission_file = open("submission1.csv", 'a')
submission_file.write("QuestionId,IsTrue\n")


def gaussian_probability(x, mean, std):
    return (1./(np.sqrt(2*np.pi)*std))*np.exp(-(((x - mean)/std)**2)/2)

with open("questions.csv") as questions_file:
    temp = questions_file.readline()
    for line in questions_file:
        question_id, seq_id, dev_id = line.split(',')
        dev_id = dev_id[:-1]

        seq_id_int = int(seq_id)
        dev_id_int = int(dev_id)

        prob_x = gaussian_probability(seq_features[seq_id_int, 0], device_features[dev_id_int, 0], device_features[dev_id_int, 3])
        prob_y = gaussian_probability(seq_features[seq_id_int, 1], device_features[dev_id_int, 1], device_features[dev_id_int, 4])
        prob_z = gaussian_probability(seq_features[seq_id_int, 2], device_features[dev_id_int, 2], device_features[dev_id_int, 5])

        posterior = prob_x*prob_y*prob_z*train_lengths[device_ids.index(dev_id_int)]

        submission_file.write(question_id + "," + str(posterior)+'\n')
