# ExcelSheet

ExcelSheet is a Facebook Messenger Chatbot that tracks user spending.

## How it works

1. The [Facebook Messenger platform](https://developers.facebook.com/docs/messenger-platform/) handles incoming requests to the chatbot via
   messenger.
2. The request is sent to this API hosted on [Google Cloud App Engine](https://cloud.google.com/appengine?hl=en)
3. The application writes spending data to a centralized Google Sheet using the [Google Sheets API](https://developers.google.com/sheets/api/guides/concepts).

<img src="/excelsheet_demo.jpg" width="400"/>

Currently, spending can be tracked in one of 11 categories and spending messages need to follow a rigid structure. Using this collected spending data, the end goal of this project is to develop a language model that automatically categorizes spending based on descriptions. Another future goal is to provide descriptive and prescriptive analysis within chatbot conversation.

**Note:** This app is currently private/in-beta on Facebook Messenger and not publicly availablt.

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
