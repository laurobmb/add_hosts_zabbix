# -*- coding: utf-8 -*-
from zabbix_api import ZabbixAPI
from autenticacao import credencial

zabbix_server,usuario,senha = credencial()

try:
	conexao = ZabbixAPI(server = zabbix_server, log_level=0)
	conexao.login(usuario,senha)
except:
	print('Erro na conexcao')
	exit(0)

hosts_zabbix = conexao.host.get({
	"output": [ 
		"name", 
		"hostid"
		],
	"sortfield": "name"
	})

f=open('hosts.csv','w')

for i in hosts_zabbix:
	hostid = i['hostid']
	hostname = i['name']
	interface = conexao.hostinterface.get({ "output": "extend", "hostids": hostid })
	ipaddress = interface[0]['ip']
	output=hostname+","+ipaddress
	print(output)
	f.write(output)
	f.write('\n')
f.close()


