import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
GOOGLE_SHEETS_CREDENTIALS_FILE = 'credenciais-google.json'
SPREADSHEET_NAME = 'Leads EstBank'

RD_ACCESS_TOKEN = 'seu_token_de_acesso_aqui'

RD_API_URL = 'https://api.rd.services/platform/conversions'

credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS_FILE, SCOPE)
client = gspread.authorize(credentials)
sheet = client.open(SPREADSHEET_NAME).sheet1

leads = sheet.get_all_records()

for lead in leads:
    payload = {
        "event_type": "CONVERSION",
        "event_family": "CDP",
        "payload": {
            "name": lead.get('Nome'),
            "email": lead.get('Email'),
            "personal_phone": lead.get('Telefone'),
            "cf_empresa": "EstBank"
        }
    }

    headers = {
        "Authorization": f"Bearer {RD_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(RD_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200 or response.status_code == 201:
        print(f"Lead {lead.get('Nome')} enviado com sucesso!")
    else:
        print(f"Erro ao enviar o lead {lead.get('Nome')}: {response.text}")
