def raqamlar_yigindisi(son):
    """Kiritilgan sonning raqamlarini qo'shib chiquvchi funksiya"""
    dastlabki_son = son
    yigindi = 0

    while son > 0:
        oxirgi_raqam = son % 10
        yigindi += oxirgi_raqam
        son = son // 10

    print(f"{dastlabki_son} sonining raqamlar yig'indisi: {yigindi}")

raqamlar_yigindisi(256)


def mehmonlar_royxati():
    """Maksimal 3 ta mehmonni ro'yxatga oluvchi funksiya"""
    mehmonlar = []
    while len(mehmonlar) < 3:
        ism = input(f"{len(mehmonlar) + 1}-mehmonning ismini kiriting: ")
        mehmonlar.append(ism)
        print(f"{ism} muvaffaqiyatli qo'shildi.")

    print("Joy to'ldi! Ro'yxatga olingan mehmonlar:")
    for mehmon in mehmonlar:
        print(f"- {mehmon}")

mehmonlar_royxati()

def rozilik_sorash():
    """Foydalanuvchidan faqat 'ha' yoki 'yo'q' javobini qabul qiluvchi funksiya"""
    while True:
        javob = input("Dasturni davom ettiramizmi? (ha / yo'q): ").lower()

        if javob == "ha":
            print("Ajoyib, davom etamiz! 🚀")
            break
        elif javob == "yo'q":
            print("Dastur to'xtatildi. 🛑")
            break
        else:
            print("Xato kiritish! Iltimos, faqat 'ha' yoki 'yo'q' deb yozing. X")

rozilik_sorash()


def tub_sonni_aniqla(son):
    """Berilgan son tub yoki murakkabligini aniqlovchi funksiya"""
    if son < 2:
        print(f"{son} tub ham, murakkab ham emas.")
        return

    boluvchi = 2
    tub = True

    while boluvchi <= son // 2:
        if son % boluvchi == 0:
            tub = False
            break
        boluvchi += 1

    if tub:
        print(f"{son} — TUB son! 💎")
    else:
        print(f"{son} — MURAKKAB son! ✖️")

tub_sonni_aniqla(17)
tub_sonni_aniqla(20)


def harorat_konverteri():
    """Harorat o'lchovlarini o'zgartiruvchi interaktiv menyu"""
    while True:
        print("--- HARORAT O'GIRGICH ---")
        print("1. Selsiy -> Farangeyt (°C -> °F)")
        print("2. Farangeyt -> Selsiy (°F -> °C)")
        print("3. Chiqish")

        tanlov = input("Tanlovingiz (1,2,3): ")

        if tanlov == "1":
            celsius = float(input("Selsiy gradusini kiriting: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"Natija: {celsius}°C = {round(fahrenheit, 2)}°F")
        elif tanlov == "2":
            fahrenheit = float(input("Farangeyt gradusini kiriting: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"Natija: {fahrenheit}°F = {round(celsius, 2)}°C")
        elif tanlov == "3":
            print("Konverter yopildi. Salomat bo'ling!")
            break
        else:
            print("Noto'g'ri menyu tanlandi! Qayta urinib ko'ring.")
harorat_konverteri()
