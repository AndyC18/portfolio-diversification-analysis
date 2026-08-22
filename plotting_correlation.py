import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from analyse_correlation import correlation_matrix, rolling_correlation_SPY_TLT

plt.figure()
x = np.array(rolling_correlation_SPY_TLT().index)
y = np.array(rolling_correlation_SPY_TLT().values)

plt.plot(x, y)
plt.axhline(0, color='red', linestyle='--', label='Zero Correlation')
plt.xlabel('Date')
plt.ylabel('Rolling Correlation')
plt.title('Correlation between SPY and TLT')
plt.legend()
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/spy_tlt_rolling_correlation.png', dpi=150, bbox_inches='tight')
# plt.show()

plt.figure()
ax =sns.heatmap(correlation_matrix(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Log Returns')
plt.savefig('figures/correlation_matrix.png', dpi=150, bbox_inches='tight')
plt.show()


