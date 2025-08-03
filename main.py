import os
import time
import os
import schedule
import time
import subprocess

DB_SERVER=os.getenv("DB_SERVER", 'localhost')
DB_PORT=os.getenv("DB_PORT", '3306')
DB_NAMES = os.getenv("DB_NAMES", 'my_database')
DB_USER=os.getenv("DB_USER", 'root')
DB_PASS=os.getenv("DB_PASS", 'my_password')
HORA_BKP = os.getenv("HORA_BKP", "00:00")
DB_DUMP_TARGET = os.getenv("DB_DUMP_TARGET", "/tmp")
RUN_ONCE=os.getenv("RUN_ONCE", 'true')
# if using one database... ('database1',)


def get_dump(database):
    filestamp = time.strftime('%Y-%m-%d_%I-%M-%S')
    # D:/xampp/mysql/bin/mysqldump for xamp windows
    fileFullName = DB_DUMP_TARGET + '/' +database+"_"+filestamp+".sql"
    cmd = "mysqldump --add-drop-database --databases %s -h %s -P %s -u %s -p%s > %s" % (database, DB_SERVER,DB_PORT,DB_USER,DB_PASS,fileFullName)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    os.popen("gzip %s" % (fileFullName)).read()
    print("\n|| Database dumped to "+fileFullName+".gz ||")


def rodar():
    #for database in databases:
    get_dump(DB_NAMES)

if __name__=="__main__":
    if(RUN_ONCE == 'true'):
        schedule.every().minute.do(rodar)
    else:
        schedule.every().day.at(HORA_BKP).do(rodar)
    while True:
        schedule.run_pending()
        time.sleep(1)