import sqlite3



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class OpenDB(object):
    """
    Simple CM for sqlite3 databases. Commits everything at exit.
    """
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()
        return self.cursor
    
    
    def __get_columns__(self):
        return [item[0] for item in self.cursor.description]
    
    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()