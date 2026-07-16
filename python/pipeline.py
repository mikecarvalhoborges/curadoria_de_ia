# importar biblioteca para executar scripts externos
import subprocess

# Executa o script coletar_respostas.py
subprocess.run(["py", "python/coletar_respostas.py"])

# Executa o script exportar_sheets.py
subprocess.run(["py", "python/exportar_sheets.py"])