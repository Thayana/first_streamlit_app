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
streamlit.dataframe(my_fruit_list)


