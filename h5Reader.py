import h5py, numpy
import matplotlib.pyplot as plt 

with h5py.File('Test2h5.h5', 'r') as f:
    data = f['gcFatJet_pt'][:]

data_1d = data.flatten()
data_real = data_1d[data_1d > 0]

plt.figure(figsize=(8, 5))
plt.hist(data_real, bins=100, color='skyblue', edgecolor='black', alpha=0.7)
# 3. Add labels and title
plt.title('Simple Histogram', fontsize=14, fontweight='bold')
plt.xlabel('Values')
plt.ylabel('Frequency')
# 4. Display the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(f'SPANetplots.png', dpi=300, bbox_inches='tight')
plt.show()