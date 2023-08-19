# [FastAPI](https://fastapi.tiangolo.com/)
O FastAPI é um moderno framework web de alto desempenho, construído usando a linguagem de programação Python. 
Ele é projetado para facilitar a criação de APIs (Interfaces de Programação de Aplicativos) de forma rápida, 
eficiente e segura.
## Características
**_Rápido :_** desempenho muito alto, igual ao NodeJS e Go (graças a Starlette e Pydantic). Um dos frameworks 
Python mais rápidos disponíveis .

**_Rápido para codificar :_** Aumente a velocidade para desenvolver recursos em cerca de 200% a 300%. *

**_Menos bugs :_** reduza cerca de 40% dos erros induzidos por humanos (desenvolvedores). *

**_Intuitivo :_** ótimo suporte ao editor. Conclusão em todos os lugares. Menos tempo de depuração.

**_Fácil :_** Projetado para ser fácil de usar e aprender. Menos tempo lendo documentos.

**_Curto :_** Minimiza a duplicação de código. Vários recursos de cada declaração de parâmetro. Menos erros.

**_Robusto :_** obtenha código pronto para produção. Com documentação interativa automática.

**_Baseado em padrões :_** Baseado em (e totalmente compatível com) os padrões abertos para APIs:OpenAPI
(anteriormente conhecido como Swagger) eEsquema JSON.

**_Integração de CORS :_** O FastAPI inclui facilidades para configurar o Compartilhamento de Recursos entre 
Origens Cruzadas (CORS), que é essencial quando você deseja que seu back-end aceite solicitações de diferentes 
domínios.

# Alguns trechos de códigos
Vou procurar explicar aqui alguns trechos de códigos dentro dos arquivos desta pasta, com as explicações que 
peguei com ChatGPT, do meu entendimento e pesquisas na internet
## from pydantic import BaseModel
**_Pydantic_ :** É uma biblioteca de validação de dados e análise de dados que é frequentemente usada em 
aplicativos 
Python, especialmente em frameworks como o [FastAPI](https://fastapi.tiangolo.com/). Ela ajuda a definir 
estruturas de dados com tipos de dados 
específicos e regras de validação.

**_BaseModel_ :** A classe BaseModel é uma parte fundamental do Pydantic. Ela permite que você defina modelos 
de dados com base em suas necessidades. Um modelo BaseModel é uma classe que herda da classe pydantic.
BaseModel. Você pode definir campos com tipos de dados específicos e adicionar validações aos campos.

### A classe BaseModel fornece funcionalidades poderosas, como:

**_Validação automática de tipos_ :** Ela garantirá que os valores atribuídos aos campos correspondam aos tipos especificados.

**_Validação personalizada_ :** Você pode adicionar métodos para fazer validações mais complexas nos campos.

**_Geração de esquemas JSON_ :** Você pode usar model.schema() para gerar um esquema JSON a partir do seu modelo, útil para documentação de API.

**_Transformação de dados_ :** A classe BaseModel permite que você faça transformações de dados ao definir campos com propriedades como alias, default, pre e post.