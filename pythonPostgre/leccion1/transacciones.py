import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="ps2746",
    host="127.0.0.1",
    port=5433,
    database="test_python"
)

try:
    conexion.autocommit = False

    cursor = conexion.cursor()
    setencia = "INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)"
    valores = ("Maria", "Esparza", "mesperanza@mail.com")
    cursor.execute(setencia, valores)
    setencia = "UPDATE persona SEt nombre=%s, apellido=%s, email=%s WHERE id_persona = %s"
    valores = ("Noemi", "Muñoz", "mmuñoz@gmail.com", 3)
    cursor.execute(setencia, valores)
    conexion.commit()
except Exception as e:
    conexion.rollback()
    print("ocurrio un error se hizo rollback" + e)
finally:
    conexion.close()