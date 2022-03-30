#!/usr/bin/env python
# coding: utf-8

# In[1]:


#テキスト量産プログラム
import csv
import pandas as pd
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('./config/config.ini',encoding='utf-8')

var = config_ini.getint('DEFAULT','Columns')
textlist_url = config_ini.get('DEFAULT','TEXT_LIST')
template_url = config_ini.get('DEFAULT','TEXT_TEMP')
output_url = config_ini.get('DEFAULT','OUTPUT_FILE')

data_rows = []
data = []
text_data = []
i = 0
#テキストconfigを読み込み

with open(textlist_url, newline='', encoding='UTF-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader :
        data_rows.append(row)
        
        #Pythonにテキストデータの読み込み
        TEXT_FILE = open(template_url, 'r', encoding='UTF-8')
        txt = TEXT_FILE.read()
        TEXT_FILE.close()
        
        #データの読み取りとテキスト変換
        try :
            for n in range(var):
                listdata = data_rows[i][n]
                data.append(listdata)
        except IndexError :
            print("error")
            
        #テキストフォーマット処理
        try :
            TEXT = txt.format(*data)
        except IndexError :
            print("error")
        except ValueError :
            print("error")
        #テキストデータをリストに変換
        text_data.append(TEXT)
        #リストの初期化
        data = []
        i += 1
        
#テキストをCSVで出力
df = pd.DataFrame(text_data)
try :
    df.to_csv(output_url,index = False, encoding='utf_8_sig')
except PermissionError :
            print("error_No.04")

print('done')


# In[ ]:




