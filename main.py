#/Users/yukinkmr07/Library/Python/3.8/bin/streamlit
import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'


st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#option = st.text_input('あなたの趣味を教えてください。')
#'あなたの趣味：',option
#condition = st.slider('あなたの今の調子は？',0,100,50)#(から,まで,最初)
# 'コンディション：',condition

#if st.checkbox('Show Image'):
#    img = Image.open('sample.png')
#    st.image(img, caption = '偏差値', use_column_width=True)

#st.selectbox(
#    'あなたの好きな数字を教えてください、',
#    list(range(1,11))
#)

#option = st.text_input('あなたの趣味を教えてください。')
#'あなたの趣味：',option
#condition = st.slider('あなたの今の調子は？',0,100,50)#(から,まで,最初)
#'コンディション：',condition


#st.title('Stremlit 超入門')

#st.write('Display Image')

#df = pd.DataFrame(
#   np.random.rand(100, 2)/[50,50] + [35.69,139.70],
# 
#  columns=['lat','lon']
#)
#st.map(df)#マッピング

#st.bar_chart(df) #棒グラフ

#st.area_chart(df) #領域グラフ

# st.line_chart(df) #折れ線グラフ

#st.table(df.style.highlight_max(axis=0))  #staticな表
#st.dataframe(df)  #interactiveな表

"""
# 章
## 説
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

