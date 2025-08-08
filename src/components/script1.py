# src/components/script_1_requisicao.py
"""
SCRIPT 1: REQUISITAR E EXTRAIR O CONTEÚDO DA PÁGINA
Objetivo: Fazer uma requisição HTTP e capturar o conteúdo bruto
"""

import requests

def fazer_requisicao(url):
    """
    Faz uma requisição HTTP simples para uma URL
    
    Args:
        url (str): URL do site a ser acessado
        
    Returns:
        str: Conteúdo HTML da página ou None se houver erro
    """
    try:
        print(f"Fazendo requisição para: {url}")
        
        # Headers básicos para simular um navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Fazendo a requisição
        response = requests.get(url, headers=headers, timeout=10)
        
        # Verificar se a requisição foi bem-sucedida
        response.raise_for_status()
        
        print(f"✅ Requisição bem-sucedida!")
        print(f"Status Code: {response.status_code}")
        print(f"Tamanho do conteúdo: {len(response.text)} caracteres")
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        return None

def main():
    """Função principal para testar a requisição"""
    
    # URL do G1 RSS Brasil
    url = "https://g1.globo.com/rss/g1/brasil/"
    
    print("=" * 50)
    print("SCRIPT 1: REQUISIÇÃO E EXTRAÇÃO")
    print("=" * 50)
    
    # Fazer a requisição
    conteudo = fazer_requisicao(url)
    
    if conteudo:
        print("\n" + "=" * 30)
        print("PRIMEIROS 500 CARACTERES:")
        print("=" * 30)
        print(conteudo[:500])
        print("...")
        
        print("\n" + "=" * 30)
        print("ÚLTIMOS 200 CARACTERES:")
        print("=" * 30)
        print("...")
        print(conteudo[-200:])
        
        print(f"\n✅ Sucesso! Conteúdo capturado com {len(conteudo)} caracteres.")
    else:
        print("\n❌ Falha ao capturar o conteúdo.")

if __name__ == "__main__":
    main()