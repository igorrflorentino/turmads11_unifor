# 🚀 Setup Completo: Jupyter Kernel para Web Scraping G1

Este guia fornece instruções passo a passo para criar um ambiente Python dedicado e configurar um kernel Jupyter para executar os notebooks de web scraping do G1 RSS.

## 📋 Índice

- [Pré-requisitos](#-pré-requisitos)
- [Passo 1: Criar Ambiente Virtual](#-passo-1-criar-ambiente-virtual)
- [Passo 2: Ativar o Ambiente](#-passo-2-ativar-o-ambiente)
- [Passo 3: Instalar Dependências](#-passo-3-instalar-dependências)
- [Passo 4: Criar Kernel Jupyter](#-passo-4-criar-kernel-jupyter)
- [Passo 5: Verificar Instalação](#-passo-5-verificar-instalação)
- [Executando os Notebooks](#-executando-os-notebooks)
- [Solução de Problemas](#-solução-de-problemas)
- [Comandos de Manutenção](#-comandos-de-manutenção)

---

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8+** (recomendado: Python 3.10 ou superior)
- **pip** (gerenciador de pacotes Python)
- **Jupyter Notebook** ou **JupyterLab**

### Verificar instalações:

```bash
# Verificar versão do Python
python --version
# ou
python3 --version

# Verificar pip
pip --version

# Verificar Jupyter
jupyter --version
```

---

## 🏗️ Passo 1: Criar Ambiente Virtual

### Opção A: Usando `venv` (Recomendado)

```bash
# Criar ambiente virtual
python -m venv venv_g1_scraper

# No Windows:
python -m venv venv_g1_scraper

# No Linux/Mac:
python3 -m venv venv_g1_scraper
```

### Opção B: Usando `conda` (Se preferir)

```bash
# Criar ambiente conda
conda create -n g1_scraper python=3.10 -y
```

---

## 🔄 Passo 2: Ativar o Ambiente

### Para `venv`:

#### Windows:
```cmd
# Command Prompt
venv_g1_scraper\Scripts\activate

# PowerShell
venv_g1_scraper\Scripts\Activate.ps1

# Git Bash
source venv_g1_scraper/Scripts/activate
```

#### Linux/Mac:
```bash
source venv_g1_scraper/bin/activate
```

### Para `conda`:
```bash
conda activate g1_scraper
```

### ✅ Verificar ativação:
Após ativar, você deve ver o nome do ambiente no início do prompt:
```
(venv_g1_scraper) C:\seu\diretorio>
```

---

## 📦 Passo 3: Instalar Dependências

### 3.1. Atualizar pip e ferramentas básicas:
```bash
python -m pip install --upgrade pip setuptools wheel
```

### 3.2. Instalar dependências principais:
```bash
# Dependências essenciais
pip install requests>=2.28.0
pip install ipykernel>=6.0.0
pip install jupyter>=1.0.0

# Dependências opcionais (recomendadas)
pip install beautifulsoup4>=4.11.0
pip install lxml>=4.9.0
pip install pandas>=1.5.0
```

### 3.3. Instalar do requirements.txt (se disponível):
```bash
pip install -r requirements.txt
```

### 3.4. Verificar instalações:
```bash
pip list
```

---

## 🎯 Passo 4: Criar Kernel Jupyter

### 4.1. Instalar o kernel no Jupyter:
```bash
# Instalar kernel com nome personalizado
python -m ipykernel install --user --name=g1_scraper --display-name="G1 Scraper - Python"
```

### 4.2. Verificar se o kernel foi criado:
```bash
jupyter kernelspec list
```

Você deve ver uma saída similar a:
```
Available kernels:
  g1_scraper    /home/user/.local/share/jupyter/kernels/g1_scraper
  python3       /home/user/.local/share/jupyter/kernels/python3
```

---

## ✅ Passo 5: Verificar Instalação

### 5.1. Testar importações:
```bash
python -c "import requests, xml.etree.ElementTree, csv, json; print('✅ Todas as dependências OK!')"
```

### 5.2. Testar requisição simples:
```bash
python -c "
import requests
try:
    response = requests.get('https://httpbin.org/status/200', timeout=5)
    print('✅ Conexão de rede funcionando!')
except:
    print('❌ Problema de conectividade')
"
```

### 5.3. Iniciar Jupyter:
```bash
# Jupyter Notebook
jupyter notebook

# ou JupyterLab
jupyter lab
```

---

## 📚 Executando os Notebooks

### 1. Abrir Jupyter:
```bash
jupyter notebook
# ou
jupyter lab
```

### 2. Selecionar o kernel correto:
- No Jupyter Notebook: `Kernel` → `Change kernel` → `G1 Scraper - Python`
- No JupyterLab: Clique no nome do kernel no canto superior direito

### 3. Ordem de execução dos notebooks:
1. **01_requisicao_e_extracao.ipynb** - Requisição básica
2. **02_apresentar_html_capturado.ipynb** - Análise da estrutura
3. **03_parsear_tags_extrair_dados.ipynb** - Parsing e extração
4. **04_criar_csv_dados_finais.ipynb** - Criação do CSV final

### 4. Estrutura de arquivos esperada:
```
projeto_g1_scraper/
├── 01_requisicao_e_extracao.ipynb
├── 02_apresentar_html_capturado.ipynb
├── 03_parsear_tags_extrair_dados.ipynb
├── 04_criar_csv_dados_finais.ipynb
├── requirements.txt
├── README.md
├── notebook_outputs/          # Criado automaticamente
└── dados_finais/             # Criado automaticamente
```

---

## 🔧 Solução de Problemas

### Problema: Kernel não aparece no Jupyter

**Solução:**
```bash
# Reinstalar o kernel
python -m ipykernel install --user --name=g1_scraper --display-name="G1 Scraper - Python" --force

# Reiniciar Jupyter
jupyter notebook
```

### Problema: Erro de importação de módulos

**Solução:**
```bash
# Verificar se está no ambiente correto
which python
# ou
where python

# Reinstalar dependências
pip install --force-reinstall requests ipykernel
```

### Problema: "ModuleNotFoundError" nos notebooks

**Solução:**
1. Verificar se o kernel correto está selecionado
2. Reinstalar ipykernel:
```bash
pip install --upgrade ipykernel
python -m ipykernel install --user --name=g1_scraper --display-name="G1 Scraper - Python" --force
```

### Problema: Erro de permissão no Windows

**Solução:**
```powershell
# Executar PowerShell como Administrador e executar:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: Conexão SSL/HTTPS

**Solução:**
```bash
# Atualizar certificados
pip install --upgrade certifi

# Ou usar requests com verificação desabilitada (só para teste)
# requests.get(url, verify=False)
```

---

## 🛠️ Comandos de Manutenção

### Atualizar dependências:
```bash
pip install --upgrade requests beautifulsoup4 lxml pandas ipykernel
```

### Listar kernels instalados:
```bash
jupyter kernelspec list
```

### Remover kernel (se necessário):
```bash
jupyter kernelspec remove g1_scraper
```

### Recriar kernel:
```bash
jupyter kernelspec remove g1_scraper
python -m ipykernel install --user --name=g1_scraper --display-name="G1 Scraper - Python"
```

### Desativar ambiente:
```bash
# Para venv
deactivate

# Para conda
conda deactivate
```

### Remover ambiente (se necessário):
```bash
# Para venv
rm -rf venv_g1_scraper  # Linux/Mac
rmdir /s venv_g1_scraper  # Windows

# Para conda
conda env remove -n g1_scraper
```

---

## 📝 Resumo dos Comandos Principais

```bash
# 1. Criar e ativar ambiente
python -m venv venv_g1_scraper
source venv_g1_scraper/bin/activate  # Linux/Mac
# venv_g1_scraper\Scripts\activate   # Windows

# 2. Instalar dependências
pip install --upgrade pip
pip install requests ipykernel jupyter beautifulsoup4 lxml pandas

# 3. Criar kernel
python -m ipykernel install --user --name=g1_scraper --display-name="G1 Scraper - Python"

# 4. Verificar
jupyter kernelspec list

# 5. Iniciar Jupyter
jupyter notebook
```

---

## 🎯 Próximos Passos

Após seguir este guia:

1. ✅ Ambiente Python configurado
2. ✅ Kernel Jupyter instalado
3. ✅ Dependências instaladas
4. ✅ Pronto para executar os notebooks

**Agora você pode:**
- Abrir os notebooks na ordem correta
- Executar o scraping do G1 RSS
- Gerar dados em formato CSV
- Analisar as notícias capturadas

---

## Se encontrar problemas:

1. Verifique se seguiu todos os passos na ordem
2. Confirme que o ambiente está ativado
3. Teste as importações básicas
4. Consulte os logs de erro do Jupyter

**Comandos de diagnóstico:**
```bash
# Verificar ambiente
which python
pip list
jupyter --paths
jupyter kernelspec list

# Testar importações
python -c "import requests, xml.etree.ElementTree; print('OK')"
```

---

