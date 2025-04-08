# 📊 Google Sheets → RD Station Automation

Este projeto tem como objetivo automatizar o envio de leads da planilha do **Google Sheets** diretamente para a **plataforma de CRM RD Station**, facilitando o fluxo de captação e registro de contatos.

---

## 🚀 Funcionalidades

- Conecta-se a uma planilha do Google Sheets contendo os dados dos leads;
- Envia automaticamente cada lead para a RD Station via API;
- Permite personalizar os campos enviados, como nome, e-mail, telefone, etc.;
- Ideal para fluxos de trabalho automatizados e integração com formulários externos.

---

## 🛠️ Pré-requisitos

- Conta no [Google Cloud Console](https://console.cloud.google.com/)
- Conta na [RD Station](https://www.rdstation.com/)
- Python 3.7 ou superior

---

## 📦 Instalação de dependências

bash

pip install gspread oauth2client requests

---

### 🔐 Configurações Necessárias
Google Sheets
Crie uma planilha com as colunas: Nome, Email, Telefone, etc.

Ative a Google Sheets API no Google Cloud.

Baixe o arquivo credenciais-google.json.

Compartilhe a planilha com o e-mail da conta de serviço (informado nas credenciais).

RD Station
Gere um Access Token no painel da RD Station.

Consulte a documentação oficial da RD Station.

---

### 🧠 Como Usar
Edite o arquivo main.py e insira:

O nome da sua planilha (SPREADSHEET_NAME);

O caminho do seu arquivo credenciais-google.json;

O token de acesso da RD Station (RD_ACCESS_TOKEN).

Execute o script:

bash

Copiar

Editar

python main.py

Os leads serão enviados para a RD Station. O terminal exibirá logs de sucesso ou erro para cada lead.

---

### 📌 Observações
Certifique-se de que os dados na planilha estão corretamente formatados.

O script não impede duplicações (pode ser ajustado conforme necessidade).

Pode ser agendado com cron, Task Scheduler ou outro agendador para execução periódica.
