import re, fnmatch, os
import requests
import os.path
from pandas import DataFrame, read_csv
import datetime
from spyre import server
import pandas as pd
import json
class Chronos(server.App):
    title = "ChronoIndex"
    inputs = [{     
                    "type":'dropdown',
                    "label": 'Type',
                    "options" : [ {"label": "VHI", "value":"VHI"},
                                  {"label": "TCI", "value":"TCI"},
                                  {"label": "VCI", "value":"VCI"}],
                    "key": 'ticker1',
                    "action_id": "update_data"
               },{     
                    "type":'dropdown',
                    "label": 'Type2',
                    "options" : [ {"label": "VHI", "value":"VHI"},
                                  {"label": "TCI", "value":"TCI"},
                                  {"label": "VCI", "value":"VCI"}],
                    "key": 'ticker2',
                    "action_id": "update_data"
               },{
                    "type":'dropdown',
                    "label": 'Location',
                    "options" : [ {"label": "1", "value":"1"},
                                  {"label": "2", "value":"2"},
                                  {"label": "3", "value":"3"},
                                  {"label": "4", "value":"4"},
                                  {"label": "5", "value":"5"},
                                  {"label": "6", "value":"6"},
                                  {"label": "7", "value":"7"},
                                  {"label": "8", "value":"8"},
                                  {"label": "9", "value":"9"},
                                  {"label": "10", "value":"10"},
                                  {"label": "11", "value":"11"},
                                  {"label": "12", "value":"12"},
                                  {"label": "13", "value":"13"},
                                  {"label": "14", "value":"14"}]
 
                    "key": 'ticker',
                    "action_id": "update_data"},{
                    "input_type":"text",
                    "variable_name":"from",
                    "label":"from",
                    "value":1985,
                    "action_id":"update_data"},{
                    "input_type":"text",
                    "variable_name":"to",
                    "label":"to",
                    "value":2017,
                    "action_id":"update_data"}]
    controls = [{    "type" : "hidden",
                    "id" : "update_data"}]
    tabs = ["Plot", "Table"]

    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]
    def getData(self, params):
        ticker = params['ticker']
        ticker1 = params['ticker1']
        Tfrom = params['from']
        Tto = params['to']
        for file in os.listdir('.'):
                if fnmatch.fnmatch(file, 'vhi_id_'+str(ticker)+'*.csv'):
                        df = pd.read_csv(file,index_col=False, header=0)
                        df = DataFrame(df[ticker1][(df['year']>=int(Tfrom))&(df['year']<=int(Tto))])
        return df
    def getPlot(self, params):
        df = self.getData(params)
        plt_obj = df.plot()
        fig = plt_obj.get_figure()
        return fig
app = Chronos()
app.launch(port=9083)
