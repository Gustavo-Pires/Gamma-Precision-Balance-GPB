import sys
from cx_Freeze import setup, Executable

# Configurações do seu código
build_exe_options = {
    "packages": [],
    "excludes": [],
    "includes": [],
    "include_files": []
}

# Configuração do executável
executables = [
    Executable(
        "grafico_paulo.py",
        base=None,
        targetName="Graficos Calibracao.exe"
    )
]

# Configuração geral
setup(
    name="GRAFICOS CONTROLE CALIBRACAO",
    version="1.0",
    description="Gerar graficos da calibracao",
    options={
        "build_exe": build_exe_options
    },
    executables=executables
)
