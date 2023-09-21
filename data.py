import gspread 
import pandas as pd 


def load_data(): 
    # Specify the URL of the publicly accessible Google Sheet
    sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRLTgxkwclFqHFN6qSfGfYhNgUyK4lyISq5nMyp43tLBl2ICiwbTnvPdfJyKypHe4K8fUhKLrzA7sSd/pub?gid=0&single=true&output=csv'

    df = pd.read_csv(sheet_url)

    return df 
