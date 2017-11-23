from QuantLib import *
import matplotlib.pyplot as plt
import numpy as np



sigma = 0.1
a = 0.1
timestep = 360
length = 30 # in years
forward_rate = 0.05
day_count = Thirty360()
todays_date = Date(15, 1, 2015)
        
        
        
        
        
Settings.instance().evaluationDate = todays_date
spot_curve = FlatForward(todays_date, QuoteHandle(SimpleQuote(forward_rate)), day_count)
spot_curve_handle = YieldTermStructureHandle(spot_curve)
        
        
        
hw_process = HullWhiteProcess(spot_curve_handle, a, sigma)
        
        
rng = GaussianRandomSequenceGenerator(UniformRandomSequenceGenerator(timestep, 
UniformRandomGenerator()))
        
        
seq = GaussianPathGenerator(hw_process, length, timestep, rng, False)
        
        
def generate_paths(num_paths, timestep): 
 arr = np.zeros((num_paths, timestep+1))
 for i in range(num_paths):
	sample_path = seq.next()
	path = sample_path.value()
	time = [path.time(j) for j in range(len(path))] 
	value = [path[j] for j in range(len(path))] 
	arr[i, :] = np.array(value)
	return np.array(time), arr




num_paths = 10
time, paths = generate_paths(num_paths, timestep) 
for i in range(num_paths):
            plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()