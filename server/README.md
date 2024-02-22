#### 🖥️ Server

Servidor desenvolvido em Python com o framework Flask e bibliotecas FlaskCors, FlaskSQLAlchemy, FlaskWTF e PyTest. A persistência dos 
dados ocorre por meio de uma base em SQLite, e as operações são executadas a partir do modelo, que conta com uma camada de repositório 
embutida. Além disso, as funcionalidades da aplicação são segmentadas na camada de serviços, acessada a partir das rotas. Existe também 
um módulo específico para testes, que valida cada uma das rotas utilizando o `pytest`.