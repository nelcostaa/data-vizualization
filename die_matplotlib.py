import matplotlib.pyplot as plt
from die import Die

# Cria dois dados d6
die_1 = Die(6)
die_2 = Die(6)

# Realiza alguns testes e armazena os resultados em uma lista
# Usa list comprehensions para declarar as listas
results = [die_1.roll() + die_2.roll() for roll_num in range(1_000_000)]

# Analisa os resultados
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

# Tambem usa list comprehensions nessa secao
frequencies = [results.count(value) for value in poss_results]

# Visualiza os resultados em um grafico
plt.style.use("seaborn-v0_8)
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies, color="green")

# Define o titulo do grafico e os eixos do rotulo
ax.set_title("Resultado de Dois D6 jogados 1.000.000 de vezes")
ax.set_xlabel("Resultado")
ax.set_ylabel("Frequencia do Resultado")

# Ajusta os limites do eixo x para começar em 2
ax.set_xlim(left=2, right=max_result)

# Define o tamanho dos rotulos
ax.tick_params(labelsize=14)

plt.show()
