import json, os;
try:
	for event in json.loads(open("événements.json", "r").read())[os.popen("date").read().split()[2]][f'{int(os.popen("date").read().split()[1]) + 0}']: print(event);
except:
	print("il n y a aucun événement mondial aujourd'hui :/") 
