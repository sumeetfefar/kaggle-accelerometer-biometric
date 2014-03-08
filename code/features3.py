import numpy as np
from metadata import device_ids


device_features = np.zeros((1038, 100))

count = 0
for i in device_ids:
    device_data = np.loadtxt(open("./data/" + str(i) +".csv","rb"), delimiter=",")
    
    x = device_data[:, 1]
    y = device_data[:, 2]
    z = device_data[:, 3]

    lon = np.rad2deg(np.arctan2(y, x))
    lat = np.arctan2(z, np.sqrt(x*x+y*y))
    R = np.sqrt(x*x + y*y + z*z)

    hist_lon, bin_edgex = np.histogram(lon, 60)
    hist_lat, bin_edgey = np.histogram(lat, 60)
    hist_R, bin_edgez = np.histogram(np.clip(R, 5, 15), 20)


    device_features[i, :40] = np.double(hist_lon) / device_data.shape[0]
    device_features[i, 40:80] = np.double(hist_lat) / device_data.shape[0]
    device_features[i, 80:] = np.double(hist_R) / device_data.shape[0]
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

np.savetxt("features3.csv", device_features, delimiter=",")
