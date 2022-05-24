import pandas as pd
import sqlite3
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

df = pd.read_csv("data/twitter.csv", index_col=0)

def create_db(df):
    connection = sqlite3.connect("data/tweets_thebridge.db")
    crsr = connection.cursor()
    
    query = """
    CREATE TABLE USERS (
        Id_autor int (25),
        Nombre varchar (30),
        Username varchar (30),
        PRIMARY KEY ("Id_autor")
    );
    """
    crsr.execute(query)
    
    for index, row in df.iterrows():        
        crsr.execute("""INSERT or IGNORE INTO USERS (Id_autor, Nombre, Username) values(?,?,?)""", (row.Id_autor, row.Nombre_autor, row.username_autor))
    
    query = """
    CREATE TABLE TWEET (
        ID_TWEET int (25),
        Texto varchar (500),
        Fecha varchar (30),
        Id_autor int (25),
        N_Retweet int (5),
        N_Reply int (5),
        N_Like int (5),
        N_Quote int (5),
        PRIMARY KEY ("ID_TWEET"),
        CONSTRAINT "FK_TWEET.Id_autor"
            FOREIGN KEY ("Id_autor")
                REFERENCES "USERS"("Id_autor")
    );
    """

    crsr.execute(query)
    for index, row in df.iterrows():
        crsr.execute("""INSERT INTO TWEET (ID_TWEET, Texto, Fecha, Id_autor, N_Retweet, N_Reply, N_Like, N_Quote) values(?,?,?,?,?,?,?,?)""", (row.Id_tweet, row.Texto, row.Fecha, row.Id_autor, row.N_Retweet, row.N_Reply, row.N_Like, row.N_Quote))
    
    connection.commit()
    connection.close()
    return "DB creada"

create_db(df)