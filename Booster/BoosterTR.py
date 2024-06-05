import os
import time


def show_wifi_profiles():
    os.system("netsh wlan show profile")
    network_name = input("Ağ adını girin: ")
    os.system(f'netsh wlan show profile "{network_name}" key=clear | findstr "Key Content"')


def show_weather(location):
    os.system(f'curl wttr.in/{location}')


def generate_qr_code(link):
    os.system(f'curl qrenco.de/{link}')


def clear_cache():
    os.system('del /q /f /s %temp%\\*')
    os.system('del /s /q C:\\Windows\\temp\\*')


def show_fun():
    os.system('curl ascii.live/forrest')


def clear_policies():
    os.system('reg delete "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies" /f')
    os.system('reg delete "HKLM\\Software\\Microsoft\\WindowsSelfHost" /f')
    os.system('reg delete "HKLM\\Software\\Policies" /f')
    os.system('reg delete "HKLM\\Software\\WOW6432Node\\Microsoft\\Policies" /f')
    os.system('reg delete "HKLM\\Software\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies" /f')
    os.system('reg delete "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware')
    os.system('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies" /f')
    os.system('reg delete "HKCU\\Software\\Microsoft\\WindowsSelfHost" /f')
    os.system('reg delete "HKCU\\Software\\Policies" /f')
    os.system('reg delete "HKLM\\Software\\Microsoft\\Policies" /f')


def create_power_scheme():
    os.system('powercfg /duplicatescheme E9A42B02-D5DF-448D-AA00-03F14749Eb61')


def optimize_windows():
    os.system('sfc /scannow')
    os.system('DISM /online /cleanup-image /checkhealth')
    os.system('DISM.exe /online /cleanup-image /scanhealth')
    os.system('DISM.exe /online /cleanup-image /restorehealth')


def free_space():
    os.system('cipher /w:c:')


def activate_windows():
    os.system('slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
    os.system('slmgr.vbs /skms kms.lotro.cc')
    os.system('slmgr.vbs /ato')


def main():
    while True:
        print("1. WIFICrack(Laptop)")
        print("2. Hava Durumu")
        print("3. Linkin QR Kodunu Oluştur")
        print("4. Önbelleği Temizle")
        print("5. Eğlence")
        print("6. Windows Politikalarını Temizleme")
        print("7. Performans Güç Ayarı Oluşturma")
        print("8. Windows İyileştirici Hızlandırıcı(5-10-15dk)")
        print("9. Bilgisayarda Alan Açma(1 saat+)")
        print("10. Windows Etkinleştirme")
        print("11. Çıkış")

        choice = input("Seçiminizi yapın (1-11): ")

        if choice == "1":
            show_wifi_profiles()
        elif choice == "2":
            location = input("Lokasyonu girin: ")
            show_weather(location)
        elif choice == "3":
            link = input("Oluşturulacak QR kodu için linki girin: ")
            generate_qr_code(link)
        elif choice == "4":
            clear_cache()
            print("Bilgisayarın önbelleği başarıyla temizlendi.")
        elif choice == "5":
            show_fun()
        elif choice == "6":
            clear_policies()
            print("Windows politikaları başarıyla temizlendi.")
        elif choice == "7":
            create_power_scheme()
            print("Performans güç ayarı oluşturuldu.")
        elif choice == "8":
            optimize_windows()
            print("Windows iyileştirici başarıyla çalıştırıldı.")
        elif choice == "9":
            free_space()
            print("Bilgisayarda alan başarıyla açıldı.")
        elif choice == "10":
            activate_windows()
            print("Windows etkinleştirme başarıyla gerçekleştirildi.")
        elif choice == "11":
            print("Temizleniyor...")
            time.sleep(3)
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
