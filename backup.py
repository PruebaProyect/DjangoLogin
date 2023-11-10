import sqlite3
import csv

# Conecta a la base de datos SQLite3
conn = sqlite3.connect('./db.sqlite3')
cursor = conn.cursor()

# Exporta los datos de la tabla a un archivo CSV
cursor.execute('SELECT * FROM app1_question')
rows = cursor.fetchall()
with open('backup_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(rows)

# Cierra la conexión a la base de datos
conn.close()

import sqlite3
import csv

# Crear o conectar a la base de datos SQLite3
conn = sqlite3.connect('./db.sqlite3')
cursor = conn.cursor()

# Leer el archivo CSV y almacenar los datos en la tabla
with open('backup_data.csv', 'r') as archivo_csv:
    datos_csv = csv.DictReader(archivo_csv)

    for fila in datos_csv:
        columna1 = fila['columna1']
        columna2 = fila['columna2']
        columna3 = fila['columna3']

        cursor.execute('''
            INSERT INTO mi_tabla (columna1, columna2, columna3)
            VALUES (?, ?, ?)
        ''', (columna1, columna2, columna3))

# Confirmar los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()