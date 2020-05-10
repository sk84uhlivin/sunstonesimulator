import random
import plotly.graph_objects as go

two_c = 0
three_c = 0
four_c = 0
sims = 30000
x_axis = ["2 Crystal", "3 Crystal", "4 Crystal"]
print()


def rolls():
    roll1 = random.randint(25, 65)
    roll2 = random.randint(25, 65)
    roll3 = random.randint(25, 65)
    roll4 = random.randint(25, 65)
    return roll1, roll2, roll3, roll4


for x in range(1, sims + 1):
    a, b, c, d = rolls()

    # 2 Crystal
    if a + b >= 100:
        two_c += 1

    # 3 Crystal
    elif a + b + c >= 100:
        three_c += 1

    # 4 Crystal
    else:
        four_c += 1

print("Generating media...")
# layout = go.Layout(legend={'traceorder': 'normal'}
# fig = go.Figure(data=[go.Pie(labels=x_axis, values=[two_c, three_c, four_c])])
fig = go.Figure()
fig.add_trace(go.Pie(labels=x_axis, values=[two_c, three_c, four_c], sort=False))
fig.update_layout(
    title=f"Sunstone Simulation - {sims} times",

    font=dict(
        family="Tahoma, sans-serif",
        size=18,
        color="#000000"
    ),

)
fig.show()

print(f"2 Crystals: {two_c}")
print(f"3 Crystals: {three_c}")
print(f"4 Crystals: {four_c}")

print(f"{sims} simulations.")
