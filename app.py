from flask import Flask,jsonify,request
import pandas as pd
from datetime import datetime, timedelta, date

app = Flask(__name__)

date = datetime.now()
dict = {"IFSC_code":[],"date":[]}


@app.route('/<key>')

#function to search IFSC code
def search(key):
    #null check
    if key is None:
        return 404
    else:    
        print(key)
        dict["date"].append(str(date))
        dict["IFSC_code"].append(key)
        IFSC = pd.ExcelFile('./RBI-IFSC-Data.xlsx')
        IFSC1 = pd.read_excel(IFSC, 'Sheet1')
        IFSC2 = pd.read_excel(IFSC, 'Pivot Table_Sheet1_1')
        IFSC_data = IFSC1.to_dict('records')
        l=len(IFSC_data)
        df = pd.DataFrame(IFSC_data)
        #print(df.head())
        data_dict=df.to_dict('records')
        #print(data_dict)
        result=df.loc[df['IFSC'] == key].to_dict('records')
        return jsonify(result) 

@app.route('/statistics')    
def statistics():  
     return jsonify(dict)


@app.route('/leaderboard')    
def leaderBoard():
    #read request parameters
    sortorder = request.args.get('sortorder')
    fetchcount = request.args.get('fetchcount')
    print(sortorder)
    print(fetchcount)
    IFSC = pd.ExcelFile('./RBI-IFSC-Data.xlsx') 
    IFSC2 = pd.read_excel(IFSC, 'Pivot Table_Sheet1_1')
    bank_leaderBoard = IFSC2.to_dict('records')
    df = pd.DataFrame(bank_leaderBoard)
    data_dict=df.to_dict('records')

    if sortorder is None and fetchcount is None:
        print(df.sort_values("Count - BANK", ascending=False).head(10))
        result=df.sort_values("Count - BANK", ascending=False).head(10).to_dict('records')
        return jsonify(result)
    if sortorder is not None and fetchcount is not None:
        if sortorder=="ASC":
            print(df.sort_values("Count - BANK").head(int(fetchcount)))
            result=df.sort_values("Count - BANK").head(int(fetchcount)).to_dict('records')
            return jsonify(result)
        if sortorder=="DESC":
            print(df.sort_values("Count - BANK", ascending=False).head(int(fetchcount)))
            result=df.sort_values("Count - BANK", ascending=False).head(int(fetchcount)).to_dict('records')
            return jsonify(result)
        else:
            return "404 invalid request"

    else:
        return "404 invalid request"
         