#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import sys
import os
import threading
from datetime import datetime

class NeuralInfiltration:
    def __init__(self):
        self.target_email = ""
        self.neural_pass = "senha123@"
        self.penetration_count = 0
        self.mission_code = f"NEURAL-{random.randint(10000, 99999)}"
        self.connection_matrix = []
        
    def neural_wipe(self):
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def neural_banner(self):
        banner = r"""
    ____                 _ _ _   _            _    
   / ___|_ __ ___   __ _(_) | | | | __ _  ___| | __
  | |  _| '_ ` _ \ / _` | | | |_| |/ _` |/ __| |/ /
  | |_| | | | | | | (_| | | |  _  | (_| | (__|   < 
   \____|_| |_| |_|\__,_|_|_|_| |_|\__,_|\___|_|\_\
                                                  
        """
        print("\033[38;5;51m" + banner + "\033[0m")
        print("\033[38;5;214m" + "≣" * 65 + "\033[0m")
        print(f"\033[38;5;214m[▲] Neural Matrix v4.2 | Mission: {self.mission_code}\033[0m")
        print(f"\033[38;5;214m[▲] Quantum Encryption: ONLINE | Neural Link: SYNCHRONIZED\033[0m")
        print("\033[38;5;214m" + "≣" * 65 + "\033[0m\n")
    
    def matrix_print(self, text, delay=0.03, color="\033[38;5;85m"):
        print(color, end="")
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char not in [' ', '\n']:
                time.sleep(delay)
        print("\033[0m")
    
    def quantum_loader(self, duration=3, label="Quantum Scanning"):
        phases = ["◐", "◓", "◑", "◒"]
        dots = ["   ", ".  ", ".. ", "..."]
        start = time.time()
        
        sys.stdout.write(f"\033[38;5;45m[▲] {label}")
        sys.stdout.flush()
        
        phase_idx = 0
        dot_idx = 0
        
        while time.time() - start < duration:
            sys.stdout.write(f"\r\033[38;5;45m[▲] {label}{dots[dot_idx]} {phases[phase_idx]}")
            sys.stdout.flush()
            
            phase_idx = (phase_idx + 1) % len(phases)
            if phase_idx == 0:
                dot_idx = (dot_idx + 1) % len(dots)
            
            time.sleep(0.2)
        
        print(f"\r\033[38;5;45m[▲] {label} \033[38;5;46m[QUANTUM LOCK ACQUIRED]\033[0m")
    
    def neural_rain(self):
        """Efeito de chuva de Matrix ao fundo (thread separada)"""
        def rain_thread():
            chars = ["0", "1", "█", "░", "▒", "▓"]
            width = 80
            columns = [0] * width
            
            for _ in range(50):
                for i in range(width):
                    if random.random() < 0.05 or columns[i] > 0:
                        if columns[i] > 0:
                            print(f"\033[38;5;22m{random.choice(chars)}\033[0m", end="")
                            columns[i] -= 1
                        else:
                            print(f"\033[38;5;46m{random.choice(chars)}\033[0m", end="")
                            columns[i] = random.randint(5, 15)
                    else:
                        print(" ", end="")
                print("\r", end="")
                sys.stdout.flush()
                time.sleep(0.1)
        
        thread = threading.Thread(target=rain_thread, daemon=True)
        thread.start()
        return thread
    
    def target_acquisition(self):
        print("\n" + "≣" * 65)
        self.matrix_print("[?] Neural Input Required: Target Gmail Neural Signature", 0.02, "\033[38;5;213m")
        
        while True:
            print("\033[38;5;213m[→] Neural Input: \033[0m", end="")
            signature = input().strip()
            
            if '@gmail.com' in signature.lower():
                self.target_email = signature
                break
            else:
                self.matrix_print("[!] Invalid Neural Pattern. Gmail Cortex Required.", 0.01, "\033[38;5;196m")
        
        print()
        self.quantum_loader(2, f"Decrypting {signature} Neural Map")
        
        self.matrix_print(f"[+] Target Cortex Mapped: {signature}", 0.015, "\033[38;5;46m")
        self.matrix_print("[+] Google Quantum Firewall Detected", 0.015, "\033[38;5;46m")
        self.matrix_print("[+] Neural Exploit Vectors Calculated", 0.015, "\033[38;5;46m")
        
        return signature
    
    def generate_neural_ip(self):
        return f"{random.randint(10, 99)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    def synapse_overload(self):
        """Novo tipo de carregamento com progressão neural"""
        print("\n" + "≣" * 65)
        self.matrix_print("[+] INITIATING SYNAPSE OVERLOAD PROTOCOL", 0.015, "\033[38;5;196m")
        print("\033[38;5;196m" + "≣" * 65 + "\033[0m\n")
        
        # Efeito de chuva de matrix
        rain = self.neural_rain()
        time.sleep(1)
        
        neural_node = self.generate_neural_ip()
        overload_start = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        self.matrix_print(f"[▲] Overload Initiated: {overload_start}", 0.01, "\033[38;5;51m")
        self.matrix_print(f"[▲] Neural Network: {neural_node} → Quantum Relay → {self.generate_neural_ip()}", 0.01, "\033[38;5;51m")
        self.matrix_print("[▲] Bypassing Google Neural Security Grid", 0.01, "\033[38;5;51m")
        self.matrix_print("[▲] Attack Algorithm: Quantum Entanglement Brute Force", 0.01, "\033[38;5;51m")
        self.matrix_print("[▲] Penetration Rate: 4-8 synaptic bursts/second", 0.01, "\033[38;5;51m")
        
        time.sleep(2)
        print("\n\033[38;5;214m[+] Executing Neural Pattern Injection:\033[0m\n")
        
        # Lista de patterns neurais (senhas)
        neural_patterns = [
            "quantum123", "neural2024", "matrix_001", "cybersynapse",
            "hive_mind01", "ai_overlord", "digital_ghost", "phantom_net",
            "zero_cool", "cerebral_key", "neuro_lock", "synaptic_pass",
            "brain_wave99", "thought_key", "mind_meld", "psi_password",
            "cortex_alpha", "neuron_beta", "dendrite_gamma", "axon_delta",
            "digital_dream", "virtual_soul", "cyber_self", "hacker_id"
        ]
        
        operation_duration = 60
        synaptic_rate = random.randint(4, 8)
        max_synapses = operation_duration * synaptic_rate
        
        injection_point = random.randint(len(neural_patterns) // 2, len(neural_patterns) + 20)
        neural_patterns.insert(injection_point, self.neural_pass)
        
        overload_begin = time.time()
        
        # Barra de progresso neural
        def show_neural_progress(current, total):
            progress = int((current / total) * 40)
            bar = "█" * progress + "░" * (40 - progress)
            percent = (current / total) * 100
            
            colors = [
                "\033[38;5;196m", "\033[38;5;202m", "\033[38;5;208m", 
                "\033[38;5;214m", "\033[38;5;220m", "\033[38;5;226m",
                "\033[38;5;190m", "\033[38;5;154m", "\033[38;5;118m", "\033[38;5;46m"
            ]
            color = colors[min(int(percent / 10), 9)]
            
            sys.stdout.write(f"\r\033[38;5;45m[▲] Neural Penetration: [{bar}] {percent:.1f}% {color}[{current}/{total} synapses]\033[0m")
            sys.stdout.flush()
        
        synapse_count = 0
        breakthrough_moment = random.randint(int(max_synapses * 0.65), int(max_synapses * 0.85))
        
        print("\033[38;5;45m[▲] Establishing Neural Connection to Target Cortex...\033[0m")
        
        while time.time() - overload_begin < operation_duration:
            synapse_count += 1
            
            if synapse_count < len(neural_patterns) * 3:
                current_pattern = neural_patterns[synapse_count % len(neural_patterns)]
            else:
                symbols = "αβγδεζηθικλμνξοπρςστυφχψω"
                current_pattern = ''.join(random.choice(symbols + "0123456789@#$%&*") for _ in range(random.randint(9, 16)))
            
            delay = random.uniform(0.03, 0.09)
            time.sleep(delay)
            
            neural_node = self.generate_neural_ip()
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            
            # Atualizar progresso a cada 5 tentativas
            if synapse_count % 5 == 0:
                show_neural_progress(synapse_count, breakthrough_moment)
            
            if synapse_count == breakthrough_moment:
                print("\n")
                status = "\033[38;5;46m[NEURAL BREAKTHROUGH]\033[0m"
                print(f"[{current_time}] [NEURAL:{neural_node}] {self.target_email}:{self.neural_pass} {status}")
                self.penetration_count = synapse_count
                
                print(f"\n\033[38;5;46m[+] Neural Bridge Established at {current_time}\033[0m")
                print(f"\033[38;5;46m[+] Cortex Firewall Breached\033[0m")
                print(f"\033[38;5;46m[+] Downloading Neural Imprint...\033[0m")
                
                # Efeito de download neural
                for i in range(3):
                    time.sleep(0.3)
                    print(f"\033[38;5;45m[▲] Downloading Memory Cluster {i+1}/3\033[0m")
                
                time.sleep(1.5)
                break
        
        if synapse_count < breakthrough_moment:
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            neural_node = self.generate_neural_ip()
            status = "\033[38;5;46m[NEURAL BREAKTHROUGH]\033[0m"
            print(f"\n[{current_time}] [NEURAL:{neural_node}] {self.target_email}:{self.neural_pass} {status}")
            self.penetration_count = synapse_count
        
        show_neural_progress(synapse_count, synapse_count)
        print("\n")
        
        return synapse_count
    
    def cortex_harvest(self, synapses):
        print("\n" + "≣" * 65)
        self.matrix_print("[+] CORTEX HARVEST: NEURAL DOMINANCE ACHIEVED", 0.015, "\033[38;5;46m")
        print("\033[38;5;46m" + "≣" * 65 + "\033[0m\n")
        
        harvest_time = datetime.now().strftime("%H:%M:%S")
        
        print(f"\033[38;5;51m[▲] Compromised Cortex: {self.target_email}\033[0m")
        print(f"\033[38;5;51m[▲] Neural Key Extracted: \033[38;5;46m{self.target_email}:{self.neural_pass}\033[0m")
        print(f"\033[38;5;51m[▲] Synaptic Attempts: {synapses}\033[0m")
        print(f"\033[38;5;51m[▲] Harvest Duration: 60 neural cycles\033[0m")
        print(f"\033[38;5;51m[▲] Breach Timecode: {harvest_time}\033[0m")
        print(f"\033[38;5;51m[▲] Mission Code: {self.mission_code}\033[0m")
        
        print("\n\033[38;5;214m[+] Extracting Neural Imprint Data:\033[0m")
        time.sleep(0.5)
        
        # Animação de extração de dados
        cortex_data = [
            ("Last Neural Activity", "2.7 cycles ago"),
            ("Geolocation Matrix", f"Quantum Grid #{random.randint(1000, 9999)}"),
            ("Biometric Lock", "Neural Bypass Active"),
            ("Memory Allocation", f"{random.uniform(2.1, 4.7):.1f}/15 TB"),
            ("Connected Synapses", f"{random.randint(2, 5)} neural interfaces"),
            ("Recent Thoughts", f"{random.randint(1, 99)} unencrypted memories"),
            ("Security Rating", f"{random.randint(30, 60)}% - Vulnerable"),
            ("Social Graph", f"{random.randint(100, 500)} neural connections")
        ]
        
        for item, value in cortex_data:
            time.sleep(0.2)
            print(f"    \033[38;5;45m[›] {item}: \033[38;5;85m{value}\033[0m")
        
        print("\n\033[38;5;214m[+] Post-Harvest Neural Commands:\033[0m")
        commands = [
            ("[1]", "Clone Memory Banks"),
            ("[2]", "Extract Social Graph"),
            ("[3]", "Access Quantum Services"),
            ("[4]", "Plant Neural Backdoor"),
            ("[5]", "Execute Ghost Protocol")
        ]
        
        for cmd, desc in commands:
            print(f"    \033[38;5;45m{cmd} {desc}\033[0m")
        
        print("\n\033[38;5;196m" + "≣" * 65 + "\033[0m")
        self.matrix_print("[+] Neural Connection: STABLE | Quantum Sync: 99.7%", 0.02, "\033[38;5;196m")
        time.sleep(1)
        
        print("\n\033[38;5;213m[?] Execute Neural Command (1-5, default=5): \033[0m", end="")
        command = input().strip()
        
        # Animações específicas para cada comando
        if command == "1":
            print("\033[38;5;46m[+] Cloning Memory Banks...\033[0m")
            for i in range(1, 4):
                time.sleep(0.7)
                print(f"\033[38;5;45m[▲] Memory Cluster {i}: {random.randint(100, 500)}GB cloned\033[0m")
        elif command == "2":
            print("\033[38;5;46m[+] Extracting Social Graph...\033[0m")
            time.sleep(1)
            print("\033[38;5;45m[▲] Neural Network: {:,} connections mapped\033[0m".format(random.randint(300, 800)))
        elif command == "3":
            print("\033[38;5;46m[+] Accessing Quantum Services...\033[0m")
            services = ["Drive", "Photos", "Assistant", "Cloud", "AI Core"]
            for service in random.sample(services, 3):
                time.sleep(0.5)
                print(f"\033[38;5;45m[▲] {service}: Quantum Access Granted\033[0m")
        elif command == "4":
            print("\033[38;5;46m[+] Planting Neural Backdoor...\033[0m")
            time.sleep(1.5)
            print("\033[38;5;45m[▲] Backdoor Active: Persistent Neural Link Established\033[0m")
        
        print("\n\033[38;5;196m[!] Initiating Neural Scrub Protocol...\033[0m")
        
        # Animação de limpeza neural
        scrub_steps = [
            "Purging Quantum Logs",
            "Erasing Neural Footprint",
            "Scrambling IP Traces",
            "Wiping Memory Cache",
            "Terminating Neural Link"
        ]
        
        for step in scrub_steps:
            time.sleep(0.6)
            print(f"\033[38;5;45m[▲] {step}...\033[0m")
        
        print(f"\033[38;5;46m[+] Mission {self.mission_code}: Neural Scrub Complete\033[0m")
    
    def execute_neural_protocol(self):
        self.neural_wipe()
        self.neural_banner()
        
        try:
            self.target_acquisition()
            time.sleep(1)
            
            synapses = self.synapse_overload()
            
            self.cortex_harvest(synapses)
            
        except KeyboardInterrupt:
            print("\n\n\033[38;5;196m[!] Neural Emergency Protocol Activated\033[0m")
            time.sleep(0.8)
            print("\033[38;5;45m[▲] All Neural Links Severed\033[0m")
            print("\033[38;5;45m[▲] Quantum Traces Eliminated\033[0m")
            sys.exit(0)

def main():
    neural = NeuralInfiltration()
    
    print("\n\033[38;5;213m[?] Initialize Neural Infiltration Protocol? (Y/n): \033[0m", end="")
    init = input().strip().lower()
    
    if init in ['y', 'yes', '']:
        neural.execute_neural_protocol()
    else:
        print("\n\033[38;5;214m[▲] Neural Protocol: STAND BY\033[0m")

if __name__ == "__main__":
    if os.name == 'nt':
        os.system("title Neural Infiltration Matrix")
        os.system("mode con: cols=85 lines=50")
    
    main()
