import matplotlib.pyplot as plt

# Definindo os horários (0h a 24h) e as temperaturas (valores fictícios)
horas = list(range(0, 25))  # Horas de 0h a 24h
temperaturas = [15, 17, 19, 22, 24, 26, 28, 30, 31, 32, 33, 33, 32, 30, 28, 26, 25, 23, 21, 20, 19, 18, 17, 16, 15]

# Criando o gráfico de linha
plt.plot(horas, temperaturas, marker='o', linestyle='-', color='b')

# Personalizando o gráfico
plt.title('Evolução da Temperatura Durante o Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.xticks(horas)  # Adicionando as horas no eixo X

# Exibindo o gráfico
plt.show()
