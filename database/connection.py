import sqlite3

def iniciar_banco():
    conn = sqlite3.connect('corridas.db')
    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()

    cursor.execute('CREATE TABLE  IF NOT EXISTS tenis (tenis_id INTEGER PRIMARY KEY AUTOINCREMENT, tenis TEXT )')


    #Colunas: id, teis_id, distancia, tempo, data
    cursor.execute('CREATE TABLE IF NOT EXISTS corridas (id INTEGER PRIMARY KEY AUTOINCREMENT, tenis_id INTEGER REFERENCES tenis(tenis_id), distancia REAL, tempo REAL, data TEXT)')
    
    cursor.execute("SELECT * FROM corridas")
    resultado = cursor.fetchall()
    if len(resultado) == 0:
        cursor.execute("INSERT INTO tenis VALUES (NULL,'Asics Nimbus 25')")
        cursor.execute("INSERT INTO tenis VALUES (NULL,'Fila Carbon 2')")
        cursor.execute("INSERT INTO tenis VALUES (NULL,'Mizuno Wave Rider 27')")
        cursor.execute("INSERT INTO corridas VALUES (NULL, 2, 9510, 3207, '2026-05-12')")
        cursor.execute("INSERT INTO corridas VALUES (NULL, 1, 9270, 3501, '2026-050-24')")
        cursor.execute("INSERT INTO corridas VALUES (NULL, 3, 8700, 3304, '2026-05-20')")
        cursor.execute("INSERT INTO corridas VALUES (NULL, 2, 10010, 3216, '2026-05-14')")

    conn.commit()
    conn.close()