import matplotlib.pyplot as plt

from passeio_aleatorio import PasseioAleatorio

# Continua crinado passeios novoos, desde que o programa esteja ativo
while True:
    # Cria um random walk
    rw = PasseioAleatorio(5000)
    rw.fill_walk()

    # Plota os pontos no passeio
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(
        rw.x_values,
        rw.y_values,
        linewidth=5,
    )
    ax.set_aspect("equal")

    # Destaca o primeiro e o ultimo ponto
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
