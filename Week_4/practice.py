import numpy as np
mu = 0
sigma = 1
N = 1000

mean=np.zeros(N)
for i in range(N):
    r2 = np.random.normal(mu,sigma,N)
    mean[i]=np.mean(r2)
import matplotlib.pyplot as plt

err_sim = np.std(mean)
err_std = sigma/N**0.5
print(err_sim)
print(err_std)
def err(N):
    mean=np.zeros(N)
    for i in range(N):
        r2 = np.random.normal(mu,sigma,N)
        mean[i]=np.mean(r2)
    err_sim = np.std(mean)
    err_std = sigma/N**0.5
    return err_sim, err_std
n = np.linspace(0,1000,1000)
x = []
y = []
y2 = []
for i in range(1000):
    x.append(i+1)
    a,b =err(i+1)
    y.append(a)
    y2.append(b)

plt.plot(x,y,label='Monte')
plt.plot(x,y2,label='Theoretical')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='best')
