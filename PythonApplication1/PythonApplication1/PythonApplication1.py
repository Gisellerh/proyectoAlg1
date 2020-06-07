import numpy as np
import matplotlib
import matplotlib.pyplot as plt

paises = ('USA','Brasil', 'Canadá','Perú','Ecuador','México','Chile','Rep.Dom.','Panamá','Colombia')
width = 0.5
arr_pais=np.arange(len(paises))

nuevos_casos = [22541,4613,1698,1182,1018,852,552,123,242,218]
nuevas_muertes = [1322,338,149,54,208,83,9,4,2,9]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots(figsize=(10,5))
barra1 = ax.bar(arr_pais - width/2, nuevos_casos, width,color='#990000', label='Nuevos casos confirmados')
barra2 = ax.bar(arr_pais + width/2, nuevas_muertes, width, color='#000000' , label='Nuevos fallecimientos')



ax.set_title('Reporte diario #100 de COVID-19 en los 10 paises más contagiados de America')
ax.set_xticks(arr_pais)
ax.set_ylabel('Casos')
ax.set_xticklabels(paises)
ax.legend()

def autolabel(barra):
    for rect in barra:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(barra1)
autolabel(barra2)

fig.tight_layout()

plt.show()