# TechSolutions System

Este é um sistema web para gerenciamento de cadastros, incluindo clientes, funcionários, produtos e vendas. Ele foi desenvolvido utilizando Flask (Python) para o backend e HTML/CSS para o frontend, com um banco de dados MySQL para persistência dos dados.

## Visão Geral

O sistema TechSolutions oferece uma interface web para realizar cadastros de diferentes entidades. A página inicial (`index.html`) apresenta links para as páginas de cadastro de cada tipo:

* Clientes
* Funcionários
* Produtos
* Vendas

## Tecnologias Utilizadas

* **Backend:** Python, Flask
* **Banco de Dados:** MySQL
* **Frontend:** HTML, CSS

## Estrutura do Projeto

* **app.py:** Arquivo principal contendo a lógica do backend Flask, incluindo as rotas e a conexão com o banco de dados.
* **templates/:** Pasta contendo os arquivos HTML para as diferentes páginas do sistema (index.html, clientes.html, funcionarios.html, produtos.html, vendas.html).
* **static/:** Pasta para arquivos estáticos como imagens (ex: kaka.jpg).
* **techsolutions_db:** Banco de dados MySQL.

## Como Executar

1. **Pré-requisitos:**
    * Python 3 instalado.
    * MySQL instalado e em execução.
    * Bibliotecas Flask e mysql-connector-python instaladas: `pip install Flask mysql-connector-python`
    * Banco de dados `techsolutions_db` criado no MySQL.  Crie as tabelas necessárias (clientes, funcionarios, produtos, vendas) com as colunas correspondentes aos dados que você deseja armazenar.  Você precisará executar scripts SQL para criar as tabelas. Exemplo para a tabela clientes:
    ```sql
    CREATE TABLE clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        email VARCHAR(255),
        telefone VARCHAR(20),
        cidade VARCHAR(255),
        estado VARCHAR(2)
    );
    ```
    Repita o processo para as outras tabelas, adaptando os tipos de dados e nomes de colunas conforme sua necessidade.

2. **Configuração:**
    * No arquivo `app.py`, ajuste as configurações de conexão com o banco de dados (host, user, password, database) de acordo com suas configurações locais.

3. **Execução:**
    * Abra um terminal na pasta do projeto e execute o comando: `python app.py`

4. **Acesso:**
    * Abra o navegador web e acesse o endereço: `http://127.0.0.1:5000/`

## Funcionalidades

* **Página Inicial (`index.html`):** Apresenta o título do sistema, uma imagem e uma lista de links para as páginas de cadastro.
* **Cadastro de Clientes (`/clientes`):** Permite cadastrar novos clientes no banco de dados.
* **Cadastro de Funcionários (`/funcionarios`):** Permite cadastrar novos funcionários no banco de dados.
* **Cadastro de Produtos (`/produtos`):** Permite cadastrar novos produtos no banco de dados.
* **Cadastro de Vendas (`/vendas`):** Permite cadastrar novas vendas no banco de dados.

## Próximos Passos (Melhorias Sugeridas)

* **Implementar listagem, edição e exclusão:** Adicionar funcionalidades para listar, editar e excluir registros das tabelas.
* **Validação de dados:** Implementar validação nos formulários para garantir a integridade dos dados.
* **Tratamento de erros:** Adicionar tratamento de erros para lidar com possíveis problemas na conexão com o banco de dados ou durante o processamento dos dados.
* **Interface mais amigável:** Melhorar a interface do usuário com o uso de frameworks CSS (como Bootstrap ou Tailwind CSS) ou bibliotecas de componentes.
* **Segurança:** Implementar medidas de segurança para proteger o sistema contra ataques, como injeção de SQL.
* **Testes:** Escrever testes unitários e de integração para garantir a qualidade do código.

## Contribuição

Este projeto foi criado como um exemplo. Contribuições e sugestões são bem-vindas.

## Licença

Nenhuma licença específica foi definida para este projeto. Sinta-se à vontade para usar e modificar o código como desejar.
