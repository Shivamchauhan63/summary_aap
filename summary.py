import streamlit
import wikipedia as shivam

import streamlit as str

streamlit.title('Shivam Chauhan This Side') # es ku run karne se phale terminal par jaa ke ( streamlit run file name ) run kar le

topic = streamlit.text_input("Search anything")
click = streamlit.button( 'Search Shivam' )

if click == True :
    recsult = shivam.summary(topic)
    streamlit.write(recsult)

