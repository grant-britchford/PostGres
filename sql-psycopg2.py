import psycopg2


connection = psycopg2.connect(database="chinook")


cursor = connection.cursor()


#cursor.execute('SELECT * FROM "artist"')


#cursor.execute('SELECT "name" FROM "artist"')


#cursor.Execute('SELECT * FROM "Artist" WHERE "Artist_id" = %s', [51])


#cursor.execute('SELECT * FROM "album" where "artist_id" = %s', [51])


cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

results = cursor.fetchall()


#results = cursor.fetchone()


connection.close()



for result in results:
    print(result)