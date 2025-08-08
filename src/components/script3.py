# src/components/script_3_parsear_tags.py
"""
SCRIPT 3: PARSEAR TAGS E EXTRAIR INFORMAÇÕES
Objetivo: Tratar o HTML/XML e extrair dados estruturados
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def fazer_requisicao(url):
    """Faz requisição HTTP (reutilizado dos scripts anteriores)"""
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
    """
    Faz o parsing do XML RSS usando ElementTree
    
    Args:
        conteudo_xml (str): Conteúdo XML do RSS
        
    Returns:
        list: Lista de elementos <item> parseados
    """
    try:
        print("🔄 Fazendo parsing do XML...")
        
        # Parsear o XML
        root = ET.fromstring(conteudo_xml)
        
        # Encontrar todos os itens
        items = root.findall('.//item')
        
        print(f"✅ XML parseado com sucesso!")
        print(f"📊 Total de itens encontrados: {len(items)}")
        
        return items
        
    except ET.ParseError as e:
        print(f"❌ Erro ao parsear XML: {e}")
        return []
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return []

def extrair_informacoes_item(item):
    """
    Extrai informações específicas de um item XML
    
    Args:
        item: Elemento XML do item
        
    Returns:
        dict: Dicionário com informações extraídas
    """
    dados = {}
    
    # Título
    titulo_elem = item.find('title')
    dados['titulo'] = titulo_elem.text if titulo_elem is not None else "N/A"
    
    # Link
    link_elem = item.find('link')
    dados['link'] = link_elem.text if link_elem is not None else "N/A"
    
    # Descrição
    desc_elem = item.find('description')
    dados['descricao'] = desc_elem.text if desc_elem is not None else "N/A"
    
    # Data de publicação
    data_elem = item.find('pubDate')
    dados['data_publicacao'] = data_elem.text if data_elem is not None else "N/A"
    
    # Categoria
    categoria_elem = item.find('category')
    dados['categoria'] = categoria_elem.text if categoria_elem is not None else "N/A"
    
    # GUID (identificador único)
    guid_elem = item.find('guid')
    dados['guid'] = guid_elem.text if guid_elem is not None else "N/A"
    
    # Adicionar timestamp da extração
    dados['extraido_em'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return dados

def processar_todos_items(items):
    """
    Processa todos os items e extrai informações
    
    Args:
        items: Lista de elementos XML
        
    Returns:
        list: Lista de dicionários com dados extraídos
    """
    print("\n🔄 Processando todos os items...")
    
    dados_extraidos = []
    
    for i, item in enumerate(items, 1):
        print(f"   Processando item {i}/{len(items)}")
        
        dados_item = extrair_informacoes_item(item)
        dados_extraidos.append(dados_item)
    
    print(f"✅ Processamento concluído!")
    print(f"📊 Total de registros extraídos: {len(dados_extraidos)}")
    
    return dados_extraidos

def exibir_amostra_dados(dados_extraidos, quantidade=3):
    """
    Exibe uma amostra dos dados extraídos
    
    Args:
        dados_extraidos (list): Lista com os dados
        quantidade (int): Quantos registros mostrar
    """
    print(f"\n" + "=" * 60)
    print(f"AMOSTRA DOS DADOS EXTRAÍDOS (primeiros {quantidade} registros)")
    print("=" * 60)
    
    for i, dados in enumerate(dados_extraidos[:quantidade], 1):
        print(f"\n📰 NOTÍCIA {i}:")
        print("-" * 40)
        print(f"🏷️  Título: {dados['titulo']}")
        print(f"📅 Data: {dados['data_publicacao']}")
        print(f"🔗 Link: {dados['link']}")
        print(f"📂 Categoria: {dados['categoria']}")
        print(f"📝 Descrição: {dados['descricao'][:100]}...")
        print(f"🆔 GUID: {dados['guid']}")
        print(f"⏰ Extraído em: {dados['extraido_em']}")

def exibir_estatisticas(dados_extraidos):
    """
    Exibe estatísticas dos dados extraídos
    
    Args:
        dados_extraidos (list): Lista com os dados
    """
    print(f"\n" + "=" * 50)
    print("📊 ESTATÍSTICAS DOS DADOS EXTRAÍDOS")
    print("=" * 50)
    
    # Contar categorias
    categorias = {}
    total_registros = len(dados_extraidos)
    
    for dados in dados_extraidos:
        categoria = dados['categoria']
        categorias[categoria] = categorias.get(categoria, 0) + 1
    
    print(f"📈 Total de registros: {total_registros}")
    print(f"📂 Total de categorias: {len(categorias)}")
    
    print("\n🏷️ DISTRIBUIÇÃO POR CATEGORIA:")
    for categoria, count in sorted(categorias.items(), key=lambda x: x[1], reverse=True):
        porcentagem = (count / total_registros) * 100
        print(f"   {categoria}: {count} registros ({porcentagem:.1f}%)")

def main():
    """Função principal do Script 3"""
    
    url = "https://g1.globo.com/rss/g1/brasil/"
    
    print("=" * 60)
    print("SCRIPT 3: PARSEAR TAGS E EXTRAIR INFORMAÇÕES")
    print("=" * 60)
    
    # 1. Fazer requisição (do Script 1)
    print("🔄 Etapa 1: Fazendo requisição...")
    conteudo = fazer_requisicao(url)
    
    if not conteudo:
        print("❌ Falha na requisição")
        return
    
    print("✅ Conteúdo capturado!")
    
    # 2. Parsear XML (novo)
    print("\n🔄 Etapa 2: Parseando XML...")
    items = parsear_xml_rss(conteudo)
    
    if not items:
        print("❌ Falha no parsing")
        return
    
    # 3. Extrair informações (novo)
    print("\n🔄 Etapa 3: Extraindo informações...")
    dados_extraidos = processar_todos_items(items)
    
    # 4. Exibir resultados
    print("\n🔄 Etapa 4: Apresentando resultados...")
    exibir_amostra_dados(dados_extraidos, 3)
    exibir_estatisticas(dados_extraidos)
    
    print(f"\n" + "=" * 60)
    print("✅ SCRIPT 3 CONCLUÍDO!")
    print(f"🎯 Próximo passo: Script 4 - Criar CSV com estes dados")
    print("=" * 60)
    
    # Retornar dados para possível uso em outros scripts
    return dados_extraidos

if __name__ == "__main__":
    main()