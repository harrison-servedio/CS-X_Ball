from ball import ball

import matplotlib.pyplot as plt

iterations = 10

oliverJohn = ball("Blue")

for _ in range(iterations):
    oliverJohn.step()

fig, ax = plt.subplots()

plt.plot(oliverJohn.Xs, oliverJohn.Ys, color=oliverJohn.color)
plt.plot(oliverJohn.Xs[-1], oliverJohn.Ys[-1], marker="o", markersize=8, markeredgecolor=oliverJohn.color, markerfacecolor=oliverJohn.color)
plt.axis('equal')
plt.axis([-300, 300, -300, 300])

plt.show()