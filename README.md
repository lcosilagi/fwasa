# INTRODUÇÃO
Script para filtrar objetos do FIREWALL ASA e gerar arquivos CSV com informações de objetos de rede que podem ser importados no `EXCEL` para fácil visualização.


## PARA CLONAR ESTE REPOSITÓRIO

`git clone git@github.com:lcosilagi/fwasa.git`


## ASA_OBJ_CSV v0.1
Este script lê o arquivo contendo as informações de objetos de rede especificados pelo parâmetro -i e filtra o conteudo
para extrair informações como nome, endereço IP ou endereço de subnet ou range e descrição quando disponível.

Como resultado, as informações extraídas são armazenadas nos arquivos:

`hosts.csv`   - informações de objetos de host em formato csv.

`subnets.csv` - informações de objetos de subnet em formato csv.

`ranges.csv`  - informações de objetos de range em formato csv.


Por padrão os objetos processados e total de objetos encontrados são exibidos na tela.  Caso não seja encontrado objetos,
não serão exibidas informações na tela e o total de objetos por tipo de objeto será apresentado com o total de 0.


## COMO OBTER AS INFORMAÇÔES DE OBJETOS DO FIREWALL ASA

* Rodar o comando `show run object` na `cli` do `ASA` (suportado até a versão 9).

* Copiar a saída do comando `show run object` para um arquivo e nomear como `objects.txt`, no entanto pode ser utilizado qualquer nome de arquivo de sua peferência.  A opcão -i permite especificar outro nome de arquivo, se você desejar.


## PROCEDIMENTO PARA UTILIZAR O SCRIPT

Para gerar os arquivos `hosts.csv`, `subnets.csv` e `ranges.csv` - executar:

    asa_obj_csv.py -i objects.txt

Para exibir a versão do script - executar:     

    asa_obj_csv.py -v

Para exbir o help - executar:

    asa_obj_csv .py -h


## COMO VERIFICAR O NÚMERO TOTAL DE OBJETOS

Para verificar o número total de objetos de host, no `Linux` utilize o comando `GREP`:

    grep -c 'host' objects.txt

Para verificar o número total de objetos de host, no `Windows` utilize a busca por regex do `notepad++`:
    `Padrão Regex:` object\snetwork\s.+\r\n\shost\s.+(\r\n\sdescription.+)?


Para verificar o número total de objetos de subnet, no `Linux` utilize o comando `GREP`:
    
    grep -c 'subnet' objects.txt

Para verificar o número total de objetos de subnet, no `Windows` utilize a busca por regex do `notepad++`:
    `Padrão Regex:` object\snetwork\s.+\r\n\ssubnet\s.+(\r\n\sdescription.+)?


Para verificar o número total de objetos de range, no `Linux` utilize o comando `GREP`:

    grep -c 'range' objects.txt

Para verificar o número total de objetos de range, no `Windows` utilize a busca por regex do `notepad++`:
    `Padrão Regex:` object\snetwork\s.+\r\n\srange\s.+(\r\n\sdescription.+)?


* Após o script rodar com sucesso, o arquivo CSV é gerado contendo as informações de nome de objeto, endereço IP do host, subnet ou range e descrição (quando houver este campo especificado no arquivo de entrada).


## DESENVOLVIMENTO
`Lupas`

## VERSÃO PYTHON
`Python 3.8.10`

## MÓDULOS
`re` `argparse`

## S.O.
`Linux` `Windows`