import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import csv
import json
import time

class G1RSScraper:
    def __init__(self):
        self.url = "https://g1.globo.com/rss/g1/brasil/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.noticias = []
    
    def fazer_requisicao(self):
        """Faz a requisição HTTP para o feed RSS"""
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer requisição: {e}")
            return None
    
    def parsear_rss(self, xml_content):
        """Faz o parsing do XML do RSS"""
        try:
            root = ET.fromstring(xml_content)
            
            # Encontra todos os itens (notícias) no RSS
            items = root.findall('.//item')
            
            for item in items:
                noticia = self.extrair_dados_noticia(item)
                if noticia:
                    self.noticias.append(noticia)
            
            print(f"Total de notícias encontradas: {len(self.noticias)}")
            return True
            
        except ET.ParseError as e:
            print(f"Erro ao fazer parsing do XML: {e}")
            return False
    
    def extrair_dados_noticia(self, item):
        """Extrai os dados de cada notícia do XML"""
        try:
            noticia = {}
            
            # Título
            titulo = item.find('title')
            noticia['titulo'] = titulo.text if titulo is not None else "N/A"
            
            # Link
            link = item.find('link')
            noticia['link'] = link.text if link is not None else "N/A"
            
            # Descrição
            description = item.find('description')
            noticia['descricao'] = description.text if description is not None else "N/A"
            
            # Data de publicação
            pub_date = item.find('pubDate')
            if pub_date is not None:
                noticia['data_publicacao'] = pub_date.text
                noticia['data_formatada'] = self.formatar_data(pub_date.text)
            else:
                noticia['data_publicacao'] = "N/A"
                noticia['data_formatada'] = "N/A"
            
            # Categoria
            category = item.find('category')
            noticia['categoria'] = category.text if category is not None else "N/A"
            
            # GUID (identificador único)
            guid = item.find('guid')
            noticia['guid'] = guid.text if guid is not None else "N/A"
            
            # Data e hora da raspagem
            noticia['data_raspagem'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            return noticia
            
        except Exception as e:
            print(f"Erro ao extrair dados da notícia: {e}")
            return None
    
    def formatar_data(self, data_rss):
        """Converte a data do RSS para formato mais legível"""
        try:
            # Formato típico do RSS: "Wed, 08 Aug 2025 10:30:00 -0300"
            data_obj = datetime.strptime(data_rss[:25], "%a, %d %b %Y %H:%M:%S")
            return data_obj.strftime("%d/%m/%Y %H:%M:%S")
        except:
            return data_rss
    
    def salvar_csv(self, nome_arquivo="noticias_g1_brasil.csv"):
        """Salva as notícias em arquivo CSV"""
        if not self.noticias:
            print("Nenhuma notícia para salvar.")
            return
        
        try:
            with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
                campos = ['titulo', 'link', 'descricao', 'categoria', 'data_publicacao', 
                         'data_formatada', 'data_raspagem', 'guid']
                
                writer = csv.DictWriter(arquivo, fieldnames=campos)
                writer.writeheader()
                
                for noticia in self.noticias:
                    writer.writerow(noticia)
            
            print(f"Dados salvos em: {nome_arquivo}")
            
        except Exception as e:
            print(f"Erro ao salvar CSV: {e}")
    
    def salvar_json(self, nome_arquivo="noticias_g1_brasil.json"):
        """Salva as notícias em arquivo JSON"""
        if not self.noticias:
            print("Nenhuma notícia para salvar.")
            return
        
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(self.noticias, arquivo, ensure_ascii=False, indent=2)
            
            print(f"Dados salvos em: {nome_arquivo}")
            
        except Exception as e:
            print(f"Erro ao salvar JSON: {e}")
    
    def exibir_noticias(self, limite=5):
        """Exibe as primeiras notícias na tela"""
        if not self.noticias:
            print("Nenhuma notícia encontrada.")
            return
        
        print(f"\n{'='*80}")
        print(f"ÚLTIMAS NOTÍCIAS DO G1 BRASIL")
        print(f"{'='*80}")
        
        for i, noticia in enumerate(self.noticias[:limite], 1):
            print(f"\n{i}. {noticia['titulo']}")
            print(f"   Data: {noticia['data_formatada']}")
            print(f"   Categoria: {noticia['categoria']}")
            print(f"   Link: {noticia['link']}")
            print(f"   Descrição: {noticia['descricao'][:150]}...")
            print("-" * 80)
    
    def executar_raspagem(self, salvar_arquivos=True, exibir=True, limite_exibicao=5):
        """Executa todo o processo de raspagem"""
        print("Iniciando raspagem do G1 RSS Brasil...")
        print(f"URL: {self.url}")
        
        # Fazer requisição
        xml_content = self.fazer_requisicao()
        if not xml_content:
            return False
        
        # Parsear RSS
        sucesso = self.parsear_rss(xml_content)
        if not sucesso:
            return False
        
        # Exibir resultados
        if exibir:
            self.exibir_noticias(limite_exibicao)
        
        # Salvar arquivos
        if salvar_arquivos:
            self.salvar_csv()
            self.salvar_json()
        
        return True

# Função para executar o scraper
def main():
    """Função principal para executar o scraper"""
    scraper = G1RSScraper()
    
    try:
        sucesso = scraper.executar_raspagem(
            salvar_arquivos=True,  # Salvar em CSV e JSON
            exibir=True,          # Mostrar notícias na tela
            limite_exibicao=10    # Mostrar 10 primeiras notícias
        )
        
        if sucesso:
            print(f"\nRaspagem concluída com sucesso!")
            print(f"Total de notícias coletadas: {len(scraper.noticias)}")
        else:
            print("Falha na raspagem.")
            
    except KeyboardInterrupt:
        print("\nRaspagem interrompida pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Exemplo de uso com monitoramento contínuo
def monitorar_noticias(intervalo_minutos=30):
    """Monitora o feed RSS em intervalos regulares"""
    print(f"Iniciando monitoramento a cada {intervalo_minutos} minutos...")
    
    while True:
        try:
            print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Verificando novas notícias...")
            
            scraper = G1RSScraper()
            scraper.executar_raspagem(
                salvar_arquivos=True,
                exibir=False,
                limite_exibicao=0
            )
            
            print(f"Próxima verificação em {intervalo_minutos} minutos...")
            time.sleep(intervalo_minutos * 60)
            
        except KeyboardInterrupt:
            print("\nMonitoramento interrompido.")
            break
        except Exception as e:
            print(f"Erro no monitoramento: {e}")
            time.sleep(60)  # Aguarda 1 minuto antes de tentar novamente

if __name__ == "__main__":
    # Execução única
    main()
    
    # Para monitoramento contínuo, descomente a linha abaixo:
    # monitorar_noticias(30)  # Verifica a cada 30 minutos