import numpy as np
from metadata import device_ids


device_features = np.zeros((1038, 120))

count = 0
for i in device_ids:
    device_data = np.loadtxt(open("./data/" + str(i) +".csv","rb"), delimiter=",")
    
    hist_x, bin_edgex = np.histogram(np.clip(device_data[:, 1], -15, 15), 40)
    hist_y, bin_edgey = np.histogram(np.clip(device_data[:, 2], -15, 15), 40)
    hist_z, bin_edgez = np.histogram(np.clip(device_data[:, 3], -15, 15), 40)


    device_features[i, :40] = np.double(hist_x) / device_data.shape[0]
    device_features[i, 40:80] = np.double(hist_y) / device_data.shape[0]
    device_features[i, 80:120] = np.double(hist_z) / device_data.shape[0]
    count += 1

    print "Devices trained : " + str(count)

"""
    device_features[i, 0] = np.mean(device_data[:, 1]) #mean_x
    device_features[i, 1] = np.mean(device_data[:, 2])
    device_features[i, 2] = np.mean(device_data[:, 3])
    device_features[i, 3] = np.std(device_data[:, 1]) #std_x
    device_features[i, 4] = np.std(device_data[:, 2])
    device_features[i, 5] = np.std(device_data[:, 3])
"""

np.savetxt("features2.csv", device_features, delimiter=",")
