import numpy as np
import matplotlib.pyplot as plt

simulation_time = 24 * 600 
landing_arrival_rate = 3 / 60 
takeoff_arrival_rate = 1 / 60 
landing_time = 12  
takeoff_time = 4  
critical_fuel_prob = 0.01
critical_fuel_min = 5  
critical_fuel_max = 40 
max_landing_queue = 6  

current_time = 0
landing_queue = []
takeoff_queue = []
rejections = 0
total_idle_time = [0, 0, 0] 
max_idle_time = [0, 0, 0]  
landing_times = [[] for _ in range(3)]

np.random.seed(123)

while current_time < simulation_time:
    if np.random.poisson(landing_arrival_rate) > 0:
        critical_fuel_time = np.random.uniform(critical_fuel_min, critical_fuel_max)
        if len(landing_queue) < max_landing_queue:
            landing_queue.append(current_time + critical_fuel_time)
        else:
            rejections += 1

    if np.random.poisson(takeoff_arrival_rate) > 0:
        takeoff_queue.append(current_time)

    for i, plane in enumerate(landing_queue):
        if plane <= current_time:
            landing_times[i].append(current_time)
            landing_queue.pop(i)
            break

    if len(landing_queue) == 0:
        for _ in range(min(len(takeoff_queue), 3)):
            landing_times.append(current_time)
            takeoff_queue.pop(0)

    current_time += 1

num_planes = sum(len(landing_time) for landing_time in landing_times)
num_rejections = rejections
mean_air_time = np.mean([landing_time[-1] for landing_time in landing_times])
mean_landing_queue_length = np.mean([len(landing_time) for landing_time in landing_times])
critical_fuel_rejections = sum(
    1 for landing_time in landing_times if landing_time[-1] > landing_time[0] + critical_fuel_min
)
total_idle_time = np.sum(total_idle_time)
max_idle_time = np.max(max_idle_time)

print("Resultados de la simulación:")
print(f"Número de aviones: {num_planes}")
print(f"Número de rechazos: {num_rejections}")
print(f"Tiempo promedio de permanencia en el aire: {mean_air_time:.2f} minutos")
print(f"Longitud promedio de la cola de aterrizaje: {mean_landing_queue_length:.2f}")
print(f"Rechazos por combustible crítico: {critical_fuel_rejections}")
print(f"Tiempo total ocioso de cada pista: {total_idle_time}")
print(f"Tiempo máximo ocioso de cada pista: {max_idle_time}")

plt.plot(range(1, len(landing_times) + 1), [len(landing_time) for landing_time in landing_times])
plt.xlabel("Número de avión")
plt.ylabel("Longitud de la cola de aterrizaje")
plt.title("Longitud de la cola de aterrizaje en función del número de avión")
plt.show()





