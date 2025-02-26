### **Descrição:**

Nesta atividade, você deverá desenvolver uma **API RESTful** utilizando **Flask**, que simulará um sistema básico de gestão de um supermercado. A API deverá permitir a manipulação de dados armazenados em **arquivos CSV**, utilizando os quatro principais métodos HTTP:

- **GET** → Para buscar informações
- **POST** → Para adicionar novos registros
- **PUT** → Para atualizar informações existentes
- **DELETE** → Para remover registros

### **Requisitos:**

1. **Arquivos CSV:**
    
    A API deverá gerenciar os seguintes arquivos de dados:
    
    - **Clientes.csv**
        - ID (inteiro, único)
        - Nome (texto)
        - Sobrenome (texto)
        - Data de nascimento (AAAA-MM-DD)
        - CPF (texto, único)
    - **Produtos.csv**
        - ID (inteiro, único)
        - Nome (texto)
        - Fornecedor (texto)
        - Quantidade (inteiro)
    - **OrdemDeVendas.csv**
        - ID da Ordem (inteiro, único)
        - Cliente (ID do cliente)
        - Produto (ID do produto)
2. **Funcionalidades da API:**
    
    Sua API deverá conter os seguintes endpoints para manipulação dos arquivos CSV:
    
    - **Clientes**
        - `GET /clientes` → Listar todos os clientes
        - `POST /clientes` → Adicionar um novo cliente
        - `PUT /clientes` → Atualizar os dados de um cliente
        - `DELETE /clientes/<id>` → Remover um cliente
    - **Produtos**
        - `GET /produtos` → Listar todos os produtos
        - `POST /produtos` → Adicionar um novo produto
        - `PUT /produtos` → Atualizar os dados de um produto
        - `DELETE /produtos/<id>` → Remover um produto
    - **Ordens de Venda**
        - `GET /ordens` → Listar todas as ordens de venda
        - `POST /ordens` → Criar uma nova ordem de venda
        - `PUT /ordens` → Atualizar uma ordem de venda
        - `DELETE /ordens/<id>` → Remover uma ordem de venda
3. **Regras de Negócio:**
    - O **ID** de cada entidade deve ser **único** e gerado automaticamente.

### **Entrega:**

- Código-fonte da API em um repositório GitHub.
- Documentação breve (Readme) sobre como rodar a API e os endpoints disponíveis.

### **Critérios Avaliativos**

O projeto será avaliado com um total de **100 pontos**, divididos da seguinte forma:

- **Desenvolvimento da API (50 pontos):** A qualidade do código, a implementação correta dos endpoints e o cumprimento dos requisitos serão analisados.
- **Teste prático no dia da entrega (50 pontos):** Todos os integrantes do grupo participarão de um teste prático para demonstrar o funcionamento da API e esclarecer dúvidas sobre o desenvolvimento.