import pyodbc
import random
import time

server = "localhost"   # 改成你的 SQL Server
database = "股票爬蟲"

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

INS_SQL = """
INSERT INTO dbo.股票 (sid, sname, price)
VALUES (?, ?, ?)

"""

try:
    for i in range(1, 30):
        rp = random.randint(1850, 1905)

        cursor.execute(INS_SQL, ("2330", "TSMC", rp))
        conn.commit()

        print(f'第{i}次擷取, 金額 {rp}')

        if i < 29:
            time.sleep(3)

    print("資料寫入完畢")

except Exception as e:
    print(f'連線失敗: 原因 {e}')

finally:
    cursor.close()
    conn.close()