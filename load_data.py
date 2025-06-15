import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('temperature-readings.csv')

engine = create_engine('postgresql://postgres:admin123@localhost:5432/iot_db')
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")