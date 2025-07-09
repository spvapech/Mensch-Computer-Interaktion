import matplotlib.pyplot as plt
import numpy as np

gerät1 = np.random.normal(loc=50, scale=10, size=100)
gerät2 = np.random.normal(loc=55, scale=15, size=100)

plt.figure(figsize=(8, 6))
plt.boxplot(
    [gerät1, gerät2],
    tick_labels=['Eingabegerät 1', 'Eingabegerät 2'],
    showmeans=False
)

plt.title('Boxplot der beiden Eingabegeräte')
plt.ylabel('Messwerte')
plt.xlabel('Eingabegerät')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('boxplot_eingabegeraete.png')
plt.close()
