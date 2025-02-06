import numpy as np
import matplotlib.pyplot as plt

# Параметры кривой
total_time = 100  # Общее время (или уровень игры)
trend_increase = 0.1  # Скорость общего роста сложности
wave_amplitude = 1    # Амплитуда колебаний (глубина спадов и высота пиков)
wave_frequency = 0.05  # Частота волн (количество циклов)

# Создаем массив времени или уровней
time = np.linspace(0, total_time, 1000)

# Вычисляем сложность
difficulty = trend_increase * time + wave_amplitude * np.sin(wave_frequency * time * 2 * np.pi)
print(difficulty)
# График кривой сложности
plt.plot(time, difficulty, label="Wave-shaped Difficulty Curve")
plt.title("Difficulty Curve with Peaks and Valleys")
plt.xlabel("Time / Level")
plt.ylabel("Difficulty")
plt.legend()
plt.grid(True)
plt.show()