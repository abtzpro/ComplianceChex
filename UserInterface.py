import sqlite3

def get_records(table):
    conn = sqlite3.connect('information_security.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM {table}")
    records = c.fetchall()

    conn.close()

    return records

def add_record(table, values):
    conn = sqlite3.connect('information_security.db')
    c = conn.cursor()

    placeholders = ', '.join(['?' for _ in range(len(values))])
    c.execute(f"INSERT INTO {table} VALUES ({placeholders})", values)

    conn.commit()
    conn.close()

def edit_record(table, id, values):
    conn = sqlite3.connect('information_security.db')
    c = conn.cursor()

    placeholders = ', '.join([f'{col}=?' for col in values.keys()])
    values_list = list(values.values())
    values_list.append(id)

    c.execute(f"UPDATE {table} SET {placeholders} WHERE id=?", values_list)

    conn.commit()
    conn.close()

def delete_record(table, id):
    conn = sqlite3.connect('information_security.db')
    c = conn.cursor()

    c.execute(f"DELETE FROM {table} WHERE id=?", (id,))

    conn.commit()
    conn.close()

# example usage
assets = get_records('information_assets')
print(assets)

add_record('policies', ('Acceptable Use Policy', 'Defines rules for using organization\'s information resources'))
edit_record('procedures', 1, {'name': 'Incident Response Plan', 'description': 'Defines the steps to be taken in the event of a security incident'})
delete_record('roles', 2)
