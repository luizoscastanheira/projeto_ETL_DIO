#  Projeto ETL DIO
## BootCamp Santader  - DIO

Este projeto se destina exemplificar um  pipeline de dados onde se demonstra uma sequência padrão de Extração, Transformação  e Carregamento de  dados, conforme solicitado no desafio de projeto.

O programa será carregado ao se executar o arquivo pipeline.py

### Etapa 1 - Extração
Nesta etapa o projeto Extrai  os dados à partir de um arquivo em  formato csv representando uma de base clientes (1.000 registros).

### Etapa 2 - Transformação
Nesta etapa, os dados extraidos  são "transformados", recebendo  a seguintes  alterações:

- Os cabeçalhos de coluna extraidos do arquivo.csv original são aterados;
- É acrescentada uma  coluna de nome "Atualizado"  onde o valor True será para clientes do  Brazil e False para clientes de outros paises;
- O conteúdo dos campos Cliente(antigo campo nome) e Pais(antigo campo country) são transformados para caixa alta.

### Etapa 3 - Carregamento
Nesta  etapa, os dados já transformados são transferidos para dois arquivos criados pela aplicação:
- Um arquivo formato (transformado.csv);
- Um arquivo formato (transformado.xlsx).

## Observações
- Este projeto é simples, objetiva  tão somente exemplificar uma sequência de ETL sem entrar no assunto em grande profundidade;
- Não  esqueça de habilitar o ambiente virtual no projeto, isso evita muitos possíveis problemas com suas bibliotecas globais;
- Os requistos de bibliotecas  estão listados no arquivo requirements.txt e podem se instalados pelo seguinte comando: pip install -r requeriments.txt
