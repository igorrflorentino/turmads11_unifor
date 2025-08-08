# src/components/script_2_apresentar_html.py
"""
SCRIPT 2: APRESENTAR O HTML CAPTURADO
Objetivo: Capturar e apresentar o HTML de forma organizada
"""

import requests

def fazer_requisicao(url):
    """
    Faz uma requisição HTTP simples para uma URL
    """
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

def salvar_html(conteudo, nome_arquivo="pagina_capturada.html"):
    """
    Salva o HTML capturado em um arquivo
    
    Args:
        conteudo (str): Conteúdo HTML
        nome_arquivo (str): Nome do arquivo para salvar
    """
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        print(f"✅ HTML salvo em: {nome_arquivo}")
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")
        return False

def apresentar_estrutura_html(conteudo):
    """
    Apresenta informações sobre a estrutura do HTML
    
    Args:
        conteudo (str): Conteúdo HTML
    """
    print("\n" + "=" * 50)
    print("ANÁLISE DA ESTRUTURA HTML")
    print("=" * 50)
    
    # Informações básicas
    print(f"📊 Tamanho total: {len(conteudo)} caracteres")
    print(f"📊 Número de linhas: {len(conteudo.splitlines())}")
    
    # Contar tags principais
    tags_importantes = ['<item>', '<title>', '<link>', '<description>', '<pubDate>', '<category>']
    
    print("\n📋 CONTAGEM DE TAGS:")
    for tag in tags_importantes:
        count = conteudo.count(tag)
        print(f"   {tag}: {count} ocorrências")
    
    # Mostrar início e fim
    print("\n" + "=" * 30)
    print("INÍCIO DO HTML (primeiras 10 linhas):")
    print("=" * 30)
    linhas = conteudo.splitlines()
    for i, linha in enumerate(linhas[:10], 1):
        print(f"{i:2d}: {linha}")
    
    print("\n" + "=" * 30)
    print("FINAL DO HTML (últimas 5 linhas):")
    print("=" * 30)
    for i, linha in enumerate(linhas[-5:], len(linhas)-4):
        print(f"{i:2d}: {linha}")

def extrair_amostra_item(conteudo):
    """
    Extrai e mostra uma amostra de um item do RSS
    
    Args:
        conteudo (str): Conteúdo HTML/XML
    """
    print("\n" + "=" * 50)
    print("AMOSTRA DE UM ITEM DO RSS")
    print("=" * 50)
    
    # Encontrar o primeiro item
    inicio_item = conteudo.find('<item>')
    fim_item = conteudo.find('</item>') + len('</item>')
    
    if inicio_item != -1 and fim_item != -1:
        item_completo = conteudo[inicio_item:fim_item]
        print("📄 PRIMEIRO ITEM ENCONTRADO:")
        print("-" * 30)
        
        # Quebrar em linhas para melhor visualização
        linhas_item = item_completo.split('>')
        for linha in linhas_item:
            if linha.strip():
                print(linha + '>')
    else:
        print("❌ Nenhum item encontrado no conteúdo")

def main():
    """Função principal do Script 2"""
    
    url = "https://g1.globo.com/rss/g1/brasil/"
    
    print("=" * 50)
    print("SCRIPT 2: APRESENTAR HTML CAPTURADO")
    print("=" * 50)
    
    # 1. Fazer requisição
    print("🔄 Fazendo requisição...")
    conteudo = fazer_requisicao(url)
    
    if not conteudo:
        print("❌ Não foi possível capturar o conteúdo")
        return
    
    print("✅ Conteúdo capturado com sucesso!")
    
    # 2. Salvar HTML em arquivo
    print("\n🔄 Salvando HTML em arquivo...")
    salvar_html(conteudo, "g1_rss_capturado.html")
    
    # 3. Apresentar estrutura
    apresentar_estrutura_html(conteudo)
    
    # 4. Mostrar amostra de item
    extrair_amostra_item(conteudo)
    
    print("\n" + "=" * 50)
    print("✅ SCRIPT 2 CONCLUÍDO!")
    print("Verifique o arquivo 'g1_rss_capturado.html' gerado")
    print("=" * 50)

if __name__ == "__main__":
    main()