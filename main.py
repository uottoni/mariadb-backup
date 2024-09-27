import configparser
import os
import time
import getpass
import os
import schedule
import time

DB_SERVER=os.getenv("HOST", 'cloud.rznet.com.br')
DB_PORT=os.getenv("PORT", '3369')
DB_NAMES = os.getenv("DB", 'solcontroldb_dev')
DB_USER=os.getenv("DB_USER", 'root')
DB_PASS=os.getenv("DB_PASS", '@@#123SqL')
HORA_BKP = os.getenv("HORA_BKP", "00:00")
DB_DUMP_TARGET = os.getenv("DST_BKP", "/tmp")

# if using one database... ('database1',)
databases=['solcontroldb_dev']

def get_dump(database):
    filestamp = time.strftime('%Y-%m-%d-%I')
    # D:/xampp/mysql/bin/mysqldump for xamp windows
    os.popen("mysqldump -h %s -P %s -u %s -p%s %s > %s.sql" % (DB_SERVER,DB_PORT,DB_USER,DB_PASS,database,DB_DUMP_TARGET+database+"_"+filestamp))
    
    print("\n|| Database dumped to "+database+"_"+filestamp+".sql || ")


def rodar():
    #for database in databases:
    get_dump(DB_NAMES)

if __name__=="__main__":
    schedule.every().day.at(HORA_BKP).do(rodar)
    while True:
        schedule.run_pending()
        time.sleep(1)