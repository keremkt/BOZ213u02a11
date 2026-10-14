hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

toplam_dakika = mins + dura
bitis_dakikasi = toplam_dakika % 60
bitis_saati = (hour + (toplam_dakika // 60)) % 24

print(str(bitis_saati) + ":" + str(bitis_dakikasi))
