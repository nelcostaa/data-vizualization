import plotly.express as px

from die import Die

# Cria tres dados d6
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Realiza alguns testes e armazena os resultados em uma lista
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
title = "Resultados de Rolar Tres D6 1.000.000 vezes"
labels = {"x": "Resultado", "y": "Frequencia do Resultado"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Personaliza ainda mais o grafico
# Faz com que as marcacoes aparecam a cada 1 invervalo no grafico
fig.update_layout(xaxis_dtick=1)

fig.show()
