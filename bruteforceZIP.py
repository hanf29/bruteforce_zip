import pyzipper

def brute_force_zip(zip_file, wordlist_file):
    try:
        with open(wordlist_file, "r") as wordlist:
            passwords = wordlist.readlines()
    except FileNotFoundError:
        print(f"[!] File wordlist '{wordlist_file}' tidak ditemukan.")
        return

    try:
        with pyzipper.AESZipFile(zip_file) as zf:
            namelist = zf.namelist()
            for password in passwords:
                password = password.strip()
                print(f"[~] Mencoba password: {password}")
                try:
                    zf.read(namelist[0], pwd=bytes(password, 'utf-8'))
                    print(f"[+] Password ditemukan: {password}")
                    return
                except:
                    print(f"[-] Password salah: {password}")
    except FileNotFoundError:
        print(f"[!] File ZIP '{zip_file}' tidak ditemukan.")
    except:
        print(f"[!] File ZIP rusak atau tidak valid.")

    print("[-] Password tidak ditemukan di wordlist.")

if __name__ == "__main__":
    zip_file = "VBG Kuliah Umum.zip"
    wordlist_file = "listpw.txt"
    brute_force_zip(zip_file, wordlist_file)