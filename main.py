print("@lfyuy enj0y!")  

import requests
import random
import string
import threading

available_usernames = []
lock = threading.Lock()

def generate_random_4l():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(4))

def generate_random_4c():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(4))

def check_youtube_username(username):
    url = f"https://www.youtube.com/@{username}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            result = f"[available] {username} @lfyuy"
            print(result)
            with lock:
                available_usernames.append(username)
        else:
            print(f"[taken] {username} @lfyuy")
    except requests.RequestException:
        print(f"[wrong] {username} @lfyuy")

def worker(mode, count):
    for _ in range(count):
        if mode == "4l":
            username = generate_random_4l()
        else:
            username = generate_random_4c()
        check_youtube_username(username)

if __name__ == "__main__":
    mode = "4l"  
    total_checks = 100
    thread_count = 10
    checks_per_thread = total_checks // thread_count
    
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(mode, checks_per_thread))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("Available usernames")
    for name in available_usernames:
        print(name)
