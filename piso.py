import json
import os
from datetime import datetime

class SistemaGestao:
    def __init__(self):
        self.arquivo_dados = 'dados_pisos.json'
        self.dados = self.carregar_dados()
    
    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {'clientes': [], 'materiais': [], 'vendas': []}
        return {'clientes': [], 'materiais': [], 'vendas': []}
    
    def salvar_dados(self):
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, ensure_ascii=False, indent=2)
        print("✓ Dados salvos com sucesso!")
    
    def adicionar_cliente(self):
        print("\n=== CADASTRAR NOVO CLIENTE ===")
        cliente = {}
        cliente['id'] = len(self.dados['clientes']) + 1
        cliente['nome'] = input("Nome: ").strip()
        cliente['telefone'] = input("Telefone: ").strip()
        cliente['cidade'] = input("Cidade: ").strip()
        cliente['endereco'] = input("Endereço: ").strip()
        cliente['transportador'] = input("Transportador: ").strip()
        cliente['cnpj'] = input("CNPJ (opcional): ").strip()
        cliente['data_cadastro'] = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        self.dados['clientes'].append(cliente)
        print(f"✓ Cliente {cliente['nome']} cadastrado com ID: {cliente['id']}")
    
    def adicionar_material(self):
        print("\n=== CADASTRAR NOVO MATERIAL ===")
        material = {}
        material['id'] = len(self.dados['materiais']) + 1
        
        # Tipo do material
        print("Tipo do material:")
        print("1 - Piso")
        print("2 - Revestimento")
        tipo_opcao = input("Escolha (1 ou 2): ").strip()
        material['tipo'] = "Piso" if tipo_opcao == "1" else "Revestimento"
        
        material['tamanho'] = input("Tamanho (ex: 60x60): ").strip()
        
        # Acabamento
        print("Acabamento:")
        print("1 - Bold")
        print("2 - Retificado")
        acabamento_opcao = input("Escolha (1 ou 2): ").strip()
        material['acabamento'] = "Bold" if acabamento_opcao == "1" else "Retificado"
        
        # Preço e peso
        try:
            material['preco_pallet'] = float(input("Preço por pallet (R$): ").strip())
            material['peso'] = float(input("Peso (kg): ").strip())
        except ValueError:
            print("⚠ Erro: Digite apenas números para preço e peso")
            return
        
        material['data_cadastro'] = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        self.dados['materiais'].append(material)
        print(f"✓ Material cadastrado com ID: {material['id']}")
    
    def listar_clientes(self):
        if not self.dados['clientes']:
            print("\nNenhum cliente cadastrado.")
            return
        
        print("\n=== CLIENTES CADASTRADOS ===")
        for cliente in self.dados['clientes']:
            print(f"\nID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Cidade: {cliente['cidade']}")
            print(f"Endereço: {cliente['endereco']}")
            print(f"Transportador: {cliente['transportador']}")
            if cliente['cnpj']:
                print(f"CNPJ: {cliente['cnpj']}")
            print(f"Cadastrado em: {cliente['data_cadastro']}")
            print("-" * 40)
    
    def listar_materiais(self):
        if not self.dados['materiais']:
            print("\nNenhum material cadastrado.")
            return
        
        print("\n=== MATERIAIS CADASTRADOS ===")
        for material in self.dados['materiais']:
            print(f"\nID: {material['id']}")
            print(f"Tipo: {material['tipo']}")
            print(f"Tamanho: {material['tamanho']}")
            print(f"Acabamento: {material['acabamento']}")
            print(f"Preço por pallet: R$ {material['preco_pallet']:.2f}")
            print(f"Peso: {material['peso']} kg")
            print(f"Cadastrado em: {material['data_cadastro']}")
            print("-" * 40)
    
    def buscar_cliente(self):
        if not self.dados['clientes']:
            print("\nNenhum cliente cadastrado.")
            return
        
        busca = input("Digite o nome ou ID do cliente: ").strip().lower()
        encontrados = []
        
        for cliente in self.dados['clientes']:
            if (busca in cliente['nome'].lower() or 
                busca == str(cliente['id'])):
                encontrados.append(cliente)
        
        if not encontrados:
            print("Nenhum cliente encontrado.")
        else:
            print(f"\n=== {len(encontrados)} CLIENTE(S) ENCONTRADO(S) ===")
            for cliente in encontrados:
                print(f"\nID: {cliente['id']} - {cliente['nome']}")
                print(f"Telefone: {cliente['telefone']}")
                print(f"Cidade: {cliente['cidade']}")
    
    def menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("    SISTEMA DE GESTÃO DE PISOS E REVESTIMENTOS")
            print("="*50)
            print("1. Cadastrar Cliente")
            print("2. Cadastrar Material") 
            print("3. Listar Clientes")
            print("4. Listar Materiais")
            print("5. Buscar Cliente")
            print("6. Salvar Dados")
            print("0. Sair")
            print("="*50)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.adicionar_cliente()
            elif opcao == "2":
                self.adicionar_material()
            elif opcao == "3":
                self.listar_clientes()
            elif opcao == "4":
                self.listar_materiais()
            elif opcao == "5":
                self.buscar_cliente()
            elif opcao == "6":
                self.salvar_dados()
            elif opcao == "0":
                self.salvar_dados()
                print("Obrigado por usar o sistema! Até logo!")
                break
            else:
                print("⚠ Opção inválida! Tente novamente.")

def main():
    print("Inicializando Sistema de Gestão...")
    sistema = SistemaGestao()
    sistema.menu_principal()

if __name__ == "__main__":
    main()
