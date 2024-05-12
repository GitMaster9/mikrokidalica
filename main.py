from pathlib import Path
import matplotlib.pyplot as plt
from tester import Tester

# antun_podatci = Path("1_antun")
# marin_podatci = Path("2_marin")
karlo_podatci = Path("3_karlo")
# diana_podatci = Path("4_diana")

tester = Tester(karlo_podatci, 56.0, 300)

test = tester.testovi[0]

granica_grafa = 2500

plt.figure()
plt.plot(test.strain[:granica_grafa], test.stress[:granica_grafa])
plt.xlabel('Strain [%]')
plt.ylabel('Stress [N/mm2]')
plt.title('Stress-Strain Curve')
plt.axvline(x=test.strain_elasticity[-1], color='r', linestyle='--')
plt.show()

print(f"Modul elastičnosti: {test.modulus:.2e} Pa")