#### 🖥️ Server

Servidor desenvolvido em Python com o framework Flask e biblitoecas FlaskCors, FlaskSQLAlchemy, FlaskWTF e PyTest. A persistência dos 
dados ocorre por meio de uma base em SQLite e as operações ocorrem a partir do modelo, este conta com uma camada de repositório embutida. 
Além disso, a segmentação das funcionalidades da aplicação na camada de serviços, à qual é acessada a partir das rotas. Existe também um 
módulo específico para testes, que valida cada uma das rotas, a partir do `pytest`.