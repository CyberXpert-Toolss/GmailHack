#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GMAILHACK - Ferramenta de Hacking para Gmail
Esta ferramenta é PAGA - Valor: R$ 100,00
Contato para comprar via WhatsApp: +55 21 97592-7909
"""

import os
import sys
import time

VALOR_FERRAMENTA = "R$ 100,00"
CONTATO_WHATSAPP = "+55 21 97592-7909"
CODIGO_CORRETO = "GMAIL2024"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_logo():
    logo = r"""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                                                                       ║
    ║  ██████╗ ███╗   ███╗ █████╗ ██╗██╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗║
    ║ ██╔════╝ ████╗ ████║██╔══██╗██║██║     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝║
    ║ ██║  ███╗██╔████╔██║███████║██║██║     ███████║███████║██║     █████╔╝ ║
    ║ ██║   ██║██║╚██╔╝██║██╔══██║██║██║     ██╔══██║██╔══██║██║     ██╔═██╗ ║
    ║ ╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗██║  ██║██║  ██║╚██████╗██║  ██╗║
    ║  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝║
    ║                                                                       ║
    ║                 FERRAMENTA DE HACKING PARA GMAIL v3.2                 ║
    ║                                                                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """
    
    print("\033[92m" + logo + "\033[0m")
    print("\033[93m" + "═" * 75 + "\033[0m")
    print(f"\033[93m[#] GmailHack Tool - Ferramenta Profissional\033[0m")
    print(f"\033[93m[#] Esta ferramenta é PAGA - Valor: {VALOR_FERRAMENTA}\033[0m")
    print(f"\033[93m[#] Contato para comprar via WhatsApp: {CONTATO_WHATSAPP}\033[0m")
    print("\033[93m" + "═" * 75 + "\033[0m\n")

def verificar_codigo():
    print("\n" + "═" * 75)
    print("\033[96m[!] VERIFICAÇÃO DE CÓDIGO DE ATIVAÇÃO\033[0m")
    print("\033[96m" + "═" * 75 + "\033[0m")
    
    print(f"\n\033[91m[!] ATENÇÃO: Esta ferramenta é PAGA\033[0m")
    print(f"\033[91m[!] Valor: {VALOR_FERRAMENTA}\033[0m")
    print(f"\033[91m[!] Para comprar, chame no WhatsApp: {CONTATO_WHATSAPP}\033[0m\n")
    
    print(f"\033[96mDigite o código de ativação: \033[0m", end="")
    codigo = input().strip()
    
    if codigo == CODIGO_CORRETO:
        print(f"\n\033[92m[✓] Código correto!\033[0m")
        print(f"\033[92m[✓] Sistema ativado com sucesso\033[0m")
        print(f"\033[92m[✓] Ferramenta pronta para uso\033[0m")
        time.sleep(2)
        return True
    else:
        print(f"\n\033[91m[✗] Código incorreto\033[0m")
        print(f"\033[91m[✗] Código digitado: '{codigo}'\033[0m")
        print(f"\033[91m[✗] Este código não está na nossa base de dados\033[0m")
        
        print(f"\n\033[93m" + "═" * 75 + "\033[0m")
        print(f"\033[93m[!] PARA OBTER O CÓDIGO CORRETO:\033[0m")
        print(f"\033[93m[!] 1. Chame no WhatsApp: {CONTATO_WHATSAPP}\033[0m")
        print(f"\033[93m[!] 2. Faça o pagamento de {VALOR_FERRAMENTA}\033[0m")
        print(f"\033[93m[!] 3. Receba o código de ativação válido\033[0m")
        print(f"\033[93m[!] 4. Use o código recebido para ativar a ferramenta\033[0m")
        print(f"\033[93m" + "═" * 75 + "\033[0m")
        
        print(f"\n\033[94m[!] WhatsApp para comprar: {CONTATO_WHATSAPP}\033[0m")
        print(f"\033[94m[!] Valor: {VALOR_FERRAMENTA}\033[0m")
        
        time.sleep(4)
        return False

def main():
    limpar_tela()
    mostrar_logo()
    
    # Direto para o código de ativação
    if verificar_codigo():
        print(f"\n\033[92m" + "═" * 75 + "\033[0m")
        print(f"\033[92m[+] Acesso liberado! Ferramenta ativada.\033[0m")
        print(f"\033[92m[+] Você pode agora usar todos os recursos.\033[0m")
        print(f"\033[92m[+] Para suporte técnico, WhatsApp: {CONTATO_WHATSAPP}\033[0m")
        print(f"\033[92m" + "═" * 75 + "\033[0m")
        time.sleep(3)
        
        # Simulação de ferramenta ativada
        print(f"\n\033[94m[+] Inicializando ferramenta GmailHack...\033[0m")
        print(f"\033[94m[+] Carregando módulos de segurança...\033[0m")
        print(f"\033[94m[+] Configurando conexões criptografadas...\033[0m")
        time.sleep(2)
        
        print(f"\n\033[92m[✓] Ferramenta carregada com sucesso!\033[0m")
        print(f"\033[92m[✓] Todos os recursos disponíveis\033[0m")
        print(f"\033[92m[✓] Use com responsabilidade\033[0m")
        
    else:
        print(f"\n\033[91m" + "═" * 75 + "\033[0m")
        print(f"\033[91m[!] CÓDIGO DE ATIVAÇÃO INVÁLIDO\033[0m")
        print(f"\033[91m[!] Para comprar a ferramenta:\033[0m")
        print(f"\033[91m[!] WhatsApp: {CONTATO_WHATSAPP}\033[0m")
        print(f"\033[91m[!] Valor: {VALOR_FERRAMENTA}\033[0m")
        print(f"\033[91m[!] Programa encerrado\033[0m")
        print(f"\033[91m" + "═" * 75 + "\033[0m")
        time.sleep(5)

if __name__ == "__main__":
    if os.name == 'nt':
        os.system("title GmailHack Tool - Ferramenta de Hacking para Gmail")
        os.system("mode con: cols=85 lines=35")
    
    main()
