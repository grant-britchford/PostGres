from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

mydb = create_engine("postgresql:///chinook")

meta = MetaData(mydb)

artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key = True),
    Column("name", String)
)

album_table = Table(
    "album", meta,
    Column("album_id", Integer, Primary_Key = True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

track_table = Table(
    "track", meta,
    Column("track_id", Integer, Primary_Key = True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type", Integer, Primary_Key = False),
    Column("genre_id", Integer, Primary_Key = False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unitprice", Float)
)


with mydb.connect() as connection:
    select_query = artist_table.select()
    
    results = connection.execute(select_query)
    for result in results:
        print(result)