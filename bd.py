import sqlite3

def addPeople(user_id, score):
    base = sqlite3.connect('diyaFKN.db')
    cur = base.cursor()
    cur.execute('INSERT INTO data VALUES(?, ?)', (user_id, score))
    base.commit()
    base.close()

def getScorePeople(user_id):
    base = sqlite3.connect('diyaFKN.db')
    cur = base.cursor()
    read = cur.execute('SELECT score FROM data WHERE user_id == ?', (user_id,)).fetchone()
    base.close()
    return int(read[0])


def addScorePeople(user_id, score):
    base = sqlite3.connect('diyaFKN.db')
    cur = base.cursor()
    try:
        cur.execute('INSERT INTO data VALUES(?, ?)', (user_id, score))
        read = cur.execute('SELECT score FROM data WHERE user_id == ?', (user_id,)).fetchone()
        base.commit()
        base.close()
        return read
    except:
        prev_tuple = cur.execute('SELECT score FROM data WHERE user_id == ?', (user_id,)).fetchone()
        score += int(prev_tuple[0])
        cur.execute('UPDATE data SET score == ? WHERE user_id == ?', (score, user_id))
        read = cur.execute('SELECT score FROM data WHERE user_id == ?', (user_id,)).fetchone()
        base.commit()
        base.close()

def showTop():
    base = sqlite3.connect('diyaFKN.db')
    cur = base.cursor()
    read = cur.execute('SELECT * FROM data').fetchall()
    return read
    base.close()
