import plotly.express as px

from die import Die

# Cria dois dados d8
die_1 = Die(8)
die_2 = Die(8)

# Realiza alguns testes e armazena os resultados em uma lista
results = []
for roll_num in range(10_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
title = "Resultados de Rolar Dois D8 1.000 vezes"
labels = {"x": "Resultado", "y": "Frequencia do Resultado"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
