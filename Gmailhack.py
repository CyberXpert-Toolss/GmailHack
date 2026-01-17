#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import sys
import os
from datetime import datetime

class GmailAccessTool:
    def __init__(self):
        self.target_email = ""
        self.password_found = "senha123@"
        self.total_attempts = 0
        self.session_id = random.randint(100000, 999999)
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = """
    ____                 _ _ _   _            _    
   / ___|_ __ ___   __ _(_) | | | | __ _  ___| | __
  | |  _| '_ ` _ \ / _` | | | |_| |/ _` |/ __| |/ /
  | |_| | | | | | | (_| | | |  _  | (_| | (__|   < 
   \____|_| |_| |_|\__,_|_|_|_| |_|\__,_|\___|_|\_\\
                                                  
        """
        print("\033[92m" + banner + "\033[0m")
        print("\033[93m" + "="*60 + "\033[0m")
        print("\033[93m[*] GMail Access Tool v3.1 - Active Session: {}\033[0m".format(self.session_id))
        print("\033[93m[*] Connection: TOR + Proxy Chain Active\033[0m")
        print("\033[93m" + "="*60 + "\033[0m\n")
    
    def typewriter_effect(self, text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def animated_loading(self, duration=3, text="Loading"):
        chars = ["⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻", "⣽"]
        end_time = time.time() + duration
        
        print(f"\033[94m[*] {text}", end="", flush=True)
        
        while time.time() < end_time:
            for char in chars:
                if time.time() > end_time:
                    break
                sys.stdout.write(f"\r\033[94m[*] {text} {char}")
                sys.stdout.flush()
                time.sleep(0.1)
        print("\r\033[94m[*] " + text + " [DONE]\033[0m")
    
    def get_target(self):
        print("\n" + "="*60)
        self.typewriter_effect("\033[96m[?] Enter target GMail address:\033[0m", 0.02)
        
        while True:
            email = input("\033[96m[>] \033[0m").strip()
            if '@gmail.com' in email.lower():
                self.target_email = email
                break
            else:
                self.typewriter_effect("\033[91m[!] Invalid GMail format. Use: user@gmail.com\033[0m", 0.01)
        
        print()
        self.animated_loading(2, f"Scanning {email}")
        
        self.typewriter_effect(f"\033[92m[+] Target acquired: {email}\033[0m", 0.02)
        self.typewriter_effect("\033[92m[+] Google API endpoint detected\033[0m", 0.02)
        self.typewriter_effect("\033[92m[+] Authentication service mapped\033[0m", 0.02)
        
        return email
    
    def generate_fake_ip(self):
        return f"{random.randint(100, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    def simulate_brute_force(self):
        print("\n" + "="*60)
        self.typewriter_effect("\033[95m[+] INITIATING BRUTE FORCE SEQUENCE\033[0m", 0.02)
        print("\033[95m" + "="*60 + "\033[0m\n")
        
        proxy_ip = self.generate_fake_ip()
        start_time = datetime.now().strftime("%H:%M:%S")
        
        self.typewriter_effect(f"\033[96m[*] Start time: {start_time}\033[0m", 0.01)
        self.typewriter_effect(f"\033[96m[*] Proxy chain: {proxy_ip}:443 -> TOR Node -> {self.generate_fake_ip()}:8080\033[0m", 0.01)
        self.typewriter_effect("\033[96m[*] Bypassing Google security protocols...\033[0m", 0.01)
        self.typewriter_effect("\033[96m[*] Rate limit: 5 requests/sec (max safe threshold)\033[0m", 0.01)
        self.typewriter_effect("\033[96m[*] Using hybrid dictionary+mask attack\033[0m", 0.01)
        
        time.sleep(2)
        print()
        
        common_passwords = [
            "123456", "password", "123456789", "12345678",
            "12345", "1234567", "senha", "password123",
            "admin", "123123", "qwerty", "abc123",
            "111111", "1234", "iloveyou", "000000",
            "senha123", "batman", "superman", "teste123",
            "password1", "1234567890", "sunshine", "princess",
            "football", "monkey", "charlie", "donald",
            "harley", "hunter", "mustang", "soccer"
        ]
        
        total_duration = 60
        attempts_per_second = random.randint(2, 5)
        total_attempts_possible = total_duration * attempts_per_second
        
        insert_pos = random.randint(len(common_passwords) // 2, len(common_passwords) + 20)
        common_passwords.insert(insert_pos, self.password_found)
        
        start_time_attack = time.time()
        
        print("\033[93m[+] Testing credential combinations:\033[0m\n")
        
        attempt_count = 0
        success_line = random.randint(int(total_attempts_possible * 0.7), int(total_attempts_possible * 0.95))
        
        while time.time() - start_time_attack < total_duration:
            attempt_count += 1
            
            if attempt_count < len(common_passwords) * 3:
                password_try = common_passwords[attempt_count % len(common_passwords)]
            else:
                chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
                password_try = ''.join(random.choice(chars) for _ in range(random.randint(6, 12)))
            
            delay = random.uniform(0.05, 0.15)
            time.sleep(delay)
            
            ip = self.generate_fake_ip()
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            
            if attempt_count == success_line:
                status = "\033[92m[ACCESS GRANTED]\033[0m"
                print(f"[{timestamp}] [TOR:{ip}] {self.target_email}:{self.password_found} {status}")
                self.total_attempts = attempt_count
                
                print(f"\n\033[92m[+] Valid credentials found at {timestamp}\033[0m")
                print(f"\033[92m[+] Authentication token generated\033[0m")
                print(f"\033[92m[+] Session established with target\033[0m")
                time.sleep(2)
                break
            else:
                status = "\033[91m[ACCESS DENIED]\033[0m"
                if attempt_count % random.randint(3, 7) == 0:
                    print(f"[{timestamp}] [TOR:{ip}] {self.target_email}:{password_try} {status}")
        
        if attempt_count < success_line:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            ip = self.generate_fake_ip()
            status = "\033[92m[ACCESS GRANTED]\033[0m"
            print(f"[{timestamp}] [TOR:{ip}] {self.target_email}:{self.password_found} {status}")
            self.total_attempts = attempt_count
        
        return attempt_count
    
    def show_results(self, attempts):
        print("\n" + "="*60)
        self.typewriter_effect("\033[92m[+] OPERATION COMPLETED SUCCESSFULLY\033[0m", 0.02)
        print("\033[92m" + "="*60 + "\033[0m\n")
        
        end_time = datetime.now().strftime("%H:%M:%S")
        
        print(f"\033[96m[*] Compromised account: {self.target_email}\033[0m")
        print(f"\033[96m[*] Credentials: \033[92m{self.target_email}:{self.password_found}\033[0m")
        print(f"\033[96m[*] Total attempts: {attempts}\033[0m")
        print(f"\033[96m[*] Time elapsed: 60 seconds\033[0m")
        print(f"\033[96m[*] Breach time: {end_time}\033[0m")
        print(f"\033[96m[*] Session ID: {self.session_id}\033[0m")
        
        print("\n\033[93m[*] Extracting account data:\033[0m")
        time.sleep(1)
        
        fake_data = [
            ("Last login", "2 hours ago"),
            ("Location", f"São Paulo, BR ({self.generate_fake_ip()})"),
            ("2FA enabled", "No"),
            ("Recovery email", "backup@email.com"),
            ("Account created", "March 15, 2018"),
            ("Storage used", "2.4/15 GB"),
            ("Connected devices", "3 devices"),
            ("Recent activity", "Email opened 5 minutes ago")
        ]
        
        for item, value in fake_data:
            print(f"    \033[94m[>] {item}: {value}\033[0m")
            time.sleep(0.2)
        
        print("\n\033[93m[*] Available actions:\033[0m")
        print("    \033[94m[1] Export emails\033[0m")
        print("    \033[94m[2] Download attachments\033[0m")
        print("    \033[94m[3] Access Google Drive\033[0m")
        print("    \033[94m[4] Maintain persistence\033[0m")
        print("    \033[94m[5] Clear logs and exit\033[0m")
        
        print("\n\033[95m" + "="*60 + "\033[0m")
        self.typewriter_effect("\033[95m[+] Session maintained. Connection stable.\033[0m", 0.03)
        time.sleep(2)
        
        print("\n\033[96m[?] Select action (1-5, default=5): \033[0m", end="")
        choice = input()
        
        if choice == "1":
            print("\033[92m[+] Starting email export...\033[0m")
            time.sleep(2)
            print("\033[92m[+] 1,247 emails exported to /tmp/gmail_dump_{}.zip\033[0m".format(self.session_id))
        elif choice == "2":
            print("\033[92m[+] Downloading attachments...\033[0m")
            time.sleep(2)
            print("\033[92m[+] 43 files downloaded (total: 156MB)\033[0m")
        elif choice == "3":
            print("\033[92m[+] Accessing Google Drive...\033[0m")
            time.sleep(2)
            print("\033[92m[+] 87 files accessible in Drive\033[0m")
        elif choice == "4":
            print("\033[92m[+] Installing persistence module...\033[0m")
            time.sleep(2)
            print("\033[92m[+] Backdoor active. Session will remain open.\033[0m")
        
        print("\n\033[91m[!] Cleaning trace logs...\033[0m")
        time.sleep(1)
        print("\033[92m[+] Proxy logs erased\033[0m")
        print("\033[92m[+] Connection history cleared\033[0m")
        print("\033[92m[+] Session {} terminated\033[0m".format(self.session_id))
    
    def run(self):
        self.clear_screen()
        self.print_banner()
        
        try:
            self.get_target()
            time.sleep(1)
            
            attempts = self.simulate_brute_force()
            
            self.show_results(attempts)
            
        except KeyboardInterrupt:
            print("\n\n\033[91m[!] Emergency shutdown initiated\033[0m")
            time.sleep(1)
            print("\033[92m[+] All connections terminated\033[0m")
            print("\033[92m[+] Evidence purged\033[0m")
            sys.exit(0)

def main():
    tool = GmailAccessTool()
    
    print("\n\033[96m[?] Initialize access protocol? (y/n): \033[0m", end="")
    choice = input().lower()
    
    if choice == 'y' or choice == '':
        tool.run()
    else:
        print("\n\033[93m[*] System offline\033[0m")

if __name__ == "__main__":
    if os.name == 'nt':
        os.system("title GMail Access Terminal")
        os.system("mode con: cols=80 lines=40")
    
    main()
