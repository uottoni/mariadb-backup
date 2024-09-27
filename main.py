import configparser
import os
import time
import getpass
import os
import schedule
import time

HOST=os.getenv("HOST", 'cloud.rznet.com.br')
PORT=os.getenv("PORT", '3369')
DB_USER=os.getenv("DB_USER", 'root')
DB_PASS=os.getenv("DB_PASS", '@@#123SqL')
HORA_BKP = os.getenv("HORA_BKP", "00:00")
DST_BKP = os.getenv("DST_BKP", "/tmp")

# if using one database... ('database1',)
databases=['solcontroldb_dev']

def get_dump(database):
    filestamp = time.strftime('%Y-%m-%d-%I')
    # D:/xampp/mysql/bin/mysqldump for xamp windows
    os.popen("mysqldump -h %s -P %s -u %s -p%s %s > %s.sql" % (HOST,PORT,DB_USER,DB_PASS,database,DST_BKP+database+"_"+filestamp))
    
    print("\n|| Database dumped to "+database+"_"+filestamp+".sql || ")


def rodar():
    for database in databases:
        get_dump(database)

if __name__=="__main__":
    schedule.every().day.at(HORA_BKP).do(rodar)