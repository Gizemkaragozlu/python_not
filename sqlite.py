# import sqlite3 as sql
#
# # Tablo Oluşturma         -> CREATE TABLE tablo_ismi(col1 TEXT , col2 INT, col3 TEXT)
# # Bu tablom yoksa oluştur -> CREATE TABLE IF NOT EXISTS tablo_ismi(col1 TEXT , col2 INT, col3 TEXT)
# # Tabloyu Kayıt Atma      -> INSERT INTO tablo_ismi VALUE (val1, val2, val3)
# # Tablodan Veri Çekme     -> SELECT * FROM tablo_ismi
# # Tablodan şarlı veri     -> SELECT col1, col2, col3 FROM tablo_ismi WHERE col1 = val1
# # Tablo Veri Güncelleme   -> UPDATE tablo_ismi SET col1 = val1
# # Tablodan Veri Silme     -> DELETE FROM tablo_ismi WHERE col1 = val1
#
# con = sql.connect('student.db')
# #sql database oluşturuldu
#
# cur = con.cursor() # İmleci konumlandırmak için
#
# # cur.execute("CREATE TABLE IF NOT EXISTS grade (name TEXT, lesson TEXT, grade INT)")
#
# # # cur.execute("INSERT INTO grade VALUES ('Gizem', 'Matematik', 66)")
# # cur.execute("INSERT INTO grade VALUES ('Ayşe', 'Fizik', 95)")
# # cur.execute("INSERT INTO grade VALUES ('Ahmet', 'Matematik', 15)")
# # cur.execute("INSERT INTO grade VALUES ('Mehmet', 'Biyoloji', 100)")
# # Tablonun içerisine alan eklenir
#
# # con.commit()
# # run ediyoruz
#
# # cur.execute("SELECT * FROM grade")
# # Tablonun tüm kolonlarını çeker.
#
# # cur.execute("SELECT name, grade FROM grade")
# # Tablonun belli alanlarını çağırmak için kullanılır.
#
# #cur.execute("SELECT * FROM grade WHERE lesson = 'Matematik'")
# # Tablomun lesson alanının Matemetik olanlarını getirir.
#
# # cur.execute("UPDATE grade SET grade = 66 WHERE name = 'Gamze'")
# # grade alanı 66 olanları Gamze yap dedik.
# # con.commit()
#
# cur.execute("DELETE FROM grade WHERE grade = 66")
# # Tabloda grade alanı 66 olanları siler
# con.commit()
#
# cur.execute("SELECT * FROM grade")
# data = cur.fetchall() #datalarımızı almak için kullanırız
# #fetchall  kullanınca commit etmemize gerek kalmıyor.
#
# for line in data:
#     print(line)
#
# # print(data)
# con.close()