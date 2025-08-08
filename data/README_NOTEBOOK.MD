# 🚀 Setup Ambiente Python e Jupyter Kernel - Guia Prático

Este README documenta os comandos executados para criar um ambiente Python completo com kernel Jupyter para o projeto de Data Harvesting.

## 📋 Resumo do que foi feito

✅ Ambiente virtual criado (`aula01`)  
✅ Kernel Jupyter configurado (`AULA01_KERNEL`)  
✅ Dependências instaladas via `requirements.txt`  
✅ Pronto para usar notebooks Jupyter  

---

## 🛠️ Comandos Executados

### 1️⃣ **Criar Ambiente Virtual**

```powershell
# Criar ambiente virtual com nome "aula01"
python -m venv aula01
```

**O que faz:** Cria um ambiente Python isolado na pasta `aula01/`

---

### 2️⃣ **Ativar Ambiente Virtual**

```powershell
# Ativar ambiente (Windows PowerShell/CMD)
aula01\Scripts\activate
```

**Resultado:** Prompt muda para `(aula01) PS ...` indicando ambiente ativo

**Equivalentes para outros sistemas:**
```bash
# Linux/Mac
source aula01/bin/activate

# Windows Git Bash
source aula01/Scripts/activate
```

---

### 3️⃣ **Instalar IPython Kernel**

```powershell
# Instalar ipykernel no ambiente ativo
python -m pip install ipykernel
```

**O que instala:**
- ✅ `ipykernel` - Para criar kernels Jupyter
- ✅ `ipython` - Shell interativo Python
- ✅ `jupyter-client` - Cliente Jupyter
- ✅ Todas as dependências necessárias

---

### 4️⃣ **Criar Kernel Jupyter**

```powershell
# Criar kernel personalizado
python -m ipykernel install --user --name=AULA01_KERNEL --display-name="aula01"
```

**Parâmetros:**
- `--user`: Instala para o usuário atual
- `--name=AULA01_KERNEL`: Nome interno do kernel
- `--display-name="aula01"`: Nome que aparece no Jupyter

**Resultado:** Kernel instalado em:
```
C:\Users\[Usuario]\AppData\Roaming\jupyter\kernels\aula01_kernel
```

---

### 5️⃣ **Instalar Dependências do Projeto**

```powershell
# Instalar bibliotecas do requirements.txt
python -m pip install -r data\requirements.txt
```

**Bibliotecas instaladas:**
- 📦 `requests>=2.28.0` - Requisições HTTP
- 📦 `beautifulsoup4>=4.11.0` - Parser HTML/XML
- 📦 `lxml>=4.9.0` - Parser XML rápido
- 📦 `pandas>=1.5.0` - Análise de dados
- 📦 `certifi>=2022.12.7` - Certificados SSL
- 📦 `urllib3>=1.26.0` - Cliente HTTP
- 📦 `chardet>=5.0.0` - Detecção de encoding

---

## 🎯 Como Usar o Ambiente Criado

### **Iniciar Jupyter Notebook:**

```powershell
# 1. Ativar ambiente (se não estiver ativo)
aula01\Scripts\activate

# 2. Iniciar Jupyter
jupyter notebook
# ou
jupyter lab
```

### **Selecionar Kernel no Jupyter:**

1. **No Jupyter Notebook:**
   - `Kernel` → `Change kernel` → `aula01`

2. **No JupyterLab:**
   - Clique no nome do kernel (canto superior direito)
   - Selecione `aula01`

### **Verificar Instalações:**

```python
# Testar no notebook ou Python shell
import requests
import pandas as pd
import bs4
import lxml

print("✅ Todas as bibliotecas funcionando!")
print(f"📦 Requests: {requests.__version__}")
print(f"📊 Pandas: {pd.__version__}")
```

---

## 📁 Estrutura de Arquivos

```
AGOSTO2025/
├── aula01/                    # 📁 Ambiente virtual
│   ├── Scripts/              # 🔧 Scripts do ambiente (Windows)
│   ├── Lib/                  # 📚 Bibliotecas instaladas
│   └── pyvenv.cfg            # ⚙️ Configuração do ambiente
├── data/
│   └── requirements.txt      # 📋 Lista de dependências
└── notebooks/                # 📓 Seus notebooks Jupyter
    ├── 01_requisicao.ipynb
    ├── 02_analise.ipynb
    └── ...
```

---

## 🔧 Comandos de Manutenção

### **Verificar Kernels Disponíveis:**
```powershell
jupyter kernelspec list
```

### **Atualizar Dependências:**
```powershell
# Ativar ambiente primeiro
aula01\Scripts\activate

# Atualizar pip
python -m pip install --upgrade pip

# Atualizar biblioteca específica
python -m pip install --upgrade requests

# Atualizar todas as dependências
python -m pip install --upgrade -r data\requirements.txt
```

### **Listar Bibliotecas Instaladas:**
```powershell
pip list
```

### **Exportar Dependências Atuais:**
```powershell
pip freeze > requirements_atual.txt
```

### **Desativar Ambiente:**
```powershell
deactivate
```

---

## 🗑️ Remover Ambiente (se necessário)

### **1. Remover Kernel Jupyter:**
```powershell
jupyter kernelspec remove AULA01_KERNEL
```

### **2. Remover Ambiente Virtual:**
```powershell
# Desativar primeiro
deactivate

# Remover pasta completa
rmdir /s aula01
```

---

## ⚡ Comandos Rápidos - Resumo

```powershell
# === SETUP INICIAL (executar uma vez) ===
python -m venv aula01
aula01\Scripts\activate
python -m pip install ipykernel
python -m ipykernel install --user --name=AULA01_KERNEL --display-name="aula01"
python -m pip install -r data\requirements.txt

# === USO DIÁRIO ===
aula01\Scripts\activate
jupyter notebook

# === VERIFICAÇÃO ===
jupyter kernelspec list
pip list
```

---

## 🎯 Troubleshooting

### **Problema: Kernel não aparece no Jupyter**
```powershell
# Recriar kernel
python -m ipykernel install --user --name=AULA01_KERNEL --display-name="aula01" --force
```

### **Problema: ModuleNotFoundError nos notebooks**
```powershell
# Verificar se ambiente está ativo
# Deve mostrar (aula01) no início do prompt

# Reinstalar ipykernel
pip install --upgrade ipykernel
python -m ipykernel install --user --name=AULA01_KERNEL --display-name="aula01" --force
```

### **Problema: pip desatualizado**
```powershell
python -m pip install --upgrade pip
```

---

## ✅ Checklist de Verificação

- [ ] Ambiente virtual criado e ativado
- [ ] IPython kernel instalado
- [ ] Kernel Jupyter configurado
- [ ] Dependências do requirements.txt instaladas
- [ ] Jupyter iniciando corretamente
- [ ] Kernel "aula01" disponível na lista
- [ ] Importações funcionando nos notebooks

---

**🎉 Ambiente configurado e pronto para uso!**

Para iniciar um novo projeto, simplesmente:
1. Ative o ambiente: `aula01\Scripts\activate`
2. Inicie o Jupyter: `jupyter notebook`
3. Selecione o kernel "aula01"
4. Comece a codificar! 🚀