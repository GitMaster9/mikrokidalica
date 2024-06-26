from pathlib import Path
import matplotlib.pyplot as plt
from tester import Tester

# antun_podatci = Path("1_antun")
marin_podatci = Path("2_marin")
# karlo_podatci = Path("3_karlo")
# diana_podatci = Path("4_diana")

tester = Tester(marin_podatci, 54.0, 150)
print(tester)

tester.boxplot_cvrstoca()
tester.boxplot_elasticnost()
tester.graf_testa(redni_broj=1)
