import subprocess
import os
import sqlite3 as sl


def GetUUID() :
    cmd = 'wmic csproduct get uuid'
    try :
        from subprocess import DEVNULL
    except ImportError :
        DEVNULL = os.open(os.devnull, os.O_RDWR)

    uuid = str(subprocess.check_output(cmd, stdin=DEVNULL, stderr=DEVNULL))
    pos1 = uuid.find("\\n") + 2
    uuid = uuid[pos1 :-15]
    return ''.join(uuid.split('-'))


def create_user(con, uuid):
    # First time running
    sql = 'INSERT INTO USER (id, name) values(?, ?)'
    data = [(1, uuid)]
    con.executemany(sql, data)
    con.commit()


def test_activation() -> bool:
    UUID = GetUUID()
    con = sl.connect('test.db')
    with con:
        data = con.execute("SELECT * FROM USER WHERE id == 1;")
        res = data.fetchall()
        print(res)

    if len(res) == 0:
        create_user(con, UUID)
        print("new user added")
    elif res[0][1] != UUID:
        con.close()
        return False

    con.close()
    return True


if __name__ == "__main__":
    con = sl.connect('test.db')
    con.cursor().execute("DELETE FROM USER;", )
    con.commit()


