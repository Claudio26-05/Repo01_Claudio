import pandas as pd

data = {
    'Ciudad': ['Lima', 'Lima', 'Arequipa', 'Lima', 'Arequipa'],
    'Ventas': [100, 200, 150, 50, 300]
}

df = pd.DataFrame(data)

# Agrupamos por ciudad y sumamos las ventas
resultado = df.groupby('Ciudad')['Ventas'].sum()

print(resultado)
