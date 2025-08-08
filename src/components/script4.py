# src/components/script_4_criar_csv.py
"""
SCRIPT 4: CRIAR CSV COM INFORMAÇÕES EXTRAÍDAS
Objetivo: Salvar os dados extraídos em formato CSV para análise
"""

import requests
import xml.etree.ElementTree as ET
import csv
import json
from datetime import datetime
import os

def fazer_requisicao(url):
    """Faz requisição HTTP (dos scripts anteriores)"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        return None

def parsear_xml_rss(conteudo_xml):
    """Parseia XML RSS (do Script 3)"""
    try:
        root = ET.fromstring(conteudo_xml)
        items = root.findall('.//item')
        return items
    except ET.ParseError as e:
        print(f"❌ Erro ao parsear XML: {e}")
        return []

def extrair_informacoes_item(item):
    """Extrai informações de um item (do Script 3)"""
    dados = {}
    
    titulo_elem = item.find('title')
    dados['titulo'] = titulo_elem.text if titulo_elem is not None else "N/A"
    
    link_elem = item.find('link')
    dados['link'] = link_elem.text if link_elem is not None else "N/A"
    
    desc_elem = item.find('description')
    dados['descricao'] = desc_elem.text if desc_elem is not None else "N/A"
    
    data_elem = item.find('pubDate')
    dados['data_publicacao'] = data_elem.text if data_elem is not None else "N/A"
    
    categoria_elem = item.find('category')
    dados['categoria'] = categoria_elem.text if categoria_elem is not None else "N/A"
    
    guid_elem = item.find('guid')
    dados['guid'] = guid_elem.text if guid_elem is not None else "N/A"
    
    dados['extraido_em'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return dados

def processar_todos_items(items):
    """Processa todos os items (do Script 3)"""
    dados_extraidos = []
    
    for item in items:
        dados_item = extrair_informacoes_item(item)
        dados_extraidos.append(dados_item)
    
    return dados_extraidos

def criar_csv(dados, nome_arquivo="noticias_g1.csv"):
    """
    Cria arquivo CSV com os dados extraídos
    
    Args:
        dados (list): Lista de dicionários com os dados
        nome_arquivo (str): Nome do arquivo CSV
        
    Returns:
        bool: True se criou com sucesso
    """
    try:
        print(f"\n🔄 Criando arquivo CSV: {nome_arquivo}")
        
        # Definir colunas do CSV
        colunas = [
            'titulo',
            'data_publicacao', 
            'categoria',
            'link',
            'descricao',
            'guid',
            'extraido_em'
        ]
        
        # Criar o arquivo CSV
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            
            # Escrever cabeçalho
            writer.writeheader()
            
            # Escrever dados
            for linha in dados:
                writer.writerow(linha)
        
        print(f"✅ CSV criado com sucesso!")
        print(f"📁 Arquivo: {nome_arquivo}")
        print(f"📊 Registros salvos: {len(dados)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar CSV: {e}")
        return False

def criar_json_backup(dados, nome_arquivo="noticias_g1.json"):
    """
    Cria backup em JSON dos dados extraídos
    
    Args:
        dados (list): Lista de dicionários com os dados
        nome_arquivo (str): Nome do arquivo JSON
    """
    try:
        print(f"\n🔄 Criando backup JSON: {nome_arquivo}")
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=2)
        
        print(f"✅ Backup JSON criado!")
        
    except Exception as e:
        print(f"❌ Erro ao criar JSON: {e}")

def verificar_arquivos_criados():
    """
    Verifica e exibe informações sobre os arquivos criados
    """
    print(f"\n" + "=" * 50)
    print("📁 VERIFICAÇÃO DOS ARQUIVOS CRIADOS")
    print("=" * 50)
    
    arquivos = ["noticias_g1.csv", "noticias_g1.json"]
    
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            tamanho = os.path.getsize(arquivo)
            print(f"✅ {arquivo}")
            print(f"   📏 Tamanho: {tamanho:,} bytes")
            
            # Para CSV, contar linhas
            if arquivo.endswith('.csv'):
                with open(arquivo, 'r', encoding='utf-8') as f:
                    linhas = len(f.readlines())
                print(f"   📊 Linhas: {linhas} (incluindo cabeçalho)")
        else:
            print(f"❌ {arquivo} - Não encontrado")

def exibir_preview_csv(nome_arquivo="noticias_g1.csv", linhas=5):
    """
    Exibe um preview do arquivo CSV criado
    
    Args:
        nome_arquivo (str): Nome do arquivo CSV
        linhas (int): Quantas linhas mostrar
    """
    try:
        print(f"\n" + "=" * 60)
        print(f"👀 PREVIEW DO CSV (primeiras {linhas} linhas)")
        print("=" * 60)
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            
            for i, linha in enumerate(reader):
                if i == 0:
                    # Cabeçalho
                    print("CABEÇALHO:")
                    print(" | ".join(linha))
                    print("-" * 60)
                elif i <= linhas:
                    # Dados
                    print(f"Linha {i}:")
                    for j, valor in enumerate(linha):
                        coluna = linha[0] if i == 0 else reader.fieldnames[j] if hasattr(reader, 'fieldnames') else f"Col{j}"
                        # Truncar valores muito longos
                        valor_truncado = valor[:50] + "..." if len(valor) > 50 else valor
                        print(f"  {j+1}. {valor_truncado}")
                    print("-" * 40)
                else:
                    break
                    
    except Exception as e:
        print(f"❌ Erro ao ler CSV: {e}")

def gerar_relatorio_final(dados):
    """
    Gera relatório final da execução
    
    Args:
        dados (list): Dados processados
    """
    print(f"\n" + "=" * 60)
    print("📋 RELATÓRIO FINAL - SCRIPT 4")
    print("=" * 60)
    
    # Estatísticas básicas
    print(f"📊 Total de notícias processadas: {len(dados)}")
    
    # Contar categorias
    categorias = {}
    for item in dados:
        cat = item['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1
    
    print(f"📂 Categorias encontradas: {len(categorias)}")
    
    # Top 3 categorias
    top_categorias = sorted(categorias.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\n🏆 TOP 3 CATEGORIAS:")
    for i, (categoria, count) in enumerate(top_categorias, 1):
        print(f"   {i}. {categoria}: {count} notícias")
    
    # Informações de tempo
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n⏰ Processamento concluído em: {agora}")
    
    print("\n✅ ARQUIVOS GERADOS:")
    print("   📄 noticias_g1.csv - Dados em formato tabular")
    print("   📄 noticias_g1.json - Backup estruturado")

def main():
    """Função principal do Script 4 - Versão completa"""
    
    url = "https://g1.globo.com/rss/g1/brasil/"
    
    print("=" * 60)
    print("SCRIPT 4: CRIAR CSV COM INFORMAÇÕES EXTRAÍDAS")
    print("=" * 60)
    
    # Etapa 1: Requisição (Scripts 1-3)
    print("🔄 Etapa 1: Fazendo requisição...")
    conteudo = fazer_requisicao(url)
    if not conteudo:
        return
    print("✅ Conteúdo capturado!")
    
    # Etapa 2: Parsing (Scripts 2-3)
    print("\n🔄 Etapa 2: Parseando XML...")
    items = parsear_xml_rss(conteudo)
    if not items:
        return
    print(f"✅ {len(items)} items encontrados!")
    
    # Etapa 3: Extração (Script 3)
    print("\n🔄 Etapa 3: Extraindo informações...")
    dados_extraidos = processar_todos_items(items)
    print(f"✅ {len(dados_extraidos)} registros extraídos!")
    
    # Etapa 4: Criar CSV (NOVO!)
    print("\n🔄 Etapa 4: Criando arquivo CSV...")
    sucesso_csv = criar_csv(dados_extraidos)
    
    # Etapa 5: Backup JSON (NOVO!)
    print("\n🔄 Etapa 5: Criando backup JSON...")
    criar_json_backup(dados_extraidos)
    
    # Etapa 6: Verificações (NOVO!)
    verificar_arquivos_criados()
    
    # Etapa 7: Preview (NOVO!)
    if sucesso_csv:
        exibir_preview_csv()
    
    # Etapa 8: Relatório final (NOVO!)
    gerar_relatorio_final(dados_extraidos)
    
    print(f"\n" + "=" * 60)
    print("🎉 SCRIPT 4 CONCLUÍDO COM SUCESSO!")
    print("🎯 Todos os 4 scripts executados: Requisição → HTML → Parsing → CSV")
    print("=" * 60)

if __name__ == "__main__":
    main()