#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import sys
import os
import socket
import hashlib
from datetime import datetime

class GMailPenetrationSuite:
    def __init__(self):
        self.target_email = ""
        self.comp_pass = "senha123@"
        self.attempts = 0
        self.session_id = f"GS-{random.randint(100000, 999999)}"
        self.vpn_exit_nodes = []
        
    def clear_terminal(self):
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def show_header(self):
        header = r"""
    ____                 _ _ _   _            _    
   / ___|_ __ ___   __ _(_) | | | | __ _  ___| | __
  | |  _| '_ ` _ \ / _` | | | |_| |/ _` |/ __| |/ /
  | |_| | | | | | | (_| | | |  _  | (_| | (__|   < 
   \____|_| |_| |_|\__,_|_|_|_| |_|\__,_|\___|_|\_\
                                                  
        """
        print("\033[92m" + header + "\033[0m")
        print("\033[93m" + "#" * 70 + "\033[0m")
        print(f"\033[93m[+] GMail Penetration Suite v5.3.1 | Session: {self.session_id}\033[0m")
        print("\033[93m[+] VPN Chain: Netherlands → Germany → Sweden → USA\033[0m")
        print("\033[93m[+] Tor Relay: Active | Proxy Rotation: Enabled\033[0m")
        print("\033[93m" + "#" * 70 + "\033[0m\n")
    
    def slow_print(self, text, speed=0.02):
        """Impressão com velocidade realista"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()
    
    def loading_sequence(self, duration=2, message="Establishing connection"):
        """Sequência de carregamento profissional"""
        steps = [
            "Initializing secure tunnel...",
            "Connecting to VPN node...",
            "Handshaking with proxy server...",
            "Verifying SSL certificates...",
            "Establishing encrypted connection..."
        ]
        
        start_time = time.time()
        step_index = 0
        
        while time.time() - start_time < duration:
            if step_index < len(steps):
                sys.stdout.write(f"\r\033[94m[+] {steps[step_index]}\033[0m")
                sys.stdout.flush()
                step_index += 1
            
            time.sleep(0.4)
            sys.stdout.write("\r" + " " * 80 + "\r")
            
        print(f"\r\033[92m[✓] {message} completed\033[0m")
    
    def generate_ip(self):
        """Gerar IPs realistas para diferentes países"""
        countries = {
            'NL': ['145.', '178.', '195.'],  # Netherlands
            'DE': ['176.', '188.', '91.'],   # Germany
            'SE': ['185.', '46.', '87.'],    # Sweden
            'US': ['104.', '192.', '23.']    # USA
        }
        
        country = random.choice(list(countries.keys()))
        base = random.choice(countries[country])
        return f"{base}{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    def setup_vpn_chain(self):
        """Configurar cadeia de VPNs realista"""
        print("\033[96m[+] Configuring VPN chain...\033[0m")
        time.sleep(0.5)
        
        self.vpn_exit_nodes = [
            self.generate_ip(),
            self.generate_ip(),
            self.generate_ip()
        ]
        
        for i, ip in enumerate(self.vpn_exit_nodes, 1):
            print(f"\033[94m    ├─ VPN Node {i}: {ip} (UDP 443)\033[0m")
            time.sleep(0.2)
        
        print("\033[92m    └─ VPN chain configured successfully\033[0m\n")
    
    def get_target(self):
        """Coletar informações do alvo"""
        print("\n" + "#" * 70)
        print("\033[96m[?] Enter target GMail address:\033[0m")
        print("\033[90m    Example: user@gmail.com\033[0m")
        
        while True:
            print("\033[96m[>]\033[0m ", end="")
            email = input().strip().lower()
            
            if '@gmail.com' in email:
                if email.count('@') == 1:
                    self.target_email = email
                    break
                else:
                    print("\033[91m[!] Invalid email format\033[0m")
            else:
                print("\033[91m[!] Please enter a valid GMail address\033[0m")
        
        print()
        self.loading_sequence(2, f"Target verification")
        
        # Verificação realista do alvo
        print("\033[96m[+] Checking target availability...\033[0m")
        time.sleep(0.8)
        
        if random.random() > 0.1:  # 90% de chance de sucesso
            print("\033[92m[✓] Target is online and accessible\033[0m")
            
            # Informações fictícias sobre o alvo
            print("\033[96m[+] Gathering target information...\033[0m")
            time.sleep(0.5)
            
            info = [
                f"Last login: {random.randint(1, 24)} hours ago",
                f"Account created: {random.randint(2015, 2022)}",
                f"2FA status: {'Disabled' if random.random() > 0.7 else 'Enabled'}",
                f"Connected devices: {random.randint(1, 5)}"
            ]
            
            for item in info:
                print(f"\033[94m    → {item}\033[0m")
                time.sleep(0.2)
        else:
            print("\033[93m[!] Target may have additional security measures\033[0m")
            print("\033[93m[!] Proceeding with caution...\033[0m")
        
        return email
    
    def password_attack(self):
        """Ataque de senha realista"""
        print("\n" + "#" * 70)
        print("\033[91m[+] INITIATING PASSWORD ATTACK SEQUENCE\033[0m")
        print("\033[91m" + "#" * 70 + "\033[0m\n")
        
        # Configurar ambiente de ataque
        self.setup_vpn_chain()
        
        attack_time = datetime.now().strftime("%H:%M:%S")
        print(f"\033[96m[+] Attack started at: {attack_time}\033[0m")
        print("\033[96m[+] Using attack method: Hybrid dictionary + mask attack\033[0m")
        print("\033[96m[+] Rate limiting: 3-5 attempts per second (safe mode)\033[0m")
        print("\033[96m[+] Bypassing Google's anti-bot protection...\033[0m")
        
        time.sleep(1.5)
        
        # Lista de senhas comuns
        common_passwords = [
            "password", "123456", "12345678", "1234", "qwerty",
            "12345", "dragon", "baseball", "football", "letmein",
            "monkey", "696969", "abc123", "mustang", "michael",
            "shadow", "master", "jennifer", "111111", "superman",
            "harley", "fuckme", "trustno1", "batman", "sunshine",
            "iloveyou", "asshole", "fuckyou", "zaq1zaq1", "test",
            "hunter", "buster", "soccer", "unknown", "pass",
            "tigger", "robert", "access", "love", "flower",
            "jordan", "matrix", "buster", "shadow", "patricia"
        ]
        
        # Inserir a senha correta em posição aleatória
        insert_pos = random.randint(len(common_passwords)//2, len(common_passwords)+20)
        common_passwords.insert(insert_pos, self.comp_pass)
        
        attack_start = time.time()
        attack_duration = 60  # 1 minuto
        
        print("\n\033[93m[+] Starting credential testing...\033[0m\n")
        
        attempt_num = 0
        success_point = random.randint(
            int(attack_duration * 2.5),
            int(attack_duration * 4.5)
        )
        
        # Headers para os logs
        print(f"{'TIME':<12} {'IP ADDRESS':<18} {'EMAIL/PASSWORD':<35} {'STATUS':<20}")
        print("-" * 85)
        
        while time.time() - attack_start < attack_duration:
            attempt_num += 1
            
            # Selecionar senha para tentativa
            if attempt_num < len(common_passwords) * 2:
                current_pass = common_passwords[attempt_num % len(common_passwords)]
            else:
                # Gerar senhas aleatórias
                patterns = [
                    "word" + str(random.randint(1900, 2024)),
                    "name" + str(random.randint(1, 99)),
                    "user" + str(random.randint(1, 999)),
                    "admin" + str(random.randint(1, 99)),
                    "test" + str(random.randint(1, 99))
                ]
                current_pass = random.choice(patterns)
            
            # Simular tempo de resposta
            response_time = random.uniform(0.1, 0.3)
            time.sleep(response_time)
            
            # Gerar log entry
            current_ip = self.vpn_exit_nodes[attempt_num % len(self.vpn_exit_nodes)]
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            # Decidir se esta é a tentativa bem-sucedida
            if attempt_num == success_point:
                status = "\033[92mSUCCESS\033[0m"
                log_entry = f"{timestamp:<12} {current_ip:<18} {self.target_email}:{self.comp_pass:<35} {status:<20}"
                print(log_entry)
                
                print(f"\n\033[92m[✓] CREDENTIALS VERIFIED SUCCESSFULLY!\033[0m")
                print(f"\033[92m[+] Password found: {self.comp_pass}\033[0m")
                print(f"\033[92m[+] Attempts made: {attempt_num}\033[0m")
                
                self.attempts = attempt_num
                break
            else:
                status = "\033[91mFAILED\033[0m"
                # Mostrar apenas algumas tentativas para não poluir
                if attempt_num % random.randint(3, 7) == 0:
                    log_entry = f"{timestamp:<12} {current_ip:<18} {self.target_email}:{current_pass:<35} {status:<20}"
                    print(log_entry)
        
        # Se não encontrou ainda, encontrar agora
        if attempt_num < success_point:
            timestamp = datetime.now().strftime("%H:%M:%S")
            current_ip = random.choice(self.vpn_exit_nodes)
            status = "\033[92mSUCCESS\033[0m"
            
            print(f"{timestamp:<12} {current_ip:<18} {self.target_email}:{self.comp_pass:<35} {status:<20}")
            print(f"\n\033[92m[✓] CREDENTIALS VERIFIED SUCCESSFULLY!\033[0m")
            self.attempts = attempt_num
        
        return attempt_num
    
    def access_account(self, attempts):
        """Acessar a conta comprometida"""
        print("\n" + "#" * 70)
        print("\033[92m[+] ACCOUNT ACCESS ACHIEVED\033[0m")
        print("\033[92m" + "#" * 70 + "\033[0m\n")
        
        end_time = datetime.now().strftime("%H:%M:%S")
        
        print(f"\033[96m[+] Target: {self.target_email}\033[0m")
        print(f"\033[96m[+] Credentials: {self.target_email}:{self.comp_pass}\033[0m")
        print(f"\033[96m[+] Total attempts: {attempts}\033[0m")
        print(f"\033[96m[+] Time elapsed: 60 seconds\033[0m")
        print(f"\033[96m[+] Compromise time: {end_time}\033[0m")
        print(f"\033[96m[+] Session ID: {self.session_id}\033[0m")
        
        print("\n\033[93m[+] Extracting account data...\033[0m")
        time.sleep(1)
        
        # Simular extração de dados
        data_points = [
            ("Email count", f"{random.randint(1000, 10000):,} messages"),
            ("Storage used", f"{random.uniform(1.2, 4.8):.1f} GB of 15 GB"),
            ("Last activity", f"{random.randint(1, 60)} minutes ago"),
            ("Connected services", "YouTube, Drive, Photos, Calendar"),
            ("Security check", f"Last: {random.randint(1, 90)} days ago"),
            ("Recovery email", f"backup{random.randint(1, 99)}@email.com"),
            ("Phone number", f"+55 {random.randint(11, 99)} 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}")
        ]
        
        for item, value in data_points:
            print(f"\033[94m    ► {item}: {value}\033[0m")
            time.sleep(0.3)
        
        print("\n\033[93m[+] Available actions:\033[0m")
        print("\033[94m    1. Read emails (inbox, sent, drafts)")
        print("    2. Download attachments")
        print("    3. Access Google Drive files")
        print("    4. Check calendar events")
        print("    5. Modify account settings")
        print("    6. Exit and clear logs\033[0m")
        
        print("\n\033[96m[?] Select option (1-6): \033[0m", end="")
        choice = input().strip()
        
        # Processar escolha
        if choice == "1":
            print("\033[92m[+] Accessing email inbox...\033[0m")
            time.sleep(1)
            print(f"\033[94m    ► Unread: {random.randint(0, 50)}")
            print(f"    ► Total: {random.randint(100, 1000)}")
            print(f"    ► Last email: {random.randint(1, 60)} minutes ago\033[0m")
        elif choice == "2":
            print("\033[92m[+] Scanning for attachments...\033[0m")
            time.sleep(1)
            print("\033[94m    ► Found: PDF documents (3)")
            print("    ► Found: Image files (12)")
            print("    ► Found: Archive files (2)")
            print("    ► Total size: 47.3 MB\033[0m")
        elif choice == "3":
            print("\033[92m[+] Connecting to Google Drive...\033[0m")
            time.sleep(1)
            print("\033[94m    ► Documents: {random.randint(5, 50)}")
            print(f"    ► Spreadsheets: {random.randint(2, 20)}")
            print(f"    ► Presentations: {random.randint(1, 10)}")
            print(f"    ► Used space: {random.randint(1, 10)}.2 GB\033[0m")
        elif choice == "4":
            print("\033[92m[+] Accessing calendar...\033[0m")
            time.sleep(1)
            print("\033[94m    ► Today's events: {random.randint(0, 5)}")
            print(f"    ► Upcoming meetings: {random.randint(1, 10)}")
            print(f"    ► Last event: {random.randint(1, 24)} hours ago\033[0m")
        elif choice == "5":
            print("\033[93m[!] WARNING: Modifying settings may trigger alerts\033[0m")
            time.sleep(1)
            print("\033[94m    ► Password changed successfully")
            print("    ► Recovery email updated")
            print("    ► 2FA disabled temporarily\033[0m")
        
        print("\n\033[91m[!] Cleaning up...\033[0m")
        cleanup_steps = [
            "Deleting connection logs",
            "Clearing browser cache",
            "Removing temporary files",
            "Wiping command history",
            "Closing all connections"
        ]
        
        for step in cleanup_steps:
            time.sleep(0.5)
            print(f"\033[94m    ► {step}\033[0m")
        
        print(f"\n\033[92m[✓] Operation {self.session_id} completed successfully\033[0m")
        print("\033[92m[✓] All traces removed from system\033[0m")
        print("\033[92m[✓] Returning to main menu...\033[0m")
    
    def run(self):
        """Executar suite completa"""
        self.clear_terminal()
        self.show_header()
        
        try:
            # Fase 1: Coleta de informações
            print("\033[96m[+] Starting reconnaissance phase...\033[0m")
            time.sleep(1)
            
            self.get_target()
            time.sleep(0.5)
            
            # Fase 2: Ataque
            attempts = self.password_attack()
            
            # Fase 3: Acesso
            self.access_account(attempts)
            
        except KeyboardInterrupt:
            print("\n\n\033[91m[!] Emergency termination triggered\033[0m")
            time.sleep(0.5)
            print("\033[94m[+] Destroying all session data...\033[0m")
            time.sleep(1)
            print("\033[92m[✓] All data wiped. System clean.\033[0m")
            sys.exit(0)

def main():
    tool = GMailPenetrationSuite()
    
    print("\n\033[96m[?] Start GMail penetration test? (y/N): \033[0m", end="")
    response = input().strip().lower()
    
    if response in ['y', 'yes']:
        tool.run()
    else:
        print("\n\033[93m[+] Operation cancelled\033[0m")
        print("\033[93m[+] Shutting down penetration suite...\033[0m")

if __name__ == "__main__":
    if os.name == 'nt':
        os.system("title GMail Penetration Suite")
        os.system("mode con: cols=90 lines=50")
    
    main()
