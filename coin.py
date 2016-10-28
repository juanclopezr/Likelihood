import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n=30
k = 100000
success = 0
failure = 0

for i in range(100000):
    heads = 0.
    tails = 0.
    for j in range(n):
        temp = np.random.random()
        if(temp<=0.5):
            heads += 1.
        else:
            tails += 1.
    if(heads>=22.):
        success += 1.
    else:
        failure += 1.

print success/k
print failure/k
print (success+failure)/k



grades = np.array([81,69,74,61,56,87,69,65,66,44,62,69,84,72,57,46,63,76,99,91])
ave = []

for i in range(k):
    np.random.shuffle(grades)
    ave.append(np.mean(grades[:8])-np.mean(grades[8:]))

#plt.hist(ave)
#plt.show()

phi = np.random.random(5000)*2*np.pi
costheta = np.random.random(5000)*2-1
theta = np.arccos(costheta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.sin(theta)*np.cos(phi)
y = np.sin(theta)*np.sin(phi)
z = costheta

ax.scatter(x,y,z, s=1)
plt.show()
