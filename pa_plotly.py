import plotly.express as px
import plotly.graph_objects as go

from passeio_aleatorio import PasseioAleatorio

# Continua criando passeios novoos, desde que o programa esteja ativo
while True:
    # Cria um random walk
    rw = PasseioAleatorio(100_000)
    rw.preencher_passeio()

    # Plota os pontos no passeio
    title = "Grafico de um Random Walk com 100.000 pontos"
    point_numbers = range(rw.num_points)
    fig = px.scatter(
        x=rw.x_values,
        y=rw.y_values,
        color=point_numbers,
        color_continuous_scale="Blues",
        title=title,
    )

    fig.update_layout(yaxis=dict(visible=False, scaleanchor="x"))
    fig.update_layout(xaxis=dict(visible=False, scaleanchor="y"))

    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
