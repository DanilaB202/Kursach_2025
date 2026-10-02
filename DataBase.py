import sqlite3
DataBase = sqlite3.connect("Baranov308is.db")

cursor = DataBase.cursor()


cursor.execute("PRAGMA foreign_keys = ON;")

# Создание таблиц
cursor.executescript("""

CREATE TABLE IF NOT EXISTS Clients (
    ID_Client INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Phone TEXT,
    Email TEXT,
    Passport TEXT,
    Address TEXT
);

CREATE TABLE IF NOT EXISTS Staff (
    ID_Staff INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Login TEXT NOT NULL,
    Password TEXT NOT NULL,
    Email TEXT,
    Rank TEXT
);

CREATE TABLE IF NOT EXISTS Tours (
    ID_Tour INTEGER PRIMARY KEY AUTOINCREMENT,
    Country TEXT,
    City TEXT,
    Hotel TEXT,
    Start_date DATE,
    End_date DATE,
    Price REAL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
    ID_Order INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Client INTEGER,
    ID_Tour INTEGER,
    Status TEXT,
    Total_price REAL,
    Create_date DATE,
    FOREIGN KEY (ID_Client) REFERENCES Clients(ID_Client),
    FOREIGN KEY (ID_Tour) REFERENCES Tours(ID_Tour)
);

CREATE TABLE IF NOT EXISTS Payouts (
    ID_Payout INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Order INTEGER,
    Total_Price REAL,
    Payment_date DATE,
    Payment_type TEXT,
    FOREIGN KEY (ID_Order) REFERENCES Orders(ID_Order)
);

CREATE TABLE IF NOT EXISTS Reviews (
    ID_Review INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Client INTEGER,
    ID_Tour INTEGER,
    Rating INTEGER,
    Comment TEXT,
    Review_Date DATE,
    FOREIGN KEY (ID_Client) REFERENCES Clients(ID_Client),
    FOREIGN KEY (ID_Tour) REFERENCES Tours(ID_Tour)
    
);""")

cursor.execute("INSERT INTO Staff (Name, Email, Login, Password) VALUES (?, ?, ?, ?)",
               ("Админ", "admin@mail.ru", "admin", "123"))

cursor.execute("INSERT INTO Staff (Name, Email, Login, Password) VALUES (?, ?, ?, ?)",
               ("Менеджер", "Manager@mail.ru", "manager", "12345"))


DataBase.commit()
DataBase.close()