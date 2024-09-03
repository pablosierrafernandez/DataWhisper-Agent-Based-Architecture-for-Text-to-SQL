from datetime import datetime
import json
import psycopg2
from psycopg2.sql import SQL, Identifier


from psycopg2 import sql

class PostgresManager:
    def __init__(self):
        self.conn = None
        self.cur = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def connect_ddbb(self, hostname, database, username, password, port):
       
        self.conn = psycopg2.connect(
            host=hostname,
            database=database,
            user=username,
            password=password,
            port=port
        )
      
        self.cur = self.conn.cursor()

        # Crear el rol de solo lectura si no existe
        self.cur.execute("DO $$ BEGIN IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'readonly') THEN CREATE ROLE readonly; END IF; END $$;")
        
        # Asignar permisos al rol de solo lectura
        self.cur.execute(sql.SQL("""
            GRANT CONNECT ON DATABASE {database} TO readonly;
            GRANT USAGE ON SCHEMA public TO readonly;
            GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
            ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly;
        """).format(database=sql.Identifier(database)))

        # Asignar el rol de solo lectura al usuario conectado
        self.cur.execute(sql.SQL("GRANT readonly TO {user};").format(user=sql.Identifier(username)))
        
        # Aplicar cambios
        self.conn.commit()


    def run_sql(self, sql) -> str:
        self.cur.execute("ROLLBACK;")
        if not "SELECT" in sql:
           
            raise ValueError("Solo se permiten consultas SELECT")
       
        self.cur.execute(sql)
        columns = [desc[0] for desc in self.cur.description]
        res = self.cur.fetchall()

        list_of_dicts = [dict(zip(columns, row)) for row in res]

        json_result = json.dumps(list_of_dicts, indent=4, default=self.datetime_handler)
        
        return json_result

    def datetime_handler(self, obj):
        """
        Handle datetime objects when serializing to JSON.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        return str(obj)  

    def get_table_definition(self, table_name):
        get_def_stmt = """
        SELECT pg_class.relname as tablename,
            pg_attribute.attnum,
            pg_attribute.attname,
            format_type(atttypid, atttypmod)
        FROM pg_class
        JOIN pg_namespace ON pg_namespace.oid = pg_class.relnamespace
        JOIN pg_attribute ON pg_attribute.attrelid = pg_class.oid
        WHERE pg_attribute.attnum > 0
            AND pg_class.relname = %s
            AND pg_namespace.nspname = 'public'  -- Assuming you're interested in public schema
        """
        self.cur.execute(get_def_stmt, (table_name,))
        rows = self.cur.fetchall()
        create_table_stmt = "CREATE TABLE {} (\n".format(table_name)
        for row in rows:
            create_table_stmt += "{} {},\n".format(row[2], row[3])
        create_table_stmt = create_table_stmt.rstrip(",\n") + "\n);"
        return create_table_stmt

    def get_all_table_names(self):
        get_all_tables_stmt = (
            "SELECT tablename FROM pg_tables WHERE schemaname = 'public';"
        )
        self.cur.execute(get_all_tables_stmt)
        return [row[0] for row in self.cur.fetchall()]

    def get_table_definitions_for_prompt(self, table_names=None):
        if table_names is None:
            table_names = self.get_all_table_names()
        definitions = []
        for table_name in table_names:
            definitions.append(self.get_table_definition(table_name))
        return "\n\n".join(definitions)

    def get_table_columns(self, table_name):
        self.cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = %s
        """, (table_name,))
        return [row[0] for row in self.cur.fetchall()]
