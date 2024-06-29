import datetime
import csv
import pandas as pd

def clean(file_path:str):
    current_date = datetime.datetime.now().date()
    lines_to_clean = []

    #Marking the line that need to be cleaned
    plans_file = open(file_path, 'r')
    csvfile = csv.DictReader(plans_file)
    for num, event in enumerate(csvfile):
        event_date = datetime.datetime.strptime(event['date'],"%Y-%m-%d").date()
        if(current_date >= event_date):
            lines_to_clean.append(num)
    
    #Deleting The Marked lines
    dataframe = pd.read_csv(file_path)
    dataframe = dataframe.drop(dataframe.index[lines_to_clean])
    dataframe.to_csv(file_path, index=False)
