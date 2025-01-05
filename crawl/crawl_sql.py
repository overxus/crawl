import sqlite3
import pandas as pd


class SqlTable:
    def __init__(self, name:str, columns:list[str], connection:sqlite3.Connection):
        """Never instantize it directly, use <OpenTable> or <CreateTable> to create a SqlTable"""
        self.name = name
        self.columns = columns
        self.con = connection
        self.cur = connection.cursor()
    
    def Execute(self, sql:str):
        return self.cur.execute(sql)
    
    def Commit(self):
        self.con.commit()
    
    def Insert(self, rows:list):
        if len(rows) > 0 and not (isinstance(rows[0], list) or isinstance(rows[0], tuple)):
            rows = [rows]
        place_holder = ', '.join(['?' for _ in range(len(self.columns))])
        self.cur.executemany(f'INSERT INTO {self.name} VALUES({place_holder})', rows)
        self.Commit()
    
    def Select(self, sql_after_where:str=None, select_field:str='*'):
        select_sql = f'SELECT {select_field} FROM {self.name}'
        if sql_after_where:
            select_sql += f' WHERE {sql_after_where}'
        q = self.Execute(select_sql)
        return q.fetchall()
    
    def Delete(self, sql_after_where:str):
        self.Execute(f'DELETE FROM {self.name} WHERE {sql_after_where}')
        self.Commit()

    def ToPandas(self, select_columns:list[str]=None):
        """query from sql table with given select fields
        Args:
            select_list: select fields
        """
        if select_columns:
            select_str = ', '.join(select_columns)
        else:
            select_str = '*'
            select_columns = self.columns
        rows = self.Select(select_field=select_str)
        return pd.DataFrame(rows, columns=select_columns)


class SqlConnection:
    def __init__(self, sql_file:str):
        self.con = sqlite3.connect(sql_file)
        self.cur = self.con.cursor()
        self.meta_dict = self._LoadMetaDict()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()
        return True
    
    def Close(self):
        self.con.close()
    
    def Execute(self, sql:str):
        return self.cur.execute(sql)
    
    def Commit(self):
        self.con.commit()

    def CreateTable(self, name:str, columns:list[str]):
        """create table in database
        Args:
            name: table name
            columns: table columns
        """
        if self.meta_dict.get(name):
            raise ValueError(f'table {name} already exists')
        self.meta_dict[name] = columns
        column_str = ', '.join(columns)
        self.Execute(f'CREATE TABLE {name}({column_str})')
        self.Execute(f'INSERT INTO meta_table VALUES("{name}", "{column_str}")')
        self.Commit()
        return self.OpenTable(name)

    def OpenTable(self, name:str):
        """query table from database
        Args:
            name: table name
        """
        if self.meta_dict.get(name, None) is None:
            raise ValueError(f'table {name} does not exists')
        return SqlTable(name, self.meta_dict[name], self.con)

    def DropTable(self, name:str):
        """drop table from database
        Args:
            name: table name
        """
        if self.meta_dict.get(name, None) is None:
            raise ValueError(f'table {name} does not exists')
        del self.meta_dict[name]
        self.Execute(f'DROP TABLE {name}')
        self.Execute(f'DELETE FROM meta_table WHERE name="{name}"')
        self.Commit()


    def _LoadMetaDict(self):
        q = self.Execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="meta_table"')
        if q.fetchall():
            meta_rows = self.Execute('SELECT * FROM meta_table').fetchall()
            return {
                meta_row[0] : [word.strip() for word in meta_row[1].split(',')]
                for meta_row in meta_rows
            }
        else:
            self.Execute(f'CREATE TABLE meta_table(name, columns)')
            return {}


def OpenSql(sql_file:str):
    return SqlConnection(sql_file)


if __name__ == "__main__":
    con = SqlConnection('test.db')
    table = con.OpenTable('stu')
    print(table.Select('id="张三"'))
    con.Close()
