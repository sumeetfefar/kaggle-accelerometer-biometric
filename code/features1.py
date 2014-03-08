import numpy as np
from metadata import device_ids


device_features = np.zeros((1038, 6))

for i in device_ids:
    device_data = np.loadtxt(open("./data/" + str(i) +".csv","rb"), delimiter=",")
    device_features[i, 0] = np.mean(device_data[:, 1]) #mean_x
    device_features[i, 1] = np.mean(device_data[:, 2])
    device_features[i, 2] = np.mean(device_data[:, 3])
    device_features[i, 3] = np.std(device_data[:, 1]) #std_x
    device_features[i, 4] = np.std(device_data[:, 2])
    device_features[i, 5] = np.std(device_data[:, 3])

np.savetxt("features1.csv", device_features, delimiter=",")
