# -*- coding: utf-8 -*-
from pyzabbix import ZabbixAPI
import pyzabbix
import csv
from autenticacao import credencial

zabbix_server,usuario,senha = credencial()

zapi = ZabbixAPI(zabbix_server)
zapi.login(user=usuario, password=senha)

arq = csv.reader(open('hosts.csv'))
f = csv.reader(open('hosts.csv'), delimiter=',')

for [hostname,ip] in f:
    try:
        hostcriado = zapi.host.create(
            host= hostname,
            status= 1,
            interfaces=[{
            "type": 1,
            "main": "1",
            "useip": 1,
            "ip": ip,
            "dns": "",
            "port": 10050
            }],
            groups=[{
            "groupid": 2
            }],
            templates=[{
            "templateid": 10001
            }]
            )
        print("O host",hostname,"criado com sucesso")
    except pyzabbix.ZabbixAPIException as e:
        print(e)

