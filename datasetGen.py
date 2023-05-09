import pandas as pd
import random

# Generar datos aleatorios
# Generar datos aleatorios
tipos = ['Cherry', 'Raf', 'Kumato', 'Pera', 'Corazon de buey']
ubicaciones = ['Almeria', 'El Ejido', 'Roquetas de Mar', 'Adra', 'Nijar']
tamaños = [random.randint(1000, 10000) for _ in range(5000)]
rendimientos = ['malo','medio','bueno','muy bueno']
fertilizantes = ['NPK', 'abono organico', 'abono foliar', 'abono liquido', 'abono granulado']
usos_fertilizantes = [random.choice(fertilizantes) for _ in range(5000)]

# Crear DataFrame
import pandas as pd
df = pd.DataFrame({
    'tipo': [random.choice(tipos) for _ in range(5000)],
    'ubicacion': [random.choice(ubicaciones) for _ in range(5000)],
    'tamano': tamaños,
    'rendimiento': [random.choice(rendimientos) for _ in range(5000)],
    'fertilizante': usos_fertilizantes
})

# Guardar datos en CSV
df.to_csv('datos_an.csv', index=False)
