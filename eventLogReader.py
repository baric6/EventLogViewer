import pandas as pd
import json

class EventStorage:
    def __init__(self, df):
        self.df = df

    def getDF(self):
        print(self.df)

    def getHead(self):
        print(self.df.head())

    def exportToJson(self):
        json_list = df.to_dict(orient='records')
         # Extract the log_string from the DataFrame
        log_string = self.df['Task Category'].iloc[0]
        
        # Convert the log string to a dictionary
        log_dict = {"Task Category": log_string.split("\r\n\r\n")}
        
        # Add the log dictionary to the JSON list
        json_list.append(log_dict)
        
        with open('export.json', 'w') as f:
            f.write(json.dumps(json_list, indent=2))

def readEventLogs():    
    # Read CSV files from List
    df = pd.concat(map(pd.read_csv, ['eventLogs/TLSecurityEvents.csv']))
    return df

if __name__ == "__main__":
    df = readEventLogs()
    eventStorage = EventStorage(df)
    eventStorage.getDF()
    eventStorage.getHead()
    eventStorage.getColumnByName("Event ID")
    eventStorage.exportToJson()
