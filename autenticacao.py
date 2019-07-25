#!/usr/bin/python3
import json,os

file_name='.credenciais.json'

full_file=os.path.abspath(os.path.join(file_name))

def credencial():
	with open(full_file) as jsonfile:
		parsed = json.load(jsonfile)
		servidor = parsed['conexao']['url']
		usuario = parsed['conexao']['user']
		senha = parsed['conexao']['password']
	return servidor,usuario,senha

