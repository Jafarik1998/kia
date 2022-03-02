# -*- coding: utf-8 -*-
"""


@author: Kasi
"""

import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module

def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)

def generate_html_download_link(fig):
    # Credit Plotly: https://discuss.streamlit.io/t/download-plotly-plot-as-html/4426/2
    towrite = StringIO()
    fig.write_html(towrite, include_plotlyjs="cdn")
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Download Plot</a>'
    return st.markdown(href, unsafe_allow_html=True)


st.set_page_config(page_title='Kiarash')
st.title('Kia Plotter 📈')
st.subheader('Upload your Excel file')

uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
        'برای کدام متغیر می‌خواهید نمودار رسم کنید؟',
        ('جنسيت', 'وضعيت تاهل', 'تعداد فرزند', 'وضعيت خدمت', 'دليل معافيت', 'شهر محل سكونت', 'نوع محل سكونت', 'گروه خوني', 'وضعيت', 'نام بانك', 'استخدام', 'مكان استقرار', 'نام واحد', 'گروه شغلي', 'واحد سرپرست', 'نوع مدرك', 'رشته تحصيلي', 'حوزه فعاليت', 'مليت'),
    )

    # -- GROUP DATAFRAME
    df_grouped = df.groupby(by=[groupby_column], as_index=False).value_counts()
   
    
    # -- PLOT DATAFRAME 
    fig_h = px.histogram(df_grouped, x=groupby_column)
    fig_p = px.pie(df_grouped, names=groupby_column)

    st.plotly_chart(fig_h)
    st.plotly_chart(fig_p)

    
if uploaded_file:
   df = pd.read_excel(uploaded_file, engine='openpyxl')
      
   button = st.radio(
     "کدام متغیرها را می‌خواهید انتخاب کنید؟",

       ('جنسيت', 'وضعيت تاهل', 'تعداد فرزند', 'وضعيت خدمت', 'دليل معافيت', 'شهر محل سكونت', 'نوع محل سكونت', 'گروه خوني', 'وضعيت', 'نام بانك', 'استخدام', 'مكان استقرار', 'نام واحد', 'گروه شغلي', 'واحد سرپرست', 'نوع مدرك', 'رشته تحصيلي', 'حوزه فعاليت', 'مليت'),
  )  
   dff = df[button].unique()
   list1 = dff.tolist()

   
   if button == "جنسيت":
       b1 = st.radio("جنسیت را انتخاب کنید", (list1))  
   
   elif  button == "وضعيت تاهل":
       b1 = st.radio("وضعيت تاهل را انتخاب کنید", (list1))  
       
   elif  button == "تعداد فرزند":
       b1 = st.radio("تعداد فرزند را انتخاب کنید", (list1))
       
   elif  button == "وضعيت خدمت":
       b1 = st.radio("وضعيت خدمت را انتخاب کنید", (list1))
  
   elif button == "دليل معافيت":
       b1 = st.radio("دليل معافيت را انتخاب کنید", (list1))  
   
   elif button == "شهر محل سكونت":
       b1 = st.radio("شهر محل سكونت را انتخاب کنید", (list1))  
   
   elif button == "نوع محل سكونت":
       b1 = st.radio("نوع محل سكونت را انتخاب کنید", (list1))  
   
   elif button == "گروه خوني":
       b1 = st.radio("گروه خوني را انتخاب کنید", (list1))  
  
   elif button == "وضعيت":
       b1 = st.radio("وضعيت را انتخاب کنید", (list1))  
  
   elif button == "نام بانك":
       b1 = st.radio("نام بانك را انتخاب کنید", (list1))  
   
   elif button == "استخدام":
       b1 = st.radio("استخدام را انتخاب کنید", (list1))  
   
   elif button == "مكان استقرار":
       b1 = st.radio("مكان استقرار را انتخاب کنید", (list1))  
      
   elif button == "نام واحد":
       b1 = st.radio("نام واحد را انتخاب کنید", (list1))  
  
   elif button == "گروه شغلي":
       b1 = st.radio("گروه شغلي را انتخاب کنید", (list1))  
   
   elif button == "واحد سرپرست":
       b1 = st.radio("واحد سرپرست را انتخاب کنید", (list1))  
   
   elif button == "نوع مدرك":
       b1 = st.radio("نوع مدرك را انتخاب کنید", (list1))  
   
   elif button == "رشته تحصيلي":
       b1 = st.radio("رشته تحصيلي را انتخاب کنید", (list1))  
   
   elif button == "حوزه فعاليت":
       b1 = st.radio("حوزه فعاليت را انتخاب کنید", (list1))  
   
   elif button == "مليت":
       b1 = st.radio("مليت را انتخاب کنید", (list1))  
                      

if uploaded_file:
   df = pd.read_excel(uploaded_file, engine='openpyxl')
      
   button2 = st.radio(
     "کدام متغیرها را در لایه‌ی دوم می‌خواهید انتخاب کنید؟",

       ('جنسيت', 'وضعيت تاهل', 'تعداد فرزند', 'وضعيت خدمت', 'دليل معافيت', 'شهر محل سكونت', 'نوع محل سكونت', 'گروه خوني', 'وضعيت', 'نام بانك', 'استخدام', 'مكان استقرار', 'نام واحد', 'گروه شغلي', 'واحد سرپرست', 'نوع مدرك', 'رشته تحصيلي', 'حوزه فعاليت', 'مليت'),
  )  
  
   df_var = df.loc[df[button] == b1]
   
   df_var2 = df_var.groupby(by=[button2], as_index=False).value_counts()
   #df_var2 = df_var.loc[df_var[button2] == b2]
   st.write(df_var2)

   fig_h2 = px.histogram(df_var2, x=button2)
   fig_p2 = px.pie(df_var2, names=button2)

   st.plotly_chart(fig_h2)
   st.plotly_chart(fig_p2)
   
    # -- DOWNLOAD SECTION
   st.subheader('Downloads:')
   generate_excel_download_link(df_var2)
   
