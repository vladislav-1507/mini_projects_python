import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Входные данные
total = 105  # Руда | Железо | Витамины
ruda = 64  # Руда
ferr = 41  # Железо
vit = 36  # Витамины
ferr_vit = 27  # Железо & Витамины
ruda_vit = 0  # Руда & Витамины

# Вычисляем Железо & Руда
ferr_ruda = ruda + ferr + vit - ruda_vit - ferr_vit - total
print(f"Количество страниц по запросу Железо & Руда: {ferr_ruda} (тыс.)")

# Расчет для venn3
all = 0 # пересечение трех множеств
ruda_only = ruda - all - ruda_vit - ferr_ruda  # только руда
ferr_only = ferr - all - ferr_vit - ferr_ruda  # только феррит
vit_only = vit - all - ruda_vit - ferr_vit  # только витамины
ruda_vit_not_ferr = ruda_vit - all  # руда и витамины, но не феррит
ferr_ruda_not_vit = ferr_ruda - all  # феррит и руда, но не витамины
ferr_vit_not_ruda = ferr_vit - all  # феррит и витамины, но не руда

# Построение диаграммы Венна
venn3(subsets=(ruda_only, ferr_only, ferr_ruda_not_vit, vit_only, ruda_vit_not_ferr, ferr_vit_not_ruda, all),
          set_labels=("Руда", "Феррит", "Витамины"))
plt.show()
