# 1. Criar arquivo
cd ~
nano google_breach.py

# 2. Colar código acima
# 3. Salvar

# 4. Permissões
chmod +x google_breach.py

# 5. Executar
python3 google_breach.py

# 6. Executar em modo stealth
stty -echo && python3 google_breach.py && stty echo
