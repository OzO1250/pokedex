from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1DQVQnKuKEL6gwLF9q4cnzKSUrNP23w52J-BOAe0ZRZE'
RANGE_NAME = 'Sheet1!A2:R'
HEADER_RANGE = 'Sheet1!A1:R'

def verify_credentials():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service

def read_file():
    pokemon =[]
    service = verify_credentials()

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return pokemon
    else:
        for row in values:
            pokemon.append(row)
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s' % row)
        #print('%s' % pokemon)
        return pokemon

#Write the GSheet file with the new array of Pokemon, combination of the API call and the GSheet initial reading
def write_file(poke):
    pokemon = poke
    service = verify_credentials()

    #print(pokemon)

    # Call the Sheets API
    values = pokemon
    headers = [['ID','Pokémon Name','URL','Last Updated']]

    data = [
        {
            'range': HEADER_RANGE,
            'values': headers
        },
        {
            'range': RANGE_NAME,
            'values': values
        }
    ]

    body = {
        'valueInputOption': 'RAW',
        'data': data
    }

    result = service.spreadsheets().values().batchUpdate(
        spreadsheetId=SPREADSHEET_ID, body=body).execute()
    print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

if __name__ == '__main__':
    read_file()
    #write_file(test)