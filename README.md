# ExcelSheet

Financial tracking made easy.

## Running with ngrok

1. Run the `app.py` Flask API listening on `localhost:8080`
2. Run ngrok with the permanent domain
   `ngrok http 8080 --domain heroic-urchin-assured.ngrok-free.app`

## Environment variables

Create a `.env` file with the following:

```
VERIFY_TOKEN=<facebook_verify_token>
PAGE_ACCESS_TOKEN=<facebook_page_access_token>
FACEBOOK_API_URL=https://graph.facebook.com/v18.0/me/messages
CREDENTIALS_JSON=<google_sheets_credentials.json>
SHEET_ID=<google_sheet_id
```
