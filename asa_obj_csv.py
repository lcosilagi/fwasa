#!/usr/bin/env python3

'''
ASA_OBJ_CSV v0.1
------------------------------------------------------------------------------------------------------------------------

Este script lê o arquivo de entrada especificado pelo parametro -i contendo as informações de objetos
e gera 3 arquivos com as informações de objetos em formato .CSV: hosts.csv, subnets.csv, ranges.csv, 
que podem ser importados para o Excel.

Por padrão, esse script também exibe na tela as informações de objetos e número total de objetos processados.

Se não houver objetos no arquivo, nenhuma informação de objeto é exibida e o total de objetos será mostrado como zero. 


OBS:
------------------------------------------------------------------------------------------------------------------------
- Nesta versão, o script gera um arquivo csv para hosts, outro para subnets e outro para ranges contendo o 
nome do objeto, o endereço IP de host, subnet ou range e se houver, a descrição.

- Se não houver informações no arquivo de entrada, um arquivo contendo somente os títulos de cabeçalho são
gerados e podem ser descartados.

- Estes arquivos csv podem ser abertos em excel para fácil visualizacao.
------------------------------------------------------------------------------------------------------------------------


------------------------
Desenvolvido por : Lupas
------------------------

------------------------
REQUISITOS
------------------------
Python 3.8.10
'''


# Importamos as bibliotecas de funcoes necessarias
import re, argparse


# Criamos o argument parser, responsável por armazenar os parametros da linha de comando
parser = argparse.ArgumentParser(usage = './%(prog)s -i [arquivo.txt]',
                                description = 'Processa arquivo de configuração do ASA contendo informações objetos e gera arquivos csv com objetos de host, subnet e range',
                                epilog = 'Ex: ./%(prog)s -i objects.txt')


parser.add_argument('-i', '--input',  dest = 'i', required = True, help = 'especifique o nome do arquivo em formato texto, que contêm as informações de objetos do Firewall ASA.  Ex: objects.txt. O arquivos objects.txt tem que estar localizado no mesmo diretório onde está sendo executado este script.  Gera arquivo .csv (hosts.csv, subnet.csv ou ranges.csv)')
parser.add_argument('-v', action= 'version', version = '%(prog)s 0.1', help = 'Exibe a versão do script')
arg = parser.parse_args()


# Armazenamos o valor dos argumentos passados em linha de comando em variaveis
arqi = arg.i
arqh = 'hosts.csv'
arqs = 'subnets.csv'
arqr = 'ranges.csv'


# -----------------------------------------------------------------------------------------
# Padrão regex para extrair nome de objeto, ip e descrição (hosts)                          
p0 = re.compile(r'object\snetwork\s(.+)\n\s?host\s(.+)(?:\n\s?description\s(.+))?')

# Padrão regex para extrair nome de objeto, ip e descrição (subnets)
p1 = re.compile(r'object\snetwork\s(.+)\n\s?subnet\s(.+)(?:\n\s?description\s(.+))?')

# Padrão regex para extrair nome de objeto, ip e descrição (subnets)
p2 = re.compile(r'object\snetwork\s(.+)\n\s?range\s(.+)(?:\n\s?description\s(.+))?')
#-----------------------------------------------------------------------------------------


# Armazenamos a contagem do número total de objetos encontrados
hcont = scont = rcont = 0


# Processamos o conteúdo dos arquivos de entrada, geramos o arquivo .csv e exbimos as informações em tela
with open(arqi,'r') as fi, open(arqh, 'w') as fh:
    obj_hosts = fi.read()

    # Grava o cabeçalho do arquivo csv de hosts
    fh.write('sep = ,\n')
    fh.write('NOME,IP, DESCRIÇÂO\n')
    print('-'*20)
    print(f'   OBJETOS HOST')
    print('-'*20)

    filtro = p0.finditer(obj_hosts)

    for oh in filtro:
        if oh.group(1) and oh.group(2) and oh.group(3):
            
            print(f'{oh.group(1)},{oh.group(2)},{oh.group(3)}')
            fh.write(f'{oh.group(1)},{oh.group(2)},{oh.group(3)}\n')
        elif not oh.group(3):
            print(f'{oh.group(1)},{oh.group(2)}')
            fh.write(f'{oh.group(1)},{oh.group(2)}\n')
    
        hcont += 1


with open(arqi,'r') as fi, open(arqs, 'w') as fs:
    obj_subnets = fi.read()
        
    filtro = p1.finditer(obj_subnets)

    # Grava o cabeçalho do arquivo csv de subnet
    fs.write('sep = ,\n')
    fs.write('NOME,SUBNET,DESCRIÇÃO\n')
    print('\n')
    print('-'*20)
    print(f'   OBJETOS SUBNET')
    print('-'*20)

    for osub in filtro:
        if osub.group(1) and osub.group(2) and osub.group(3):
            print(f'{osub.group(1)},{osub.group(2)},{osub.group(3)}')
            fs.write(f'{osub.group(1)},{osub.group(2)},{osub.group(3)}\n')
        elif not osub.group(3):
            print(f'{osub.group(1)},{osub.group(2)}')
            fs.write(f'{osub.group(1)},{osub.group(2)}\n')

        scont += 1


with open(arqi,'r') as fi, open(arqr,'w') as fr:
    obj_ranges = fi.read()
        
    filtro = p2.finditer(obj_ranges)

    # Grava o cabeçalho do arquivo csv de range
    fr.write('sep = ,\n')
    fr.write('NOME,RANGE,DESCRIÇÃO\n')
    print('\n')
    print('-'*20)
    print(f'   OBJETOS RANGE')
    print('-'*20)

    for org in filtro:
        if org.group(1) and org.group(2) and org.group(3):
            print(f'{org.group(1)},{org.group(2)},{org.group(3)}')
            fr.write(f'{org.group(1)},{org.group(2)},{org.group(3)}\n')
        elif not org.group(3):
            print(f'{org.group(1)},{org.group(2)}')
            fr.write(f'{org.group(1)},{org.group(2)}\n')
            
        rcont += 1


# Imprimimos na tela o número total de objetos encontrados
print('\n\n\t '+'-'*55)
print(f'\t  Total de [{hcont}] objeto(s) host(s) processado(s).')
print(f'\t  Total de [{scont}] objeto(s) subnet(s) processado(s).')
print(f'\t  Total de [{rcont}] objeto(s) range(s) processado(s).')
print('\t '+'-'*55+'\n')