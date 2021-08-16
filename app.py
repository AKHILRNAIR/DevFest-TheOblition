from flask import Flask,render_template
from flask_mysqldb import MySQL
import pickle
from sklearn import svm
import pandas as pd

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = "devfest-the oblivionn"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')

def contractor2():
    cur = mysql.connection.cursor()


    cur.execute('''SELECT * FROM applications''')
    results1 = cur.fetchall()
    cur.execute('''SELECT * FROM contractors''')
    results2 = cur.fetchall()
    
    app = []
    price = []
    con = []
    rat = []
    exp = []
    name = []
    count = 0

    for x in results1:
        app.append(x['Application_ID'])
        price.append(x['Price'])
        con.append(x['Contractor_ID'])
        count +=1


    for x in results2:
        if(x['Contractor_ID'] in con):
            rat.append(x['Rating'])
            exp.append(x['Experience'])
            name.append(x['Name'])

    if (count == 10):
        dataset = {'Application_ID': app,'Contractor_ID': con,'Price' : price,'Rating': rat,'Experience':exp}

        testset = pd.DataFrame(dataset)
        #print(testset)
        df = testset[testset.columns[3:5]]
        #print(df)
        con_new = []
        app_new = []
        price_new = []
        filename = 'ML_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(df)
        print (result)
        for i in range(10):
            if(result[i] == 1):
                con_new.append(con[i])
                app_new.append(app[i])
                price_new.append(price[i])
        price_new.sort()
        print(price_new)
        for x in results1:
            if(x['Price']==price_new[0]):
                con_sel = x['Contractor_ID']
                app_sel = x['Application_ID']
                #name_sel = x['Name']
    
        #print(con_sel)
        return render_template('apptemp.html',name = con_sel)
        #return "done"
    else:
        return render_template('notenough.html')

    


    


        

        
    
    