import pymssql

"""
使用 pymssql 對資料庫進行連接
"""
server = "misdb01.database.windows.net"
database = "free-sql-db-6993718"
user = "dbeng"
password = "abc-12345"   
'''密碼洩漏問題'''



"""建立表

CREATE TABLE [dbo].[股票] (
    [ID]    INT             IDENTITY (1, 1) NOT NULL,
    [Sid]   CHAR (4)        NOT NULL,
    [sname] VARCHAR (30)    NOT NULL,
    [price] DECIMAL (16, 2) NOT NULL,
    [pdate] DATETIME        CONSTRAINT [DEFAULT_股票_pdate] DEFAULT (getdate()) NOT NULL,
    CONSTRAINT [PK_股票] PRIMARY KEY CLUSTERED ([ID] ASC)
);



"""




connect = pymssql.connect(server, user, password, database)
print("db登入成功")