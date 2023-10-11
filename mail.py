import smtplib
title = 'Subject:Mail Konu Başlığı'                      #mail konu başılığı
message = 'Merhaba bu bir test mailidir'                 #mail içeriği
content = title + '\n' + message
sender = 'gizemkaragozlu5@gmail.com'                      #gönderen mail adresi
password = 'suzcbjwrrvnlpoms'                             #gönderen mail şifresi(Not: Uygulama şifreleri ->diğer->bir ad verilir->oluştur->cihaz için uygulama şifreniz.)
to = 'gizemkaragozlu5@gmail.com'                          #kime gönderileceği
try:
    server = smtplib.SMTP("smtp.gmail.com",587)#host ve port
    server.ehlo()                                         #bağlantının başlatılamsı sağlanır
    server.starttls()                                     #bilgilerin şifrelenmesi sağlanır
    server.login(sender,password)                         #bağlantı kurulur
    server.sendmail(sender, to, content.encode('utf-8'))  #gönderilecek mail adresi,kime gönderilecek,mail içeriği
    #content.encode('utf-8') = Türkçe karakter hata vermesin diye yazılır
    server.close()#işimiz bitince kapat
except Exception as e:
    print('Hata:' +str(e))

#Not: hata veriyorsa mail adresiniz 3.şahıslara kapalıdır mail adresine gidilir,
# güvenlik daha az güvenli uygulama erişimi açık yapılır.

