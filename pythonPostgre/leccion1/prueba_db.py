import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="ps2746",
    host="127.0.0.1",
    port=5433,
    database="test_python"
)

#cursor = conexion.cursor()
#sentencia = "SELECT * FROM persona"
#cursor.execute(sentencia)
#registros = cursor.fetchall()
#print(registros)

#cursor.close()
#conexion.close()

try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
            #llaves_primarias = ((1, 2),)
            #entrada = input("proporciona los ids a buscar")
            #llaves_primarias = (tuple(entrada.split(",")),)
            #cursor.execute(sentencia, llaves_primarias)
            #registros = cursor.fetchall()

            #for reistro in registros:
            #    print(reistro)

            #sentencia = "INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)"
            #valores = (
            #    ("Zaida", "Jasso", "zjasso@mail.com"),
            #    ("Fernanda", "Hernandez", "fhernandez@mail.com"),
            #    ("Valeria", "Romo", "vromo@mail.com")
            #)
            #cursor.executemany(sentencia, valores)

            #lo hace el bloque d ecodigo with
            #conexion.commit()

            #reistros_insertados = cursor.rowcount
            #print(f"registros insertado {reistros_insertados}")

            #sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s"
            #valores = ("Uriel", "Ramirez", "uramirez@mail.com", 3)
            #cursor.execute(sentencia, valores)
            #registros_actualizados = cursor.rowcount
            #print(f"registros actualizados {registros_actualizados}")

            #actulizar varios registros
            #sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s"
            #valores = (
            #    ("Noemi", "Gonzales", "ngonzales@mail.com", 3),
            #    ("Karla", "Juarez", "kjuarez@mail.com", 2),
            #)
            #cursor.executemany(sentencia, valores)
            #registros_actualizados = cursor.rowcount
            #print(f"registros actualizados {registros_actualizados}")

            sentencia = "DELETE FROM persona WHERE id_persona = %s"
            valores = (1,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f"registros eliminados {registros_eliminados}")
except Exception as e:
    print("ocurrio un error " + e)
finally:
    conexion.close()