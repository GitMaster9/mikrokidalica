from pathlib import Path
import matplotlib.pyplot as plt
from tester import Tester

antun_podatci = Path("1_antun")
marin_podatci = Path("2_marin")
karlo_podatci = Path("3_karlo")
diana_podatci = Path("4_diana")

karlo = Tester(karlo_podatci, 56.0)

test = karlo.testovi[0]

plt.plot(test.strain, test.stress)

plt.xlabel('Strain [%]')
plt.ylabel('Stress [N/mm2]')

plt.show()