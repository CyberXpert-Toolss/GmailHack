#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import sys
import os
from datetime import datetime

class ShadowBreach:
    def __init__(self):
        self.target_email = ""
        self.cracked_pass = "senha123@"
        self.attempt_count = 0
        self.operation_id = random.randint(1000, 9999)
        
    def wipe_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def display_header(self):
        header = r"""
    ____                 _ _ _   _            _    
   / ___|_ __ ___   __ _(_) | | | | __ _  ___| | __
  | |  _| '_ ` _ \ / _` | | | |_| |/ _` |/ __| |/ /
  | |_| | | | | | | (_| | | |  _  | (_| | (__|   < 
   \____|_| |_| |_|\__,_|_|_|_| |_|\__,_|\___|_|\_\
                                                  
        """
        print("\033[32m" + header + "\033[0m")
        print("\033[33m" + "-" * 60 + "\033[0m")
        print("\033[33m[•] Operation PHANTOM v2.7 | Session: #{}\033[0m".format(self.operation_id))
        print("\033[33m[•] Encrypted Tunnel: ACTIVE | Stealth Mode: ENGAGED\033[0m")
        print("\033[33m" + "-" * 60 + "\033[0m\n")
    
    def ghost_type(self, text, speed=0.025):
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(speed)
        print()
    
    def ghost_loader(self, seconds=2, message="Ghosting"):
        symbols = ["▁", "▃", "▄", "▅", "▆", "▇", "█", "▇", "▆", "▅", "▄", "▃"]
        end = time.time() + seconds
        
        print(f"\033[36m[•] {message}", end="", flush=True)
        
        while time.time() < end:
            for sym in symbols:
                if time.time() > end:
                    break
                sys.stdout.write(f"\r\033[36m[•] {message} {sym}")
                sys.stdout.flush()
                time.sleep(0.08)
        print(f"\r\033[36m[•] {message} \033[32m[READY]\033[0m")
    
    def acquire_target(self):
        print("\n" + "-" * 60)
        self.ghost_type("\033[35m[?] Insert target Gmail identity:\033[0m", 0.015)
        
        while True:
            identity = input("\033[35m[→] \033[0m").strip()
            if '@gmail.com' in identity.lower():
                self.target_email = identity
                break
            else:
                self.ghost_type("\033[31m[!] Invalid Gmail signature. Required format: user@gmail.com\033[0m", 0.01)
        
        print()
        self.ghost_loader(1, f"Ghost scanning {identity}")
        
        self.ghost_type(f"\033[32m[+] Target locked: {identity}\033[0m", 0.015)
        self.ghost_type("\033[32m[+] Google authentication vector identified\033[0m", 0.015)
        self.ghost_type("\033[32m[+] Security layers mapped for penetration\033[0m", 0.015)
        
        return identity
    
    def phantom_ip(self):
        return f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    def breach_protocol(self):
        print("\n" + "-" * 60)
        self.ghost_type("\033[31m[+] INITIATING CREDENTIAL HARVEST PROTOCOL\033[0m", 0.015)
        print("\033[31m" + "-" * 60 + "\033[0m\n")
        
        ghost_ip = self.phantom_ip()
        breach_start = datetime.now().strftime("%H:%M:%S")
        
        self.ghost_type(f"\033[36m[•] Breach timestamp: {breach_start}\033[0m", 0.01)
        self.ghost_type(f"\033[36m[•] Ghost network: {ghost_ip} → VPN → {self.phantom_ip()}\033[0m", 0.01)
        self.ghost_type("\033[36m[•] Evading Google security protocols...\033[0m", 0.01)
        self.ghost_type("\033[36m[•] Attack pattern: Rainbow + Dictionary hybrid\033[0m", 0.01)
        self.ghost_type("\033[36m[•] Injection rate: 3-7 attempts/second\033[0m", 0.01)
        
        time.sleep(1)
        print()
        
        pass_combinations = [
            "admin123", "qwerty123", "welcome1", "masterkey",
            "shadow123", "phantom1", "ghost123", "hunter2",
            "dragon123", "python3", "kali2023", "ubuntu1",
            "windows10", "macbook1", "android1", "iphone13",
            "matrix123", "cyberpunk", "hackerman", "rootaccess",
            "letmein123", "changeme1", "default1", "password1",
            "12345678", "11111111", "00000000", "abcdefg"
        ]
        
        operation_time = 60
        injection_rate = random.randint(3, 7)
        max_injections = operation_time * injection_rate
        
        injection_point = random.randint(len(pass_combinations) // 2, len(pass_combinations) + 15)
        pass_combinations.insert(injection_point, self.cracked_pass)
        
        breach_begin = time.time()
        
        print("\033[33m[+] Injecting credential combinations:\033[0m\n")
        
        injection_count = 0
        success_moment = random.randint(int(max_injections * 0.6), int(max_injections * 0.9))
        
        while time.time() - breach_begin < operation_time:
            injection_count += 1
            
            if injection_count < len(pass_combinations) * 3:
                current_try = pass_combinations[injection_count % len(pass_combinations)]
            else:
                characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
                current_try = ''.join(random.choice(characters) for _ in range(random.randint(8, 14)))
            
            delay = random.uniform(0.04, 0.12)
            time.sleep(delay)
            
            ghost_node = self.phantom_ip()
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-4]
            
            if injection_count == success_moment:
                status = "\033[32m[CREDENTIALS VALID]\033[0m"
                print(f"[{current_time}] [GHOST:{ghost_node}] {self.target_email}:{self.cracked_pass} {status}")
                self.attempt_count = injection_count
                
                print(f"\n\033[32m[+] Authentication breach successful at {current_time}\033[0m")
                print(f"\033[32m[+] Security token compromised\033[0m")
                print(f"\033[32m[+] Establishing persistent connection...\033[0m")
                time.sleep(1.5)
                break
            else:
                status = "\033[31m[INVALID CREDENTIALS]\033[0m"
                if injection_count % random.randint(2, 5) == 0:
                    print(f"[{current_time}] [GHOST:{ghost_node}] {self.target_email}:{current_try} {status}")
        
        if injection_count < success_moment:
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-4]
            ghost_node = self.phantom_ip()
            status = "\033[32m[CREDENTIALS VALID]\033[0m"
            print(f"[{current_time}] [GHOST:{ghost_node}] {self.target_email}:{self.cracked_pass} {status}")
            self.attempt_count = injection_count
        
        return injection_count
    
    def show_harvest(self, injections):
        print("\n" + "-" * 60)
        self.ghost_type("\033[32m[+] OPERATION PHANTOM: COMPROMISE SUCCESSFUL\033[0m", 0.015)
        print("\033[32m" + "-" * 60 + "\033[0m\n")
        
        breach_end = datetime.now().strftime("%H:%M:%S")
        
        print(f"\033[36m[•] Compromised identity: {self.target_email}\033[0m")
        print(f"\033[36m[•] Harvested credentials: \033[32m{self.target_email}:{self.cracked_pass}\033[0m")
        print(f"\033[36m[•] Total injections: {injections}\033[0m")
        print(f"\033[36m[•] Breach duration: 60 seconds\033[0m")
        print(f"\033[36m[•] Compromise time: {breach_end}\033[0m")
        print(f"\033[36m[•] Operation ID: PHANTOM-{self.operation_id}\033[0m")
        
        print("\n\033[33m[+] Extracting digital footprint:\033[0m")
        time.sleep(0.8)
        
        digital_data = [
            ("Last authentication", "Today 14:32"),
            ("Geolocation", f"Brazil, SP ({self.phantom_ip()})"),
            ("Two-factor status", "Disabled"),
            ("Account age", "3 years, 7 months"),
            ("Storage allocation", "3.2/15 GB"),
            ("Linked devices", "Smartphone, Tablet, Laptop"),
            ("Recent activity", "Email received 8 minutes ago"),
            ("Security score", "48/100 (Vulnerable)")
        ]
        
        for item, value in digital_data:
            print(f"    \033[34m[›] {item}: {value}\033[0m")
            time.sleep(0.15)
        
        print("\n\033[33m[+] Post-breach options:\033[0m")
        print("    \033[34m[1] Clone mailbox data\033[0m")
        print("    \033[34m[2] Extract contact network\033[0m")
        print("    \033[34m[3] Access Google services\033[0m")
        print("    \033[34m[4] Plant ghost persistence\033[0m")
        print("    \033[34m[5] Erase traces and vanish\033[0m")
        
        print("\n\033[31m" + "-" * 60 + "\033[0m")
        self.ghost_type("\033[31m[+] Ghost connection: STABLE | Encryption: ACTIVE\033[0m", 0.02)
        time.sleep(1.5)
        
        print("\n\033[35m[?] Select post-operation vector (1-5, default=5): \033[0m", end="")
        vector = input().strip()
        
        if vector == "1":
            print("\033[32m[+] Cloning mailbox contents...\033[0m")
            time.sleep(1.8)
            print("\033[32m[+] 2,148 messages cloned to ghost storage\033[0m")
        elif vector == "2":
            print("\033[32m[+] Extracting contact network...\033[0m")
            time.sleep(1.8)
            print("\033[32m[+] 312 contacts mapped and archived\033[0m")
        elif vector == "3":
            print("\033[32m[+] Accessing Google ecosystem...\033[0m")
            time.sleep(1.8)
            print("\033[32m[+] Drive, Photos, and Calendar accessible\033[0m")
        elif vector == "4":
            print("\033[32m[+] Planting ghost persistence module...\033[0m")
            time.sleep(2)
            print("\033[32m[+] Backdoor active. Silent access maintained.\033[0m")
        
        print("\n\033[31m[!] Initiating ghost protocol cleanup...\033[0m")
        time.sleep(1)
        print("\033[32m[+] Operation logs purged\033[0m")
        print("\033[32m[+] Network traces erased\033[0m")
        print("\033[32m[+] Session PHANTOM-{} terminated\033[0m".format(self.operation_id))
    
    def execute(self):
        self.wipe_screen()
        self.display_header()
        
        try:
            self.acquire_target()
            time.sleep(0.8)
            
            injections = self.breach_protocol()
            
            self.show_harvest(injections)
            
        except KeyboardInterrupt:
            print("\n\n\033[31m[!] Emergency ghost protocol activated\033[0m")
            time.sleep(0.8)
            print("\033[32m[+] All connections severed\033[0m")
            print("\033[32m[+] Digital footprint eliminated\033[0m")
            sys.exit(0)

def main():
    phantom = ShadowBreach()
    
    print("\n\033[35m[?] Engage phantom protocol? (y/N): \033[0m", end="")
    engage = input().lower()
    
    if engage == 'y':
        phantom.execute()
    else:
        print("\n\033[33m[•] Phantom protocol deactivated\033[0m")

if __name__ == "__main__":
    if os.name == 'nt':
        os.system("title Phantom Breach Protocol")
        os.system("mode con: cols=80 lines=45")
    
    main()
