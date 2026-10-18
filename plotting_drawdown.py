import matplotlib.pyplot as plt
from cum_return_and_max_drawdown import compute_drawdown

plt.figure(figsize=(10, 6))
SPY_drawdowns = compute_drawdown()['SPY']
plt.plot(SPY_drawdowns.index, SPY_drawdowns.values)
plt.title('SPY drawdown')
plt.xlabel('Date')
plt.ylabel('Drawdown')
plt.savefig('figures/spy_drawdown.png', dpi=150, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6))
TLT_drawdowns = compute_drawdown()['TLT']
plt.plot(TLT_drawdowns.index, TLT_drawdowns.values)
plt.title('TLT drawdown')
plt.xlabel('Date')
plt.ylabel('Drawdown')
plt.savefig('figures/tlt_drawdown.png', dpi=150, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6))
GLD_drawdowns = compute_drawdown()['GLD']
plt.plot(GLD_drawdowns.index, GLD_drawdowns.values)
plt.title('GLD drawdown')
plt.xlabel('Date')
plt.ylabel('Drawdown')
plt.savefig('figures/gld_drawdown.png', dpi=150, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6))
EFA_drawdowns = compute_drawdown()['EFA']
plt.plot(EFA_drawdowns.index, EFA_drawdowns.values)
plt.title('EFA drawdown')
plt.xlabel('Date')
plt.ylabel('Drawdown')
plt.savefig('figures/efa_drawdown.png', dpi=150, bbox_inches='tight')
plt.show()



