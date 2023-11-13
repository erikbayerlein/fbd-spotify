import psycopg2 as ps

conn = ps.connect(database = "fbd_spotify", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

