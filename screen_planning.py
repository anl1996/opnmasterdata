import pandas as pd
import glob
import dash
import numpy as np
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
import plotly.figure_factory as ff
filenames = glob.glob("/*.xlsm")
allExcelFiles = glob.glob("*.xlsm")
campaign_type = "LAUNCH","ONGOING"
db_TV = pd.concat(pd.read_excel(excelFile,sheet_name="TV_Database") for excelFile in allExcelFiles)
db_FB = pd.concat(pd.read_excel(excelFile,sheet_name="FB_Database") for excelFile in allExcelFiles)
db_YT = pd.concat(pd.read_excel(excelFile,sheet_name="YT_Database") for excelFile in allExcelFiles)
db_Other = pd.concat(pd.read_excel(excelFile,sheet_name="Other_Database") for excelFile in allExcelFiles)
data = pd.concat(pd.read_excel(excelFile,sheet_name="data") for excelFile in allExcelFiles)
view = pd.concat(pd.read_excel(excelFile,sheet_name="view") for excelFile in allExcelFiles)
frequency = pd.concat(pd.read_excel(excelFile,sheet_name="Unlimited") for excelFile in allExcelFiles)
figures = pd.concat(pd.read_excel(excelFile,sheet_name="Figures") for excelFile in allExcelFiles)

figures=figures.drop(columns=["Unnamed: 0","Unnamed: 9"],index=0)
figures.columns=figures.values[0]
figures.drop(index=1,inplace=True)
figures.reset_index(drop="index",inplace=True)
BTAQ4=0
BTAFY=0
CTAFY=0
BSAQ4=0
BSAFY=0
CSAFY=0
"""
BTAQ4=figures["Brand TOM Awareness Q4\'21"][0]
BTAFY=figures["Brand TOM Awareness FY\'21"][0]
CTAFY=figures["Category TOM Awareness FY\'21"][0]
BSAQ4=figures["Brand Spontaneous Awareness Q4\'21"][0]
BSAFY=figures["Brand Spontaneous Awareness FY\'21"][0]
CSAFY=figures["Category Spontaneous Awareness FY\'21"][0]
"""
aylar="JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"
secilen_ay={"JANUARY":0,"FEBRUARY":1,"MARCH":2,"APRIL":3,"MAY":4,"JUNE":5,"JULY":6,"AUGUST":7,"SEPTEMBER":8,"OCTOBER":9,"NOVEMBER":10,"DECEMBER":11}

#target_audience_names="12-24 C1C2","12-34 Years Old","15-34 ABC1","15-24 ABC1C2","15-24","20-44 ABC1C2","HKF 25-44 ABC1C2 ","15-34 ABC1C2","25-34 ABC1","15-34 Years Old","15-44 ABC1","20+","12-34 ABC1C2","12-24 ABC1C2","25+ ABC1","25-44 ABC1"
reach_names="Reach@1+","Reach@2+","Reach@3+","Reach@4+"
campaign_type = "LAUNCH","ONGOING"

target_audience_names="12-34 Years Old","15-24","15-34 ABC1","15-34 ABC1C2","20+","12-34 ABC1C2","20-44 ABC1C2","12-24 C1C2","12-24 ABC1C2","HKF 25-44 ABC1C2 ","15-34 Years Old","25-34 ABC1","15-44 ABC1","25-44 ABC1","25+ ABC1","15-24 ABC1C2"
target_audience_names_FB_YT_OTHER='25-34 ABC1','20-44 ABC1C2','20+','HKF 25-44 ABC1C2 ','12-34 Years Old','12-24 ABC1C2','12-24 C1C2','12-34 ABC1C2','15-24','15-34 ABC1C2','15-24 ABC1C2','15-34 Years Old','25+ ABC1','15-34 ABC1','15-44 ABC1','25-44 ABC1'
#--------------------------------------------------------------------------------------------------

db_TV_12_34_years_old=db_TV[[10,'PT%:',0,'Ay',',,','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13']][4:15]
db_TV_15_24_years_old=db_TV[["15-24","Unnamed: 63","Unnamed: 64","Unnamed: 65","Unnamed: 66","Unnamed: 67","Unnamed: 68","Unnamed: 69","Unnamed: 70","Unnamed: 71","Unnamed: 72","Unnamed: 73"]][4:15]
db_TV_15_34_ABC1=db_TV[["15-34 ABC1","Unnamed: 123","Unnamed: 124","Unnamed: 125","Unnamed: 126","Unnamed: 127","Unnamed: 128","Unnamed: 129","Unnamed: 130","Unnamed: 131","Unnamed: 132","Unnamed: 133"]][4:15]
db_TV_15_34_ABC1C2=db_TV[["15-34 ABC1C2","Unnamed: 183","Unnamed: 184","Unnamed: 185","Unnamed: 186","Unnamed: 187","Unnamed: 188","Unnamed: 189","Unnamed: 190","Unnamed: 191","Unnamed: 192","Unnamed: 193"]][4:15]
db_TV_20_plus=db_TV[["20+","Unnamed: 243","Unnamed: 244","Unnamed: 245","Unnamed: 246","Unnamed: 247","Unnamed: 248","Unnamed: 249","Unnamed: 250","Unnamed: 251","Unnamed: 252","Unnamed: 253"]][4:15]
db_TV_12_34_ABC1C2=db_TV[["12-34 ABC1C2","Unnamed: 303","Unnamed: 304","Unnamed: 305","Unnamed: 306","Unnamed: 307","Unnamed: 308","Unnamed: 309","Unnamed: 310","Unnamed: 311","Unnamed: 312","Unnamed: 313"]][4:15]
db_TV_20_44_ABC1C2=db_TV[["20-44 ABC1C2","Unnamed: 363","Unnamed: 364","Unnamed: 365","Unnamed: 366","Unnamed: 367","Unnamed: 368","Unnamed: 369","Unnamed: 370","Unnamed: 371","Unnamed: 372","Unnamed: 373"]][4:15]
db_TV_12_24_C1C2=db_TV[["12-24 C1C2","Unnamed: 423","Unnamed: 424","Unnamed: 425","Unnamed: 426","Unnamed: 427","Unnamed: 428","Unnamed: 429","Unnamed: 430","Unnamed: 431","Unnamed: 432","Unnamed: 433"]][4:15]
db_TV_12_24_ABC1C2=db_TV[["12-24 ABC1C2","Unnamed: 483","Unnamed: 484","Unnamed: 485","Unnamed: 486","Unnamed: 487","Unnamed: 488","Unnamed: 489","Unnamed: 490","Unnamed: 491","Unnamed: 492","Unnamed: 493"]][4:15]
db_TV_HKF_25_44_ABC1C2=db_TV[["HKF 25-44 ABC1C2 ","Unnamed: 543","Unnamed: 544","Unnamed: 545","Unnamed: 546","Unnamed: 547","Unnamed: 548","Unnamed: 549","Unnamed: 550","Unnamed: 551","Unnamed: 552","Unnamed: 553"]][4:15]
db_TV_15_34_years_old=db_TV[["15-34 Years Old","Unnamed: 603","Unnamed: 604","Unnamed: 605","Unnamed: 606","Unnamed: 607","Unnamed: 608","Unnamed: 609","Unnamed: 610","Unnamed: 611","Unnamed: 612","Unnamed: 613"]][4:15]
db_TV_25_34_ABC1=db_TV[["25-34 ABC1","Unnamed: 663","Unnamed: 664","Unnamed: 665","Unnamed: 666","Unnamed: 667","Unnamed: 668","Unnamed: 669","Unnamed: 670","Unnamed: 671","Unnamed: 672","Unnamed: 673"]][4:15]
db_TV_15_44_ABC1=db_TV[["15-44 ABC1","Unnamed: 723","Unnamed: 724","Unnamed: 725","Unnamed: 726","Unnamed: 727","Unnamed: 728","Unnamed: 729","Unnamed: 730","Unnamed: 731","Unnamed: 732","Unnamed: 733"]][4:15]
db_TV_25_44_ABC1=db_TV[["25-44 ABC1","Unnamed: 783","Unnamed: 784","Unnamed: 785","Unnamed: 786","Unnamed: 787","Unnamed: 788","Unnamed: 789","Unnamed: 790","Unnamed: 791","Unnamed: 792","Unnamed: 793"]][4:15]
db_TV_25_plus_ABC1=db_TV[["25+ ABC1","Unnamed: 843","Unnamed: 844","Unnamed: 845","Unnamed: 846","Unnamed: 847","Unnamed: 848","Unnamed: 849","Unnamed: 850","Unnamed: 851","Unnamed: 852","Unnamed: 853"]][4:15]
db_TV_15_24_ABC1C2=db_TV[["15-24 ABC1C2","Unnamed: 903","Unnamed: 904","Unnamed: 905","Unnamed: 906","Unnamed: 907","Unnamed: 908","Unnamed: 909","Unnamed: 910","Unnamed: 911","Unnamed: 912","Unnamed: 913"]][4:15]

#-----------------------------------------------------------------------------------------------


db_TV_12_34_years_old_reachs=db_TV.loc[:,10:'Unnamed: 61'][19:]
db_TV_15_24_years_old_reachs=db_TV.loc[:,"15-24":"Unnamed: 121"][19:]
db_TV_15_34_ABC1_reachs=db_TV.loc[:,"15-34 ABC1":"Unnamed: 181"][19:]
db_TV_15_34_ABC1C2_reachs=db_TV.loc[:,"15-34 ABC1C2":"Unnamed: 241"][19:]
db_TV_20_plus_reachs=db_TV.loc[:,"20+":"Unnamed: 301"][19:]
db_TV_12_34_ABC1C2_reachs=db_TV.loc[:,"12-34 ABC1C2":"Unnamed: 361"][19:]
db_TV_20_44_ABC1C2_reachs=db_TV.loc[:,"20-44 ABC1C2":"Unnamed: 421"][19:]
db_TV_12_24_C1C2_reachs=db_TV.loc[:,"12-24 C1C2":"Unnamed: 481"][19:]
db_TV_12_24_ABC1C2_reachs=db_TV.loc[:,"12-24 ABC1C2":"Unnamed: 541"][19:]
db_TV_HKF_25_44_ABC1C2_reachs=db_TV.loc[:,"HKF 25-44 ABC1C2 ":"Unnamed: 601"][19:]
db_TV_15_34_years_old_reachs=db_TV.loc[:,"15-34 Years Old":"Unnamed: 661"][19:]
db_TV_25_34_ABC1_reachs=db_TV.loc[:,"25-34 ABC1":"Unnamed: 721"][19:]
db_TV_15_44_ABC1_reachs=db_TV.loc[:,"15-44 ABC1":"Unnamed: 781"][19:]
db_TV_25_44_ABC1_reachs=db_TV.loc[:,"25-44 ABC1":"Unnamed: 841"][19:]
db_TV_25_plus_ABC1_reachs=db_TV.loc[:,"25+ ABC1":"Unnamed: 901"][19:]
db_TV_15_24_ABC1C2_reachs=db_TV.loc[:,"15-24 ABC1C2":"Unnamed: 961"][19:]

#--------------------------------------------------------------------------------------------------
db_FB_25_34_ABC1_reachs=db_FB.loc[:,"25-34 ABC1":'Unnamed: 4'][3:]
db_FB_20_44_ABC1C2_reachs=db_FB.loc[:,"20-44 ABC1C2":'Unnamed: 10'][3:]
db_FB_20_plus_reachs=db_FB.loc[:,"20+":'Unnamed: 16'][3:]
db_FB_HKF_25_44_ABC1C2_reachs=db_FB.loc[:,"HKF 25-44 ABC1C2 ":'Unnamed: 22'][3:]
db_FB_12_34_years_old_reachs=db_FB.loc[:,"12-34 Years Old":'Unnamed: 28'][3:]
db_FB_12_24_ABC1C2_reachs=db_FB.loc[:,"12-24 ABC1C2":'Unnamed: 34'][3:]
db_FB_12_24_C1C2_reachs=db_FB.loc[:,"12-24 C1C2":'Unnamed: 40'][3:]
db_FB_12_34_ABC1C2_reachs=db_FB.loc[:,"12-34 ABC1C2":'Unnamed: 46'][3:]
db_FB_15_24_reachs=db_FB.loc[:,"15-24":'Unnamed: 52'][3:]
db_FB_15_34_ABC1C2_reachs=db_FB.loc[:,"15-34 ABC1C2":'Unnamed: 58'][3:]
db_FB_15_24_ABC1C2_reachs=db_FB.loc[:,"15-24 ABC1C2":'Unnamed: 64'][3:]
db_FB_15_34_years_old_reachs=db_FB.loc[:,"15-34 Years Old":'Unnamed: 70'][3:]
db_FB_25_plus_ABC1_reachs=db_FB.loc[:,"25+ ABC1":'Unnamed: 76'][3:]
db_FB_15_34_ABC1_reachs=db_FB.loc[:,"15-34 ABC1":'Unnamed: 82'][3:]
db_FB_15_44_ABC1_reachs=db_FB.loc[:,"15-44 ABC1":'Unnamed: 88'][3:]
db_FB_25_44_ABC1_reachs=db_FB.loc[:,"25-44 ABC1":'Unnamed: 94'][3:]

#--------------------------------------------------------------------------------------------------
db_YT_25_34_ABC1_reachs=db_YT.loc[:,"25-34 ABC1":'Unnamed: 4'][3:]
db_YT_20_44_ABC1C2_reachs=db_YT.loc[:,"20-44 ABC1C2":'Unnamed: 10'][3:]
db_YT_20_plus_reachs=db_YT.loc[:,"20+":'Unnamed: 16'][3:]
db_YT_HKF_25_44_ABC1C2_reachs=db_YT.loc[:,"HKF 25-44 ABC1C2 ":'Unnamed: 22'][3:]
db_YT_12_34_years_old_reachs=db_YT.loc[:,"12-34 Years Old":'Unnamed: 28'][3:]
db_YT_12_24_ABC1C2_reachs=db_YT.loc[:,"12-24 ABC1C2":'Unnamed: 34'][3:]
db_YT_12_24_C1C2_reachs=db_YT.loc[:,"12-24 C1C2":'Unnamed: 40'][3:]
db_YT_12_34_ABC1C2_reachs=db_YT.loc[:,"12-34 ABC1C2":'Unnamed: 46'][3:]
db_YT_15_24_reachs=db_YT.loc[:,"15-24":'Unnamed: 52'][3:]
db_YT_15_34_ABC1C2_reachs=db_YT.loc[:,"15-34 ABC1C2":'Unnamed: 58'][3:]
db_YT_15_24_ABC1C2_reachs=db_YT.loc[:,"15-24 ABC1C2":'Unnamed: 64'][3:]
db_YT_15_34_years_old_reachs=db_YT.loc[:,"15-34 Years Old":'Unnamed: 70'][3:]
db_YT_25_plus_ABC1_reachs=db_YT.loc[:,"25+ ABC1":'Unnamed: 76'][3:]
db_YT_15_34_ABC1_reachs=db_YT.loc[:,"15-34 ABC1":'Unnamed: 82'][3:]
db_YT_15_44_ABC1_reachs=db_YT.loc[:,"15-44 ABC1":'Unnamed: 88'][3:]
db_YT_25_44_ABC1_reachs=db_YT.loc[:,"25-44 ABC1":'Unnamed: 94'][3:]

#---------------------------------------------------------------------------------------------------
a=[]
for i in range(len(target_audience_names)):
    for j in range(len(reach_names)):
        for z in range(len(aylar)):
            a.append(target_audience_names[i]+reach_names[j]+aylar[z])
            
b=[]
for i in range(len(target_audience_names)):
    for z in range(len(aylar)):
        b.append(target_audience_names[i]+"Budget"+aylar[z])
        
db_TV_12_34_years_old_reachs.set_axis(b[0:12]+a[0:48], axis=1, inplace=True)
db_TV_15_24_years_old_reachs.set_axis(b[12:24]+a[48:96], axis=1, inplace=True)
db_TV_15_34_ABC1_reachs.set_axis(b[24:36]+a[96:144], axis=1, inplace=True)
db_TV_15_34_ABC1C2_reachs.set_axis(b[36:48]+a[144:192], axis=1, inplace=True)
db_TV_20_plus_reachs.set_axis(b[48:60]+a[192:240], axis=1, inplace=True)
db_TV_12_34_ABC1C2_reachs.set_axis(b[60:72]+a[240:288], axis=1, inplace=True)
db_TV_20_44_ABC1C2_reachs.set_axis(b[72:84]+a[288:336], axis=1, inplace=True)
db_TV_12_24_C1C2_reachs.set_axis(b[84:96]+a[336:384], axis=1, inplace=True)
db_TV_12_24_ABC1C2_reachs.set_axis(b[96:108]+a[384:432], axis=1, inplace=True)
db_TV_HKF_25_44_ABC1C2_reachs.set_axis(b[108:120]+a[432:480], axis=1, inplace=True)
db_TV_15_34_years_old_reachs.set_axis(b[120:132]+a[480:528], axis=1, inplace=True)
db_TV_25_34_ABC1_reachs.set_axis(b[132:144]+a[528:576], axis=1, inplace=True)
db_TV_15_44_ABC1_reachs.set_axis(b[144:156]+a[576:624], axis=1, inplace=True)
db_TV_25_44_ABC1_reachs.set_axis(b[156:168]+a[624:672], axis=1, inplace=True)
db_TV_25_plus_ABC1_reachs.set_axis(b[168:180]+a[672:720], axis=1, inplace=True)
db_TV_15_24_ABC1C2_reachs.set_axis(b[180:192]+a[720:768], axis=1, inplace=True)

db_TV_12_34_years_old.set_axis(aylar, axis=1, inplace=True)
db_TV_15_24_years_old.set_axis(aylar, axis=1, inplace=True)
db_TV_15_34_ABC1.set_axis(aylar, axis=1, inplace=True)
db_TV_15_34_ABC1C2.set_axis(aylar, axis=1, inplace=True)
db_TV_20_plus.set_axis(aylar, axis=1, inplace=True)
db_TV_12_34_ABC1C2.set_axis(aylar, axis=1, inplace=True)
db_TV_20_44_ABC1C2.set_axis(aylar, axis=1, inplace=True)
db_TV_12_24_C1C2.set_axis(aylar, axis=1, inplace=True)
db_TV_12_24_ABC1C2.set_axis(aylar, axis=1, inplace=True)
db_TV_HKF_25_44_ABC1C2.set_axis(aylar, axis=1, inplace=True)
db_TV_15_34_years_old.set_axis(aylar, axis=1, inplace=True)
db_TV_25_34_ABC1.set_axis(aylar, axis=1, inplace=True)
db_TV_15_44_ABC1.set_axis(aylar, axis=1, inplace=True)
db_TV_25_44_ABC1.set_axis(aylar, axis=1, inplace=True)
db_TV_25_plus_ABC1.set_axis(aylar, axis=1, inplace=True)
db_TV_15_24_ABC1C2.set_axis(aylar, axis=1, inplace=True)
dfconcat_aylar=pd.concat([db_TV_12_34_years_old,db_TV_15_24_years_old,
                   db_TV_15_34_ABC1,db_TV_15_34_ABC1C2,
                   db_TV_20_plus,db_TV_12_34_ABC1C2,
                   db_TV_20_44_ABC1C2,db_TV_12_24_C1C2,
                   db_TV_12_24_ABC1C2,db_TV_HKF_25_44_ABC1C2,
                   db_TV_15_34_years_old,db_TV_25_34_ABC1,
                   db_TV_15_44_ABC1,db_TV_25_44_ABC1,
                   db_TV_25_plus_ABC1,db_TV_15_24_ABC1C2,], 
                         keys=["12-34 Years Old","15-24","15-34 ABC1",
                                                         "15-34 ABC1C2","20+","12-34 ABC1C2",
                                                         "20-44 ABC1C2","12-24 C1C2","12-24 ABC1C2",
                                                         "HKF 25-44 ABC1C2 ","15-34 Years Old","25-34 ABC1",
                                                         "15-44 ABC1","25-44 ABC1","25+ ABC1",
                                                         "15-24 ABC1C2"])

dfconcat_reachs=pd.concat([db_TV_12_34_years_old_reachs,db_TV_15_24_years_old_reachs,
                   db_TV_15_34_ABC1_reachs,db_TV_15_34_ABC1C2_reachs,
                   db_TV_20_plus_reachs,db_TV_12_34_ABC1C2_reachs,
                   db_TV_20_44_ABC1C2_reachs,db_TV_12_24_C1C2_reachs,
                   db_TV_12_24_ABC1C2_reachs,db_TV_HKF_25_44_ABC1C2_reachs,
                   db_TV_15_34_years_old_reachs,db_TV_25_34_ABC1_reachs,
                   db_TV_15_44_ABC1_reachs,db_TV_25_44_ABC1_reachs,
                   db_TV_25_plus_ABC1_reachs,db_TV_15_24_ABC1C2_reachs,
                   ], keys=["12-34 Years Old","15-24","15-34 ABC1",
                                                         "15-34 ABC1C2","20+","12-34 ABC1C2",
                                                         "20-44 ABC1C2","12-24 C1C2","12-24 ABC1C2",
                                                         "HKF 25-44 ABC1C2 ","15-34 Years Old","25-34 ABC1",
                                                         "15-44 ABC1","25-44 ABC1","25+ ABC1",
                                                         "15-24 ABC1C2"],axis=1)
a=[]
for i in range(len(target_audience_names_FB_YT_OTHER)):
    for j in range(len(reach_names)):
        a.append(target_audience_names_FB_YT_OTHER[i]+reach_names[j])
        
b=[]
for i in range(len(target_audience_names_FB_YT_OTHER)):
    b.append(target_audience_names_FB_YT_OTHER[i]+"Budget")
    
db_FB_25_34_ABC1_reachs.set_axis(b[0:1]+a[0:4], axis=1, inplace=True)
db_FB_20_44_ABC1C2_reachs.set_axis(b[1:2]+a[4:8], axis=1, inplace=True)
db_FB_20_plus_reachs.set_axis(b[2:3]+a[8:12], axis=1, inplace=True)
db_FB_HKF_25_44_ABC1C2_reachs.set_axis(b[3:4]+a[12:16], axis=1, inplace=True)
db_FB_12_34_years_old_reachs.set_axis(b[4:5]+a[16:20], axis=1, inplace=True)
db_FB_12_24_ABC1C2_reachs.set_axis(b[5:6]+a[20:24], axis=1, inplace=True)
db_FB_12_24_C1C2_reachs.set_axis(b[6:7]+a[24:28], axis=1, inplace=True)
db_FB_12_34_ABC1C2_reachs.set_axis(b[7:8]+a[28:32], axis=1, inplace=True)
db_FB_15_24_reachs.set_axis(b[8:9]+a[32:36], axis=1, inplace=True)
db_FB_15_34_ABC1C2_reachs.set_axis(b[9:10]+a[36:40], axis=1, inplace=True)
db_FB_15_24_ABC1C2_reachs.set_axis(b[10:11]+a[40:44], axis=1, inplace=True)
db_FB_15_34_years_old_reachs.set_axis(b[11:12]+a[44:48], axis=1, inplace=True)
db_FB_25_plus_ABC1_reachs.set_axis(b[12:13]+a[48:52], axis=1, inplace=True)
db_FB_15_34_ABC1_reachs.set_axis(b[13:14]+a[52:56], axis=1, inplace=True)
db_FB_15_44_ABC1_reachs.set_axis(b[14:15]+a[56:60], axis=1, inplace=True)
db_FB_25_44_ABC1_reachs.set_axis(b[15:16]+a[60:64], axis=1, inplace=True)

dfconcat_reachs_FB=pd.concat([db_FB_25_34_ABC1_reachs,db_FB_20_44_ABC1C2_reachs,
                   db_FB_20_plus_reachs,db_FB_HKF_25_44_ABC1C2_reachs,
                   db_FB_12_34_years_old_reachs,db_FB_12_24_ABC1C2_reachs,
                   db_FB_12_24_C1C2_reachs,db_FB_12_34_ABC1C2_reachs,
                   db_FB_15_24_reachs,db_FB_15_34_ABC1C2_reachs,
                   db_FB_15_24_ABC1C2_reachs,db_FB_15_34_years_old_reachs,
                   db_FB_25_plus_ABC1_reachs,db_FB_15_34_ABC1_reachs,
                   db_FB_15_44_ABC1_reachs,db_FB_25_44_ABC1_reachs,
                   ], 
                             keys=target_audience_names_FB_YT_OTHER,axis=1)    

db_YT_25_34_ABC1_reachs.set_axis(b[0:1]+a[0:4], axis=1, inplace=True)
db_YT_20_44_ABC1C2_reachs.set_axis(b[1:2]+a[4:8], axis=1, inplace=True)
db_YT_20_plus_reachs.set_axis(b[2:3]+a[8:12], axis=1, inplace=True)
db_YT_HKF_25_44_ABC1C2_reachs.set_axis(b[3:4]+a[12:16], axis=1, inplace=True)
db_YT_12_34_years_old_reachs.set_axis(b[4:5]+a[16:20], axis=1, inplace=True)
db_YT_12_24_ABC1C2_reachs.set_axis(b[5:6]+a[20:24], axis=1, inplace=True)
db_YT_12_24_C1C2_reachs.set_axis(b[6:7]+a[24:28], axis=1, inplace=True)
db_YT_12_34_ABC1C2_reachs.set_axis(b[7:8]+a[28:32], axis=1, inplace=True)
db_YT_15_24_reachs.set_axis(b[8:9]+a[32:36], axis=1, inplace=True)
db_YT_15_34_ABC1C2_reachs.set_axis(b[9:10]+a[36:40], axis=1, inplace=True)
db_YT_15_24_ABC1C2_reachs.set_axis(b[10:11]+a[40:44], axis=1, inplace=True)
db_YT_15_34_years_old_reachs.set_axis(b[11:12]+a[44:48], axis=1, inplace=True)
db_YT_25_plus_ABC1_reachs.set_axis(b[12:13]+a[48:52], axis=1, inplace=True)
db_YT_15_34_ABC1_reachs.set_axis(b[13:14]+a[52:56], axis=1, inplace=True)
db_YT_15_44_ABC1_reachs.set_axis(b[14:15]+a[56:60], axis=1, inplace=True)
db_YT_25_44_ABC1_reachs.set_axis(b[15:16]+a[60:64], axis=1, inplace=True)


dfconcat_reachs_YT=pd.concat([db_YT_25_34_ABC1_reachs,db_YT_20_44_ABC1C2_reachs,
                   db_YT_20_plus_reachs,db_YT_HKF_25_44_ABC1C2_reachs,
                   db_YT_12_34_years_old_reachs,db_YT_12_24_ABC1C2_reachs,
                   db_YT_12_24_C1C2_reachs,db_YT_12_34_ABC1C2_reachs,
                   db_YT_15_24_reachs,db_YT_15_34_ABC1C2_reachs,
                   db_YT_15_24_ABC1C2_reachs,db_YT_15_34_years_old_reachs,
                   db_YT_25_plus_ABC1_reachs,db_YT_15_34_ABC1_reachs,
                   db_YT_15_44_ABC1_reachs,db_YT_25_44_ABC1_reachs,
                   ], 
                             keys=target_audience_names_FB_YT_OTHER,axis=1)


a=np.arange(5, 5005, 5)
b=np.arange(0,5)
c=np.concatenate((b, a))
dfconcat_reachs.reset_index(drop=True,inplace=True)
dfconcat_reachs.set_index(c,inplace=True)





pt_katsayısı=data.loc[:,"Unnamed: 30":"Unnamed: 41"][2:]
grp_sayilari="GRP",0,10,20,30,40,50,60,70,80,90,100
pt_katsayısı.set_axis(grp_sayilari, axis='columns', inplace=True)
pt_katsayısı.reset_index(drop=True,inplace=True)





df=[]
for i in range(len(data["Please select brand name"])):
    if min(data["FB Budget"], key=lambda x:abs(x-data["Please select brand name"][i])):
        a=min(data["FB Budget"], key=lambda x:abs(x-data["Please select brand name"][i]))
        b=max(data["FB Budget"][data["FB Budget"]==a].index)
        df.append(data["Reach@1+"][b])
data["Facebook"]=pd.DataFrame(data=df)





df=[]
for i in range(len(data["Please select brand name"])):
    if min(data["YT Budget"], key=lambda x:abs(x-data["Please select brand name"][i])):
        a=min(data["YT Budget"], key=lambda x:abs(x-data["Please select brand name"][i]))
        b=max(data["YT Budget"][data["YT Budget"]==a].index)
        df.append(data["Reach@1+.1"][b])
data["Youtube"]=pd.DataFrame(data=df)





df=[]    
for i in range(len(data["Please select brand name"])):
    if min(data["Other Budget"], key=lambda x:abs(x-data["Please select brand name"][i])):
        a=min(data["Other Budget"], key=lambda x:abs(x-data["Please select brand name"][i]))
        b=max(data["Other Budget"][data["Other Budget"]==a].index)
        df.append(data["other REACH"][b])
data["Other Video"]=pd.DataFrame(data=df)




"""
with pd.ExcelWriter("C:\\Users\\anila\\Desktop\\filename.xlsx") as writer:
    db_TV.to_excel(writer, sheet_name="TV_Database", index=False)
    db_FB.to_excel(writer, sheet_name="FB_Database", index=False)
    db_YT.to_excel(writer, sheet_name="YT_Database", index=False)
    db_Other.to_excel(writer, sheet_name="Other_Database", index=False)
    data.to_excel(writer, sheet_name="data", index=False)
    view.to_excel(writer, sheet_name="view", index=False)
    frequency.to_excel(writer, sheet_name="Unlimited", index=False)
    figures.to_excel(writer, sheet_name="Figures", index=False)
""" 



# Initiate the App
#server = Flask(__name__)
app = dash.Dash(__name__)
server = app.server
# Read files

# Build the Components
Header_component = html.H1("Dashboard")

# visual component
maximum1=31
maximum2=31
maximum3=31
colors = ['mediumturquoise']
color= ['lightgreen']
data1 = {
   "values": [BTAQ4],
   "labels": ["Brand TOM Awareness Q4'21"],
    "domain": {"row":0,"column":0},
   "name": "parties",
   "hole": .8,
   "type": "pie",
   "hoverinfo":"label+percent",
    "textinfo":"value",
    "textfont_size":1,
    "marker":dict(colors=colors)
}
data2 = {
   "values": [BTAFY],
   "labels": ["Brand TOM Awareness FY'21"],
   "name": "parties",
    "domain": {"row": 1,"column":0},
   "hole": .8,
   "type": "pie",
   "hoverinfo":"label+percent",
    "textinfo":"value",
    "textfont_size":1,
    "marker":dict(colors=colors)
}
data3 = {
   "values": [CTAFY],
   "labels": ["Category TOM Awareness FY'21"],
   "name": "parties",
    "domain": {"row": 2,"column":0},
   "hole": .8,
   "type": "pie",
   "hoverinfo":"label+percent",
    "textinfo":"value",
    "textfont_size":1,
    "marker":dict(colors=colors)
}
data4 = {
   "values": [BSAQ4],
   "labels": ["Brand Spontaneous Awareness Q4'21"],
    "domain": {"row": 0,"column":1},
   "name": "parties",
   "hole": .8,
   "type": "pie",
   "hoverinfo":"label+percent",
    "textinfo":"value",
    "textfont_size":1,
    "marker":dict(colors=color)
}
data5 = {
   "values": [BSAFY],
   "labels": ["Brand Spontaneous Awareness FY'21"],
   "name": "parties",
    "domain": {"row": 1,"column":1},
   "hole": .8,
   "type": "pie",
   "hoverinfo":"label+percent",
    "textinfo":"value",
    "textfont_size":1,
    "marker":dict(colors=color)
}
data6 = {
   "values": [CSAFY],
   "labels": ["Category Spontaneous Awareness FY'21"],
   "name": "parties",
    "domain": {"row": 2,"column":1},
   "hole": .8,
   "type": "pie",
   "hoverinfo":"label+percent",
    "textinfo":"value",
    "textfont_size":1,
    "marker":dict(colors=color)
}

data_a = [data1,data2,data3,data4,data5,data6]

layout = go.Layout(
   {
      "grid": {"rows": 3, "columns": 2},
      "annotations": [
         {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": BTAQ4,
            "x": 0.21,
            "y": 0.88
         },
         {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": BTAFY,
            "x": 0.21,
            "y": 0.5
         },
          {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": round(CTAFY,1),
            "x": 0.20,
            "y": 0.12
         },
          {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": BSAQ4,
            "x": 0.79,
            "y": 0.88
         },
         {
            "font": {
               "size": 20
            },
            "showarrow": False,
             
            "text": BSAFY,
            "x": 0.79,
            "y": 0.5
         },
          {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": round(18.99, 1),
            "x": 0.82,
            "y": 0.12,
         }
      ]
   }
)
piefig=go.Figure(data=data_a,layout = layout)

#component 1
"""
countfig= go.FigureWidget()
countfig.add_scatter(name="Brand TOM Awareness Q4'21",x = figures.columns[2:],y = np.array(BTAQ4),fill = "tonexty")
countfig.add_scatter(name="Brand TOM Awareness FY\'21",x = figures.columns[2:],y = np.array(BTAFY),fill = "tonexty")
countfig.add_scatter(name="Category TOM Awareness FY\'21",x = figures.columns[2:],y = np.array(CTAFY),fill = "tonexty")
countfig.add_scatter(name="Brand Spontaneous Awareness Q4\'21",x = figures.columns[2:],y = np.array(BSAQ4),fill = "tonexty")
countfig.add_scatter(name="Brand Spontaneous Awareness FY\'21",x = figures.columns[2:],y = np.array(BSAFY),fill = "tonexty")
countfig.add_scatter(name="Category Spontaneous Awareness FY\'21",x = figures.columns[2:],y = np.array(CSAFY),fill = "tonexty")
"""
#component 2
"""
piefig = go.FigureWidget(
    px.pie(
        names=["Brand TOM Awareness Q4'21", "Brand TOM Awareness FY'21",
       "Category TOM Awareness FY'21", "Brand Spontaneous Awareness Q4'21",
       "Brand Spontaneous Awareness FY'21",
       "Category Spontaneous Awareness FY'21"],
        labels=["Brand TOM Awareness Q4'21", "Brand TOM Awareness FY'21",
       "Category TOM Awareness FY'21", "Brand Spontaneous Awareness Q4'21",
       "Brand Spontaneous Awareness FY'21",
       "Category Spontaneous Awareness FY'21"],
        values = [BTAQ4,BTAFY,CTAFY,BSAQ4,BSAFY,CSAFY]
    
        
    )
)
piefig.update_layout(title="Piechart")
"""

#countfig.update_layout(title = "Awareness")
#design the app layout
ay_31=["JANUARY","MARCH","MAY","JULY","AUGUST","OCTOBER","DECEMBER"]
ay_30=["APRIL","JUNE","SEPTEMBER","NOVEMBER"]
ay_28=["FEBRUARY"]
#if ay_1
app = dash.Dash(__name__, )
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H3('Screen Planning Tool', style = {"margin-bottom": "0px", 'color': 'white',"fontWeight": "bold"}),
            ]),
        ], className = "six column", id = "title")
    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),
    html.Div([
        html.Div([dbc.Col(children=[
            html.P("Select Brand Name:", className = 'fix_label', style = {'color': 'white',"fontWeight": "bold"}),
            html.Div([dcc.Dropdown(figures["Marka"], id='demo_dropdown')]),
            html.Div(dcc.Graph(id = 'pie',figure=piefig,
                      config = {'displayModeBar': 'hover'}))]),
        ], className = "create_container four columns"),
    html.Div([
            html.P("Select Target Audience:", className = 'fix_label', style = {'color': 'white',"fontWeight": "bold"}),
            html.Div(dcc.Dropdown(target_audience_names,id='target_audience',style={"display": True})),
            
            html.P("Select Campaign Type:", className = 'fix_label', style = {'color': 'white',"fontWeight": "bold"}),
            dcc.Dropdown(campaign_type, 'LAUNCH', id='secilen_campaign_type',style={"display": True}),
            html.Div([
                html.H6("Select Month's:", className = 'dcc_compon', style = {"color": "white","fontWeight": "bold","display": "inline-block","width": "25%"}),
                html.H6("Select PT 's %:", className = 'dcc_compon', style = {"color": "white","fontWeight": "bold","display": "inline-block","width": "25%"}),
                html.H6("Select GRP 's %:", className = 'dcc_compon', style = {"color": "white","fontWeight": "bold","display": "inline-block","width": "25%"}),
                html.H6("Select DAYS 's:", className = 'dcc_compon', style = {"color": "white","fontWeight": "bold","display": "inline-block","width": "15%"}),
                ]),
                html.Div(dcc.Dropdown( aylar,id='ay_1',placeholder="1.AYI SEÇİNİZ",className='dcc_compon' ),style={"display": "inline-block","width": "16%"}),
                html.Div(dcc.Slider(id='secilen1_PT',min=0,max=100,step=10,className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True}), style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Slider(id='secilen1_GRP',min=0,max=100,step=10,className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True}), style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Slider(id='gun1',min=0,max=maximum1,step=1,marks={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",maximum1:str(maximum1)},className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True} ),style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Dropdown( aylar,id='ay_2',placeholder="2.AYI SEÇİNİZ",className='dcc_compon' ),style={"display": "inline-block","width": "16%"}),
                html.Div(dcc.Slider(id='secilen2_PT',min=0,max=100,step=10,className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True}), style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Slider(id='secilen2_GRP',min=0,max=100,step=10,className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True}), style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Slider(id='gun2',min=0,max=maximum2,step=1,marks={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",maximum2:str(maximum2)},className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True} ),style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Dropdown( aylar,id='ay_3',placeholder="3.AYI SEÇİNİZ",className='dcc_compon' ),style={"display": "inline-block","width": "16%"}),
                html.Div(dcc.Slider(id='secilen3_PT',min=0,max=100,step=10,className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True}), style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Slider(id='secilen3_GRP',min=0,max=100,step=10,className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True}), style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
                html.Div(dcc.Slider(id='gun3',min=0,max=maximum3,step=1,marks={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",maximum3:str(maximum3)},className='dcc_compon',tooltip={"placement": "bottom", "always_visible": True} ),style={"display": "inline-block","width": "28%","fontWeight": "bold"}),
            dcc.Store(id="target",data=[]),
            dcc.Store(id="all_number",data=[]),
            dcc.Store(id="kampanya_tipi",data=[]),
            dcc.Store(id="result_min",data=[]),
            dcc.Store(id="result_max",data=[]),
            dcc.Store(id="budgets",data=[]),
            dcc.Store(id="reachs",data=[]),
            dcc.Store(id="ay_1_1",data=[]),
            dcc.Store(id="ay_2_2",data=[]),
            dcc.Store(id="ay_3_3",data=[]),
        ], className = "create_container eight columns"),
    ], className = "row flex-display"),
    html.Div([
        

        html.Div([
            html.Div([
            html.P("Select TV Budget:", className = 'dcc_compon', style = {'color': 'white',"fontWeight": "bold"}),
            html.Div(dcc.Input(id='secilen_TV', type='number', value=0,placeholder="TV Budget Giriniz",className='dcc_compon'),style={"display": "inline-block","width": "50%"}),
            html.P("Select FB Budget:", className = 'dcc_compon', style = {'color': 'white',"fontWeight": "bold"}),
            html.Div(dcc.Input(id='secilen_FB', type='number', value=0,placeholder="FB Budget Giriniz",className='dcc_compon'),style={"display": "inline-block","width": "50%"}),
            html.P("Select YT Budget:", className = 'dcc_compon', style = {'color': 'white',"fontWeight": "bold"}),
            html.Div(dcc.Input(id='secilen_YT', type='number', value=0,placeholder="YT Budget Giriniz",className='dcc_compon'),style={"display": "inline-block","width": "50%"}),
            html.P("Select TIKTOK Budget:", className = 'dcc_compon', style = {'color': 'white',"fontWeight": "bold"}),
            html.Div(dcc.Input(id='secilen_TIKTOK', type='number', value=0,placeholder="TIKTOK Budget Giriniz",className='dcc_compon'),style={"display": "inline-block","width": "50%"}),
            html.P("Select OTHER Budget:", className = 'dcc_compon', style = {'color': 'white',"fontWeight": "bold"}),
            html.Div(dcc.Input(id='secilen_OTHER', type='number', value=0,placeholder="OTHER Budget Giriniz",className='dcc_compon'),style={"display": "inline-block","width": "50%"}),
            ],style={'float': 'right','margin': 'auto'}),
            html.Div([dcc.Graph(id = 'bar',config = {'displayModeBar': 'hover'},className = "dcc_compon",style={"height":800})],style={'float': 'left'}),
        ], className="create_container six columns"),
         html.Div([
             html.Div([dcc.Graph(id = 'gauge',config = {'displayModeBar': 'hover'},className = "dcc_compon",style={'width': '100%', 'height': 800})]),
                  ],className = "create_container six columns"),
        
    ], className = "row flex-display"),
    html.Div([
        html.Div([
            html.Div([dcc.Graph(id = 'bar2',config = {'displayModeBar': 'hover'},className = "dcc_compon",style={"height":800})],style={'float': 'left'}),
                    ], className = "create_container six columns"),
        html.Div([
            html.Div([dcc.Graph(id= "pie2",config = {'displayModeBar': 'hover'},className = "dcc_compon",style={'width': '100%',"height":800})]),
        ], className = "create_container six columns"),
    ],className = "row flex-display"),
    ], id = "mainContainer", style = {"display": "flex", "flex-direction": "column"})
#--------------------------BRAND VE CATEGORY AWARENESS PİE CHART BÖLÜMÜ -----------------------------
@app.callback(
    Output("pie", "figure"),
    Input("demo_dropdown", "value"))
def generate_chart(demo_dropdown):
    for i in range(len(figures["Marka"])):
        if figures["Marka"][i]==demo_dropdown:
            BTAQ4=figures["Brand TOM Awareness Q4\'21"][i]
            BTAFY=figures["Brand TOM Awareness FY\'21"][i]
            CTAFY=figures["Category TOM Awareness FY\'21"][i]
            BSAQ4=figures["Brand Spontaneous Awareness Q4\'21"][i]
            BSAFY=figures["Brand Spontaneous Awareness FY\'21"][i]
            CSAFY=figures["Category Spontaneous Awareness FY\'21"][i]
    #fig = go.Figure(data=[go.Pie(labels=["Brand TOM Awareness Q4'21", "Brand TOM Awareness FY'21",
       #"Category TOM Awareness FY'21", "Brand Spontaneous Awareness Q4'21",
       #"Brand Spontaneous Awareness FY'21","Category Spontaneous Awareness FY'21"],
        #values=[BTAQ4,BTAFY,CTAFY,BSAQ4,BSAFY,CSAFY],insidetextorientation='radial')])
    data1 = {
    "values": [BTAQ4],
    "labels": ["Brand TOM Awareness Q4'21"],
    "domain": {"row":0,"column":0},
    "name": "parties",
    "hole": .8,
    "type": "pie",
    "hoverinfo":"label+percent",
    "textinfo":"value",
    "textfont_size":1,
    "marker":dict(colors=colors)
    }
    data2 = {
       "values": [BTAFY],
       "labels": ["Brand TOM Awareness FY'21"],
       "name": "parties",
        "domain": {"row": 1,"column":0},
       "hole": .8,
       "type": "pie",
       "hoverinfo":"label+percent",
        "textinfo":"value",
        "textfont_size":1,
        "marker":dict(colors=colors)
    }
    data3 = {
       "values": [CTAFY],
       "labels": ["Category TOM Awareness FY'21"],
       "name": "parties",
        "domain": {"row": 2,"column":0},
       "hole": .8,
       "type": "pie",
       "hoverinfo":"label+percent",
        "textinfo":"value",
        "textfont_size":1,
        "marker":dict(colors=colors)
    }
    data4 = {
       "values": [BSAQ4],
       "labels": ["Brand Spontaneous Awareness Q4'21"],
        "domain": {"row": 0,"column":1},
       "name": "parties",
       "hole": .8,
       "type": "pie",
       "hoverinfo":"label+percent",
        "textinfo":"value",
        "textfont_size":1,
        "marker":dict(colors=color)
    }
    data5 = {
       "values": [BSAFY],
       "labels": ["Brand Spontaneous Awareness FY'21"],
       "name": "parties",
        "domain": {"row": 1,"column":1},
       "hole": .8,
       "type": "pie",
       "hoverinfo":"label+percent",
        "textinfo":"value",
        "textfont_size":1,
        "marker":dict(colors=color)
    }
    data6 = {
       "values": [CSAFY],
       "labels": ["Category Spontaneous Awareness FY'21"],
       "name": "parties",
        "domain": {"row": 2,"column":1},
       "hole": .8,
       "type": "pie",
       "hoverinfo":"label+percent",
        "textinfo":"value",
        "textfont_size":1,
        "marker":dict(colors=color)
    }

    data_a = [data1,data2,data3,data4,data5,data6]

    layout = go.Layout(
       {
          "grid": {"rows": 3, "columns": 2},
          "annotations": [
             {
                "font": {
                   "size": 20
                },
                "showarrow": False,
                "text": round(BTAQ4,1),
                "x": 0.21,
                "y": 0.88
             },
             {
                "font": {
                   "size": 20
                },
                "showarrow": False,
                "text": round(BTAFY,1),
                "x": 0.21,
                "y": 0.5
             },
              {
                "font": {
                   "size": 20
                },
                "showarrow": False,
                "text": round(CTAFY,1),
                "x": 0.20,
                "y": 0.12
             },
              {
                "font": {
                   "size": 20
                },
                "showarrow": False,
                "text": round(BSAQ4,1),
                "x": 0.79,
                "y": 0.88
             },
             {
                "font": {
                   "size": 20
                },
                "showarrow": False,

                "text": round(BSAFY,1),
                "x": 0.79,
                "y": 0.5
             },
              {
                "font": {
                   "size": 20
                },
                "showarrow": False,
                "text": round(CSAFY,1),
                "x": 0.82,
                "y": 0.12,
             }
          ]
       }
    )
    fig=go.Figure(data=data_a,layout = layout)
    return fig

#---------------------------TARGET AUDİENCE SEÇİMİ BÖLÜMÜ ---------------------------------------------


@app.callback(
    Output("target","dataset1"),
    Input("target_audience", "value"))
def select_target_auidence(target_audience):
    secilen_target=target_audience
    for i in range(len(data["Please select brand name.1"][1:29].drop_duplicates().reset_index(drop="index"))):
        if (data["Please select brand name.1"][1:29].drop_duplicates().reset_index(drop="index")[i]==secilen_target):
            target_audience=data["Please select brand name.1"][1:29].drop_duplicates().reset_index(drop="index")[i]
            dataset1=[target_audience]
            return dataset1
#---------------------------CAMPAİGN TYPE SEÇİMİ BÖLÜMÜ -----------------------------------------------

@app.callback(
    Output("kampanya_tipi","dataset2"),
    Input("secilen_campaign_type", "value"))
def select_campaign_type(secilen_campaign_type):
    dataset2=[secilen_campaign_type]
    return dataset2


#---------------------------PT-GRP-AY-GÜN SEÇİMİ BÖLÜMÜ -----------------------------------------------
@app.callback(
    Output("all_number","dataset"),
    Input("ay_1", "value"),
    Input("ay_2", "value"),
    Input("ay_3", "value"),
    Input("secilen1_PT", "value"),
    Input("secilen1_GRP", "value"),
    Input("secilen2_PT", "value"),
    Input("secilen2_GRP", "value"),
    Input("secilen3_PT", "value"),
    Input("secilen3_GRP", "value"),
    Input("gun1", "value"),
    Input("gun2", "value"),
    Input("gun3", "value"))

def grp_pt_day(ay_1,ay_2,ay_3,secilen1_PT, secilen1_GRP, secilen2_PT,secilen2_GRP, secilen3_PT, secilen3_GRP,gun1,gun2,gun3):
    
    for i in range(len(data["Unnamed: 25"][1:12])):
        if data["Unnamed: 25"][1:12][i+1]==secilen1_PT:
            PT1=data["Unnamed: 25"][1:12][i+1]
        if data["Unnamed: 25"][1:12][i+1]==secilen2_PT:
            PT2=data["Unnamed: 25"][1:12][i+1]
        if data["Unnamed: 25"][1:12][i+1]==secilen3_PT:
            PT3=data["Unnamed: 25"][1:12][i+1]
    for i in range(len(data["Unnamed: 25"][1:12])):
        if data["Unnamed: 25"][1:12][i+1]==secilen1_GRP:
            GRP1=data["Unnamed: 25"][1:12][i+1]
        if data["Unnamed: 25"][1:12][i+1]==secilen2_GRP:
            GRP2=data["Unnamed: 25"][1:12][i+1]
        if data["Unnamed: 25"][1:12][i+1]==secilen3_GRP:
            GRP3=data["Unnamed: 25"][1:12][i+1]
    dataset=[ay_1,ay_2,ay_3,PT1,GRP1,PT2,GRP2,PT3,GRP3,gun1,gun2,gun3]
    return dataset

@app.callback(
    Output("gun1","max"),
    Output("gun1","marks"),
    Input("ay_1", "value"))
def maximum_1(ay_1):
    maximum1=0
    for i in range(len(ay_31)):
        if ay_1==ay_31[i]:
            maximum1=31
    for i in range(len(ay_30)):
        if ay_1==ay_30[i]:
            maximum1=30
    for i in range(len(ay_28)):
        if ay_1==ay_28[i]:
            maximum1=28
    if maximum1==31:
        marks1={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",31:"31"}
    if maximum1==30:
        marks1={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",30:"30"}
    if maximum1==28:
        marks1={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",28:"28"}
    return maximum1,marks1
@app.callback(
    Output("gun2","max"),
    Output("gun2","marks"),
    Input("ay_2", "value"))
def select_campaign_type(ay_2):
    maximum2=0
    for i in range(len(ay_31)):
        if ay_2==ay_31[i]:
            maximum2=31
    for i in range(len(ay_30)):
        if ay_2==ay_30[i]:
            maximum2=30
    for i in range(len(ay_28)):
        if ay_2==ay_28[i]:
            maximum2=28
    if maximum2==31:
        marks2={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",31:"31"}
    if maximum2==30:
        marks2={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",30:"30"}
    if maximum2==28:
        marks2={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",28:"28"}
    return maximum2,marks2

@app.callback(
    Output("gun3","max"),
    Output("gun3","marks"),
    Input("ay_3", "value"))
def select_campaign_type(ay_3):
    maximum3=0
    for i in range(len(ay_31)):
        if ay_3==ay_31[i]:
            maximum3=31
    for i in range(len(ay_30)):
        if ay_3==ay_30[i]:
            maximum3=30
    for i in range(len(ay_28)):
        if ay_3==ay_28[i]:
            maximum3=28
    if maximum3==31:
        marks3={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",31:"31"}
    if maximum3==30:
        marks3={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",30:"30"}
    if maximum3==28:
        marks3={0:"0",5:"5",10:"10",15:"15",20:"20",25:"25",28:"28"}
    return maximum3,marks3

#---------------------------Hesaplamalar BÖLÜMÜ -----------------------------------------------
@app.callback(
    Output("result_min","result_min"),
    Output("result_max","result_max"),
    Input("all_number", "dataset"),
    Input("target","dataset1"),
    Input("kampanya_tipi","dataset2"))
def hesaplama(dataset,dataset1,dataset2):
    yuzde_pt_grp=[]
    secilen_ay={"JANUARY":0,"FEBRUARY":1,"MARCH":2,"APRIL":3,"MAY":4,"JUNE":5,"JULY":6,"AUGUST":7,"SEPTEMBER":8,"OCTOBER":9,"NOVEMBER":10,"DECEMBER":11}
    total_day=dataset[9]+dataset[10]+dataset[11]
    active_months=total_day/30
    yuzde_pt_grp.append(((dataset[3]*dataset[4])/100)+((dataset[5]*dataset[6])/100)+((dataset[7]*dataset[8])/100))
    yuzde_pt_grp=sum(yuzde_pt_grp)
    secilen1_PT=int(dataset[3]/10)
    secilen2_PT=int(dataset[4]/10)
    secilen3_PT=int(dataset[5]/10)
    cpp1=dfconcat_aylar.loc[dataset1[0]].iloc[secilen1_PT][secilen_ay[dataset[0]]]
    cpp2=dfconcat_aylar.loc[dataset1[0]].iloc[secilen2_PT][secilen_ay[dataset[1]]]
    cpp3=dfconcat_aylar.loc[dataset1[0]].iloc[secilen3_PT][secilen_ay[dataset[2]]]
    cpp=(cpp1*dataset[4])/100+(cpp2*dataset[6])/100+(cpp3*dataset[8])/100
    secilen_ay1=secilen_ay[dataset[0]]
    
    secilen_TVC=10
    df=[]
    for i in range(len(data["TV Budget"])):
        df.append((data["GRP"][i]*secilen_TVC*cpp)/1000)
    data["TV Budget"]=pd.DataFrame(data=df)
    df=[]
    for i in range(len(dfconcat_reachs)-5):
        df.append(dfconcat_reachs[dataset1[0]][dataset1[0]+reach_names[0]+aylar[secilen_ay1]].iloc[i+5]*pt_katsayısı[secilen1_PT*10][i]   )
    data['Reach@1+.2']=pd.DataFrame(data=df)
    j=0
    df=[]
    for i in range(len(data['Please select brand name'])):
        if data['Please select brand name'][i]>data["TV Budget"][j]:
            j=j+1
            df.append(data["GRP"][j])
        elif data['Please select brand name'][i]<=data["TV Budget"][j]:
            df.append(data["GRP"][j])
        else:
            break            
    data["TV GRP"]=pd.DataFrame(data=df)
        #TV İÇİN campaign_type = "LAUNCH","ONGOING"
    for i in range(len(data[["Unnamed: 44","Unnamed: 45","Unnamed: 46","Unnamed: 47","Unnamed: 48"]][31:48])):
        if data["Unnamed: 44"][31:48][i+31]==dataset1[0] and dataset2[0]=="ONGOING":
            ongoing_min_TV=data["Unnamed: 45"][31:48][i+31]
            ongoing_max_TV=data["Unnamed: 46"][31:48][i+31]
        elif data["Unnamed: 44"][31:48][i+31]==dataset1[0] and dataset2[0]=="LAUNCH":
            launch_min_TV=data["Unnamed: 47"][31:48][i+31]
            launch_max_TV=data["Unnamed: 48"][31:48][i+31]
#FACEBOOK İÇİN
    for i in range(len(data[["Unnamed: 44","Unnamed: 45","Unnamed: 46","Unnamed: 47","Unnamed: 48"]][50:67])):
        if data["Unnamed: 44"][50:67][i+50]==dataset1[0] and dataset2[0]=="ONGOING":
            ongoing_min_FB=data["Unnamed: 45"][50:67][i+50]
            ongoing_max_FB=data["Unnamed: 46"][50:67][i+50]
        elif data["Unnamed: 44"][50:67][i+50]==dataset1[0] and dataset2[0]=="LAUNCH":
            launch_min_FB=data["Unnamed: 47"][50:67][i+50]
            launch_max_FB=data["Unnamed: 48"][50:67][i+50]
#YOUTUBE İÇİN
    for i in range(len(data[["Unnamed: 44","Unnamed: 45","Unnamed: 46","Unnamed: 47","Unnamed: 48"]][69:86])):
        if data["Unnamed: 44"][69:86][i+69]==dataset1[0] and dataset2[0]=="ONGOING":
            ongoing_min_YT=data["Unnamed: 45"][69:86][i+69]
            ongoing_max_YT=data["Unnamed: 46"][69:86][i+69]
        elif data["Unnamed: 44"][69:86][i+69]==dataset1[0] and dataset2[0]=="LAUNCH":
            launch_min_YT=data["Unnamed: 47"][69:86][i+69]
            launch_max_YT=data["Unnamed: 48"][69:86][i+69]
#OTHER VİDEO İÇİN
    for i in range(len(data[["Unnamed: 44","Unnamed: 45","Unnamed: 46","Unnamed: 47","Unnamed: 48"]][89:106])):
        if data["Unnamed: 44"][89:106][i+89]==dataset1[0] and dataset2[0]=="ONGOING":
            ongoing_min_OTHER=data["Unnamed: 45"][89:106][i+89]
            ongoing_max_OTHER=data["Unnamed: 46"][89:106][i+89]
        elif data["Unnamed: 44"][89:106][i+89]==dataset1[0] and dataset2[0]=="LAUNCH":
            launch_min_OTHER=data["Unnamed: 47"][89:106][i+89]
            launch_max_OTHER=data["Unnamed: 48"][89:106][i+89]
#TİKTOK İÇİN
    for i in range(len(data["Please select brand name.1"][1:29].drop_duplicates().reset_index(drop="index"))):
        if data["Please select brand name.1"][1:29].drop_duplicates().reset_index(drop="index")[i]==dataset1[0]:
            tiktok_katsayisi=[]
            tiktok_katsayisi=data["Unnamed: 60"][i+1]
            
    df=[]
    for i in range(len(data["Facebook"])):
        df.append(data["Facebook"].loc[i]*tiktok_katsayisi)
    data["TİKTOK"]=pd.DataFrame(data=df)
    #tiktok reach@1
    df=[]
    for i in range(len(data["Reach@1+"])):
        df.append(data["Reach@1+"].loc[i]*tiktok_katsayisi)
    data["Reach"]=pd.DataFrame(data=df)
    #tiktok reach@2
    df=[]
    for i in range(len(data["Please select brand nameReach@2+"])):
        df.append(data["Please select brand nameReach@2+"].loc[i]*tiktok_katsayisi)
    data["Please select brand nameReach@2+.3"]=pd.DataFrame(data=df)
    
    if dataset2[0]=="ONGOING":
        ongoing_min_TIKTOK=ongoing_min_FB*tiktok_katsayisi
        ongoing_max_TIKTOK=ongoing_max_FB*tiktok_katsayisi
    elif dataset2[0]=="LAUNCH":
        launch_min_TIKTOK=launch_min_FB*tiktok_katsayisi
        launch_max_TIKTOK=launch_max_FB*tiktok_katsayisi
        
    if dataset2[0]=="ONGOING":
        budget_min_TV=active_months*ongoing_min_TV
        budget_max_TV=active_months*ongoing_max_TV
        if data["TV GRP"][data["TV GRP"]==min(data["TV GRP"], key=lambda x:abs(x-budget_min_TV))].index.nunique()>1:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_min_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_min_TV=max(data["Bütçe"][b])
        else:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_min_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_min_TV=max(data["Bütçe"][b])
        if data["TV GRP"][data["TV GRP"]==min(data["TV GRP"], key=lambda x:abs(x-budget_max_TV))].index.nunique()>1:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_max_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_max_TV=max(data["Bütçe"][b])
        else:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_max_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_max_TV=max(data["Bütçe"][b])

    if dataset2[0]=="LAUNCH":
        budget_min_TV=active_months*launch_min_TV
        budget_max_TV=active_months*launch_max_TV
        if data["TV GRP"][data["TV GRP"]==min(data["TV GRP"], key=lambda x:abs(x-budget_min_TV))].index.nunique()>1:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_min_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_min_TV=max(data["Bütçe"][b])
        else:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_min_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_min_TV=max(data["Bütçe"][b])
        if data["TV GRP"][data["TV GRP"]==min(data["TV GRP"], key=lambda x:abs(x-budget_max_TV))].index.nunique()>1:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_max_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_max_TV=max(data["Bütçe"][b])
        else:
            a=min(data["TV GRP"], key=lambda x:abs(x-budget_max_TV))
            b=data["TV GRP"][data["TV GRP"]==a].index
            budget_max_TV=max(data["Bütçe"][b])
        
    if active_months<1.4 and dataset2[0]=="LAUNCH":
        FB_reach_min=(1-(1-launch_min_FB/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        FB_reach_min=(1-(1-launch_min_FB/100)*(1-launch_min_FB/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        FB_reach_min=(1-(1-launch_min_FB/100)*(1-launch_min_FB/100)*(1-launch_min_FB/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        FB_reach_min=(1-(1-ongoing_min_FB/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        FB_reach_min=(1-(1-ongoing_min_FB/100)*(1-ongoing_min_FB/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        FB_reach_min=(1-(1-ongoing_min_FB/100)*(1-ongoing_min_FB/100)*(1-ongoing_min_FB/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="LAUNCH":
        FB_reach_max=(1-(1-launch_max_FB/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        FB_reach_max=(1-(1-launch_max_FB/100)*(1-launch_max_FB/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        FB_reach_max=(1-(1-launch_max_FB/100)*(1-launch_max_FB/100)*(1-launch_max_FB/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        FB_reach_max=(1-(1-ongoing_max_FB/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        FB_reach_max=(1-(1-ongoing_max_FB/100)*(1-ongoing_max_FB/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        FB_reach_max=(1-(1-ongoing_max_FB/100)*(1-ongoing_max_FB/100)*(1-ongoing_max_FB/100))*100*0.7

    if active_months<1.4 and dataset2[0]=="LAUNCH":
        YT_reach_min=(1-(1-launch_min_YT/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        YT_reach_min=(1-(1-launch_min_YT/100)*(1-launch_min_YT/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        YT_reach_min=(1-(1-launch_min_YT/100)*(1-launch_min_YT/100)*(1-launch_min_YT/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        YT_reach_min=(1-(1-ongoing_min_YT/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        YT_reach_min=(1-(1-ongoing_min_YT/100)*(1-ongoing_min_YT/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        YT_reach_min=(1-(1-ongoing_min_YT/100)*(1-ongoing_min_YT/100)*(1-ongoing_min_YT/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="LAUNCH":
        YT_reach_max=(1-(1-launch_max_YT/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        YT_reach_max=(1-(1-launch_max_YT/100)*(1-launch_max_YT/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        YT_reach_max=(1-(1-launch_max_YT/100)*(1-launch_max_YT/100)*(1-launch_max_YT/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        YT_reach_max=(1-(1-ongoing_max_YT/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        YT_reach_max=(1-(1-ongoing_max_YT/100)*(1-ongoing_max_YT/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        YT_reach_max=(1-(1-ongoing_max_YT/100)*(1-ongoing_max_YT/100)*(1-ongoing_max_YT/100))*100*0.7

    if active_months<1.4 and dataset2[0]=="LAUNCH":
        TIKTOK_reach_min=(1-(1-launch_min_TIKTOK/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        TIKTOK_reach_min=(1-(1-launch_min_TIKTOK/100)*(1-launch_min_TIKTOK/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        TIKTOK_reach_min=(1-(1-launch_min_TIKTOK/100)*(1-launch_min_TIKTOK/100)*(1-launch_min_TIKTOK/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        TIKTOK_reach_min=(1-(1-ongoing_min_TIKTOK/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        TIKTOK_reach_min=(1-(1-ongoing_min_TIKTOK/100)*(1-ongoing_min_TIKTOK/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        TIKTOK_reach_min=(1-(1-ongoing_min_TIKTOK/100)*(1-ongoing_min_TIKTOK/100)*(1-ongoing_min_TIKTOK/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="LAUNCH":
        TIKTOK_reach_max=(1-(1-launch_max_TIKTOK/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        TIKTOK_reach_max=(1-(1-launch_max_TIKTOK/100)*(1-launch_max_TIKTOK/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        TIKTOK_reach_max=(1-(1-launch_max_TIKTOK/100)*(1-launch_max_TIKTOK/100)*(1-launch_max_TIKTOK/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        TIKTOK_reach_max=(1-(1-ongoing_max_TIKTOK/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        TIKTOK_reach_max=(1-(1-ongoing_max_TIKTOK/100)*(1-ongoing_max_TIKTOK/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        TIKTOK_reach_max=(1-(1-ongoing_max_TIKTOK/100)*(1-ongoing_max_TIKTOK/100)*(1-ongoing_max_TIKTOK/100))*100*0.7

    if active_months<1.4 and dataset2[0]=="LAUNCH":
        OTHER_reach_min=(1-(1-launch_min_OTHER/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        OTHER_reach_min=(1-(1-launch_min_OTHER/100)*(1-launch_min_OTHER/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        OTHER_reach_min=(1-(1-launch_min_OTHER/100)*(1-launch_min_OTHER/100)*(1-launch_min_OTHER/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        OTHER_reach_min=(1-(1-ongoing_min_OTHER/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        OTHER_reach_min=(1-(1-ongoing_min_OTHER/100)*(1-ongoing_min_OTHER/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        OTHER_reach_min=(1-(1-ongoing_min_OTHER/100)*(1-ongoing_min_OTHER/100)*(1-ongoing_min_OTHER/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="LAUNCH":
        OTHER_reach_max=(1-(1-launch_max_OTHER/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="LAUNCH":
        OTHER_reach_max=(1-(1-launch_max_OTHER/100)*(1-launch_max_OTHER/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="LAUNCH":
        OTHER_reach_max=(1-(1-launch_max_OTHER/100)*(1-launch_max_OTHER/100)*(1-launch_max_OTHER/100))*100*0.7
    if active_months<1.4 and dataset2[0]=="ONGOING":
        OTHER_reach_max=(1-(1-ongoing_max_OTHER/100))*100
    elif 1.4<=active_months<=2.6 and dataset2[0]=="ONGOING":
        OTHER_reach_max=(1-(1-ongoing_max_OTHER/100)*(1-ongoing_max_OTHER/100))*100*0.8
    elif active_months>2.6 and dataset2[0]=="ONGOING":
        OTHER_reach_max=(1-(1-ongoing_max_OTHER/100)*(1-ongoing_max_OTHER/100)*(1-ongoing_max_OTHER/100))*100*0.7    

    a=min(data["Facebook"], key=lambda x:abs(x-FB_reach_min))
    b=data["Facebook"][data["Facebook"]==a].index
    budget_min_FB=data["Bütçe"][b].iloc[0]

    a=min(data["Facebook"], key=lambda x:abs(x-FB_reach_max))
    b=data["Facebook"][data["Facebook"]==a].index
    budget_max_FB=data["Bütçe"][b].iloc[0]

    a=min(data["Youtube"], key=lambda x:abs(x-YT_reach_min))
    b=data["Youtube"][data["Youtube"]==a].index
    budget_min_YT=data["Bütçe"][b].iloc[0]

    a=min(data["Youtube"], key=lambda x:abs(x-YT_reach_max))
    b=data["Youtube"][data["Youtube"]==a].index
    budget_max_YT=data["Bütçe"][b].iloc[0]

    a=min(data["TİKTOK"], key=lambda x:abs(x-TIKTOK_reach_min))
    b=data["TİKTOK"][data["TİKTOK"]==a].index
    budget_min_TIKTOK=data["Bütçe"][b].iloc[0]

    a=min(data["TİKTOK"], key=lambda x:abs(x-TIKTOK_reach_max))
    b=data["TİKTOK"][data["TİKTOK"]==a].index
    budget_max_TIKTOK=data["Bütçe"][b].iloc[0]

    a=min(data["Other Video"], key=lambda x:abs(x-OTHER_reach_min))
    b=data["Other Video"][data["Other Video"]==a].index
    budget_min_OTHER=data["Bütçe"][b].iloc[0]

    a=min(data["Other Video"], key=lambda x:abs(x-OTHER_reach_max))
    b=data["Other Video"][data["Other Video"]==a].index
    budget_max_OTHER=data["Bütçe"][b].iloc[0]

    budget_all_min=budget_min_OTHER+budget_min_FB+budget_min_TIKTOK+budget_min_TV+budget_min_YT
    budget_all_max=budget_max_OTHER+budget_max_FB+budget_max_TIKTOK+budget_max_TV+budget_max_YT
    result_min = [budget_min_TV,budget_min_FB,budget_min_YT,budget_min_TIKTOK,budget_min_OTHER,budget_all_min]
    result_max = [budget_max_TV,budget_max_FB,budget_max_YT,budget_max_TIKTOK,budget_max_OTHER,budget_all_max]
    print("dataset:         ",dataset)
    print("dataset1:         ",dataset1)
    print("dataset2:         ",dataset2)
    print("result_min:"        ,result_min)
    print("result_max:"        ,result_max)
    print("TV:    ",budget_min_TV," ",budget_max_TV)
    print("FB:    ",budget_min_FB," ",budget_max_FB)
    print("YT:    ",budget_min_YT," ",budget_max_YT)
    print("TİKTOK:    ",budget_min_TIKTOK," ",budget_max_TIKTOK)
    print("OTHER:    ",budget_min_OTHER," ",budget_max_OTHER)
    print("ALL:    ",budget_all_min," ",budget_all_max)
    return result_min,result_max

@app.callback(
    Output("budgets","dataset_budgets"),
    Output("reachs","dataset_reachs"),
    Input("secilen_TV", "value"),
    Input("secilen_FB", "value"),
    Input("secilen_YT", "value"),
    Input("secilen_TIKTOK", "value"),
    Input("secilen_OTHER", "value"),
    Input("all_number", "dataset"),
    Input("target","dataset1"))

def budget_hesaplama(secilen_TV,secilen_FB,secilen_YT,secilen_TIKTOK,secilen_OTHER,dataset,dataset1):
    secilen_budgets_all=secilen_TV+secilen_FB+secilen_YT+secilen_TIKTOK+secilen_OTHER
    
#----------------------------------REACH TV ---------------------------------------------------------
    if data["TV Budget"][data["TV Budget"]==min(data["TV Budget"], key=lambda x:abs(x-secilen_TV))].index.nunique()>1:
        a=min(data["TV Budget"], key=lambda x:abs(x-secilen_TV))
        b=data["TV Budget"][data["TV Budget"]==a].index
        reach_TV=max(data["Reach@1+.2"][b])
    else:
        a=min(data["TV Budget"], key=lambda x:abs(x-secilen_TV))
        b=data["TV Budget"][data["TV Budget"]==a].index
        reach_TV=max(data["Reach@1+.2"][b])
    if data["Please select brand name"][data["Please select brand name"]==min(data["Please select brand name"], key=lambda x:abs(x-secilen_TV))].index.nunique()>1:
        a=min(data["Please select brand name"], key=lambda x:abs(x-secilen_TV))
        b=data["Please select brand name"][data["Please select brand name"]==a].index
        TV_grp=max(data["TV GRP"][b])
    else:
        a=min(data["Please select brand name"], key=lambda x:abs(x-secilen_TV))
        b=data["Please select brand name"][data["Please select brand name"]==a].index
        TV_grp=max(data["TV GRP"][b])
    a=db_TV["TVC:"][db_TV["TVC:"]==TV_grp].index
    a=a-19
    reach_TV2=dfconcat_reachs[dataset1[0]][dataset1[0]+reach_names[1]+dataset[0]].iloc[a].values[0]
    
#--------------------------------------------REACH FB ------------------------------------------------
    #facebook reach@1
    a=min(dfconcat_reachs_FB[dataset1[0]][dataset1[0]+"Budget"], key=lambda x:abs(x-secilen_FB))
    b=dfconcat_reachs_FB[dfconcat_reachs_FB[dataset1[0]][dataset1[0]+"Budget"]==a].index
    reach_FB=dfconcat_reachs_FB[dataset1[0]][dataset1[0]+"Reach@1+"][b].iloc[0]
    #facebook reach@2
    a=min(dfconcat_reachs_FB[dataset1[0]][dataset1[0]+"Budget"], key=lambda x:abs(x-secilen_FB))
    b=dfconcat_reachs_FB[dfconcat_reachs_FB[dataset1[0]][dataset1[0]+"Budget"]==a].index
    reach_FB2=dfconcat_reachs_FB[dataset1[0]][dataset1[0]+"Reach@2+"][b].iloc[0]
#--------------------------------------------REACH YT ------------------------------------------------
    #youtube reach@1
    a=min(dfconcat_reachs_YT[dataset1[0]][dataset1[0]+"Budget"], key=lambda x:abs(x-secilen_YT))
    b=dfconcat_reachs_YT[dfconcat_reachs_YT[dataset1[0]][dataset1[0]+"Budget"]==a].index
    reach_YT=dfconcat_reachs_YT[dataset1[0]][dataset1[0]+"Reach@1+"][b].iloc[0]
    #youtube reach@2
    a=min(dfconcat_reachs_YT[dataset1[0]][dataset1[0]+"Budget"], key=lambda x:abs(x-secilen_YT))
    b=dfconcat_reachs_YT[dfconcat_reachs_YT[dataset1[0]][dataset1[0]+"Budget"]==a].index
    reach_YT2=dfconcat_reachs_YT[dataset1[0]][dataset1[0]+"Reach@2+"][b].iloc[0]
#--------------------------------------------REACH TIKTOK ----------------------------------------------
    #tiktok reach@1
    a=min(data["Tiktok"], key=lambda x:abs(x-secilen_TIKTOK))
    b=data["Tiktok"][data["Tiktok"]==a].index
    reach_TIKTOK=data["Reach"][b].iloc[0]
    #tiktok reach@2
    a=min(data["Tiktok"], key=lambda x:abs(x-secilen_TIKTOK))
    b=data["Tiktok"][data["Tiktok"]==a].index
    reach_TIKTOK2=data["Please select brand nameReach@2+.3"][b].iloc[0]
#------------------------------------------------------------------------------------------------------  
    dataset_reachs=[reach_TV,reach_TV2,reach_FB,reach_FB2,reach_YT,reach_YT2,reach_TIKTOK,reach_TIKTOK2]
    print(dataset_reachs)
    dataset_budgets=[secilen_TV,secilen_FB,secilen_YT,secilen_TIKTOK,secilen_OTHER,secilen_budgets_all]
    return dataset_budgets,dataset_reachs

@app.callback(
    Output("bar", "figure"),
    Input("result_min", "result_min"),
    Input("budgets", "dataset_budgets"),
    Input("result_max", "result_max"))
def bar_chart(result_min,dataset_budgets,result_max):

    teams=["TV","Facebook","Youtube","TIKTOK","Other","Budget Overall"]
    df=pd.DataFrame({'result_min': result_min,
            'budgets': dataset_budgets,
                'result_max': result_max,
             },index=teams)
    
    fig1 = px.bar(df, x=teams, y=['result_min',"budgets","result_max"],barmode="group",
            color_discrete_map={'result_min':'#08306B', 'budgets':'#08519C', 'result_max':'#9ecae1'},
            labels={'value':'Investment',"x":"Medium","variable":"Budget"})


    return fig1
@app.callback(
    Output("bar2", "figure"),
    Input("reachs", "dataset_reachs"))
def bar_chart2(dataset_reachs):
    
    #fig2=ff.create_table([dataset_reachs], height_constant=60)
    teams=["TV_Reach1","TV_Reach2","Facebook_Reach1","Facebook_Reach2","Youtube_Reach1","Youtube_Reach2","TIKTOK_Reach1","TIKTOK_Reach2"]
    fig2 = px.bar(y=teams, x=dataset_reachs,barmode="group",orientation="h",
                 labels={'y':'Medium',"x":"Reachs"})
    return fig2

@app.callback(
    Output("pie2", "figure"),
    Input("reachs", "dataset_reachs"))
def pie_chart2(dataset_reachs):
    teams=["TV_Reach1","TV_Reach2","Facebook_Reach1","Facebook_Reach2","Youtube_Reach1","Youtube_Reach2","TIKTOK_Reach1","TIKTOK_Reach2"]
    fig4 = px.pie(values=dataset_reachs, names=teams, title='Reach %')
    return fig4



    #fig2=ff.create_table([dataset_reachs], height_constant=60)
    """
    trace2 = go.Bar(x=teams, y=dataset_reachs, xaxis='x2', yaxis='y2',
                marker=dict(color='#44fffc'),
                name='Girilen Budget')
    fig2.add_traces([trace2])

    fig2['layout']['xaxis2'] = {}
    fig2['layout']['yaxis2'] = {}
    fig2.layout.yaxis.update({'domain': [0, .45]})
    fig2.layout.yaxis2.update({'domain': [.6, 1]})

        # The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
    fig2.layout.yaxis2.update({'anchor': 'x2'})
    fig2.layout.xaxis2.update({'anchor': 'y2'})
    fig2.layout.yaxis2.update({'title': 'Budget'})

        # Update the margins to add a title and see graph x-labels.
    fig2.layout.margin.update({'t':75, 'l':50})
    fig2.layout.update({'title': 'Reachs'})

        # Update the height because adding a graph vertically will interact with
        # the plot height calculated for the table
    fig2.layout.update({'height':800})
    """

@app.callback(
    Output("gauge", "figure"),
    Input("result_min", "result_min"),
    Input("budgets", "dataset_budgets"),
    Input("result_max", "result_max"))
def gauge_chart(result_min,dataset_budgets,result_max):
    from plotly.subplots import make_subplots
    fig5 = make_subplots(
    rows=2, cols=3,
    specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}],
           [{"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],
    )
    if dataset_budgets[0]<=result_min[0]:
        abc=result_min[0]
    if (dataset_budgets[0]>result_min[0]) and (dataset_budgets[0]<=result_max[0]):
        abc=result_max[0]
    if dataset_budgets[0]>result_max[0]:
        abc=result_max[0]
    fig5.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = dataset_budgets[0],
        title = {'text': "TV"},
        delta = {'reference': abc},
        gauge = {'axis': {'range': [None, result_max[0]+result_min[0]]},
                 'bar': {'color': "orange"},
             'steps' : [
                 {'range': [0, result_min[0]], 'color': "lightgray"},
                 {'range': [result_min[0], result_max[0]], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': result_max[0]}},
        domain = {'row': 1, "column": 0}
    ),row=1, col=1)
    if dataset_budgets[1]<=result_min[1]:
        abc=result_min[1]
    if (dataset_budgets[1]>result_min[1]) and (dataset_budgets[1]<=result_max[1]):
        abc=result_max[1]
    if dataset_budgets[1]>result_max[1]:
        abc=result_max[1]
    fig5.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = dataset_budgets[1],
        title = {'text': "FACEBOOK"},
        delta = {'reference': abc},
        gauge = {'axis': {'range': [None, result_max[1]+result_min[1]]},
                 'bar': {'color': "orange"},
             'steps' : [
                 {'range': [0, result_min[1]], 'color': "lightgray"},
                 {'range': [result_min[1], result_max[1]], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': result_max[1]}},
        domain = {'row': 1, "column": 0}
    ),row=1, col=2)
    if dataset_budgets[2]<=result_min[2]:
        abc=result_min[2]
    if (dataset_budgets[2]>result_min[2]) and (dataset_budgets[2]<=result_max[2]):
        abc=result_max[2]
    if dataset_budgets[2]>result_max[2]:
        abc=result_max[2]
    fig5.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = dataset_budgets[2],
        title = {'text': "YOUTUBE"},
        delta = {'reference': abc},
        gauge = {'axis': {'range': [None, result_max[2]+result_min[2]]},
                 'bar': {'color': "orange"},
             'steps' : [
                 {'range': [0, result_min[2]], 'color': "lightgray"},
                 {'range': [result_min[2], result_max[2]], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': result_max[2]}},
        domain = {'row': 1, "column": 0}
    ),row=1, col=3)
    if dataset_budgets[3]<=result_min[3]:
        abc=result_min[3]
    if (dataset_budgets[3]>result_min[3]) and (dataset_budgets[3]<=result_max[3]):
        abc=result_max[3]
    if dataset_budgets[3]>result_max[3]:
        abc=result_max[3]
    fig5.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = dataset_budgets[3],
        title = {'text': "TIKTOK"},
        delta = {'reference': abc},
        gauge = {'axis': {'range': [None, result_max[3]+result_min[3]]},
                 'bar': {'color': "orange"},
             'steps' : [
                 {'range': [0, result_min[3]], 'color': "lightgray"},
                 {'range': [result_min[3], result_max[3]], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': result_max[3]}},
        domain = {'row': 1, "column": 0}
    ),row=2, col=1)
    if dataset_budgets[4]<=result_min[4]:
        abc=result_min[4]
    if (dataset_budgets[4]>result_min[4]) and (dataset_budgets[4]<=result_max[4]):
        abc=result_max[4]
    if dataset_budgets[4]>result_max[4]:
        abc=result_max[4]
    fig5.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = dataset_budgets[4],
        title = {'text': "OTHER"},
        delta = {'reference': abc},
        gauge = {'axis': {'range': [None, result_max[4]+result_min[4]]},
                 'bar': {'color': "orange"},
             'steps' : [
                 {'range': [0, result_min[4]], 'color': "lightgray"},
                 {'range': [result_min[4], result_max[4]], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': result_max[4]}},
        domain = {'row': 1, "column": 0}
    ),row=2, col=2)
    
    if dataset_budgets[5]<=result_min[5]:
        abc=result_min[5]
    if (dataset_budgets[5]>result_min[5]) and (dataset_budgets[5]<=result_max[5]):
        abc=result_max[5]
    if dataset_budgets[5]>result_max[5]:
        abc=result_max[5]
    fig5.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = dataset_budgets[5],
        title = {'text': "ALL"},
        delta = {'reference': abc},
        gauge = {'axis': {'range': [None, result_max[5]+result_min[5]]},
                 'bar': {'color': "orange"},
             'steps' : [
                 {'range': [0, result_min[5]], 'color': "lightgray"},
                 {'range': [result_min[5], result_max[5]], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': result_max[5]}},
        domain = {'row': 1, "column": 0}
    ),row=2, col=3)
    

    return fig5

#run app
if __name__=="__main__":
    app.run_server(debug=False)
