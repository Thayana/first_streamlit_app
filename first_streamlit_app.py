import streamlit
streamlit.title(" My Parents are heathy diner")
streamlit.header("🥗 Breakfast Menu")
streamlit.text("🥣 Rice")
streamlit.text("🥗 Avocado Toast")
streamlit.text("🐔 Omega Fish")
streamlit.text("🥑kale,Spinach")
streamlit.text("🍞french fries")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacoda','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


