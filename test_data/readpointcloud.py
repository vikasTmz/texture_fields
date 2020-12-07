import numpy as np

oldpts = np.load('cc067578ad92517bbe25370c898e25a5/pointcloud_old.npz')
newpts = np.load('cc067578ad92517bbe25370c898e25a5/pointcloud.npz')

print(newpts["normals"][0:5])
print(oldpts["normals"][0:5])

print("==================================")

print(newpts["points"][0:5])
print(oldpts["points"][0:5])
