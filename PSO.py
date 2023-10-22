import random
from sympy import symbols
from sympy import lambdify
from sympy import sympify
import matplotlib.pyplot as plt
import numpy as np

# Clase para representar una partícula en el enjambre
class Particle:
    def __init__(self, initial_position):
        self.position = initial_position
        self.velocity = random.uniform(-1, 1)
        self.best_position = self.position

def Solution():
    print("")
    x = symbols('x')
    fn = sympify(input('Ingresa la función objetivo: '))
    f = lambdify(x, fn)
    obj = input("¿Cuál es el objetivo de la función (Max - Min)?: ")
    num_particles = int(input("¿Cuántas particulas deseas usar para el problema?: "))
    max_iterations = int(input("¿Cuántas iteraciones desea realizar?: "))
    xl = float(input("Ingresa el valor menor del rango de posición inicial de las particulas: "))
    xu = float(input("Ingresa el valor mayor del rango de posición inicial de las particulas: "))
    c1 = 2.0  # Factor de aprendizaje cognitivo
    c2 = 2.0  # Factor de aprendizaje social
    inertia = 0.5  # Factor de inercia
    swarm = [Particle(random.uniform(xl, xu)) for _ in range(num_particles)]
    global_best_position = PSO(max_iterations, swarm, inertia, c1, c2, f, obj, num_particles, xl, xu, fn)
    print("Mejor posición encontrada:", global_best_position)
    print("Valor óptimo:", f(global_best_position))

def PSO(max_iterations, swarm, inertia, c1, c2, f, obj, num_particles, xl, xu, fn):
    particle_positions_history = [[] for _ in range(num_particles)]
    if obj == "Max" or obj == "max":
        global_best_position = max(swarm, key=lambda particle: f(particle.position)).position
    if obj == "Min" or obj == "min":
        global_best_position = min(swarm, key=lambda particle: f(particle.position)).position
    for iteration in range(max_iterations):
        for i, particle in enumerate(swarm):
            # Actualizar la velocidad y posición de la partícula
            particle.velocity = inertia * particle.velocity + c1 * random.random() * (particle.best_position - particle.position) + c2 * random.random() * (global_best_position - particle.position)
            particle.position += particle.velocity
            particle_positions_history[i].append(particle.position)
            if obj == "Max" or obj == "max":
                # Actualizar la mejor posición personal de la partícula
                if f(particle.position) > f(particle.best_position):
                    particle.best_position = particle.position
                # Actualizar la mejor posición global del enjambre
                if f(particle.position) > f(global_best_position):
                    global_best_position = particle.position
            if obj == "Min" or obj == "min":
                # Actualizar la mejor posición personal de la partícula
                if f(particle.position) < f(particle.best_position):
                    particle.best_position = particle.position
                # Actualizar la mejor posición global del enjambre
                if f(particle.position) < f(global_best_position):
                    global_best_position = particle.position
    num_particles_to_plot = 20
    particles_to_plot_indices = random.sample(range(num_particles), num_particles_to_plot)
    plt.figure(figsize=(8, 6))
    for i in particles_to_plot_indices:
        plt.plot(range(max_iterations), particle_positions_history[i], label=f'Partícula {i + 1}')
    plt.xlabel('Iteraciones')
    plt.ylabel('Posición')
    plt.title('Evolución de las partículas en PSO')
    plt.legend(loc='upper left', bbox_to_anchor=(0.98, 1))
    plt.show()
    print(" ")
    plt.figure(figsize=(8, 6))
    xpts = np.linspace(global_best_position - 10, global_best_position + 10)
    plt.plot(xpts, f(xpts))
    plt.title("Gráfica de la función " + str(fn))
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(global_best_position, f(global_best_position), c="red")
    plt.annotate("Optimo global " + str((global_best_position, f(global_best_position))), xy=(global_best_position, f(global_best_position)+0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()

    return global_best_position

Solution()
