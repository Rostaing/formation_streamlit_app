import streamlit as st
import pandas as pd
import time

# Texte d'affichage
st.header("Home")

st.write("Mon premier texte.")
st.write(["st", "is <", 3])
# st.write_stream(my_generator)
st.text("Fixed width text")
st.markdown("_Markdown_")
st.markdown("**Markdown**")
st.markdown("*Markdown*")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")

st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.html("<p>Hi!</p>")
st.html("<h1>Mon titre!</h1>")
st.html("<h6>Mon titre!</h6>")

# Afficher des widgets interactifs

st.button("Click me")
st.button("Valider")
# st.download_button("Download file", data)
# st.link_button("Go to gallery", url)
st.page_link("pages/about.py", label="Home")

data = "data/csv/population.csv"
df = pd.read_csv(data)
st.data_editor(df)

st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs", "Fruits", "Pomme"])
st.multiselect("Buy", ["milk", "apples", "potatoes", "Fruits", "Pomme"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.text_input("Nom complet")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")

# user_audio = st.audio_input("Record a voice message")
# st.audio(user_audio)

# user_image = st.camera_input("Take a picture")
# st.image(user_image)

st.color_picker("Pick a color")

#Afficher les données
d = "data/csv/ds_salaries.csv"
df1 = pd.read_csv(d)
data = st.dataframe(df1)
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)

# Affichage multimédia
# st.image("data/images/img4.webp")
# st.audio("data/audio/RostaingAI_Song.mp3")
# st.video("data/vidéo/data.mp4")
# st.logo("data/logo/logo.jpg")

# Afficher les graphiques
st.area_chart(df)

# Ajouter des éléments à la barre latérale
st.sidebar.radio("Select one:", [1, 2])

# Colonnes
# Two equal columns:
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# # Three different columns:
# col1, col2, col3 = st.columns([3, 1, 1])
# # col1 is larger.

# # Bottom-aligned columns
# col1, col2 = st.columns(2, vertical_alignment="bottom")

# # You can also use "with" notation:
# with col1:
#     st.radio("Select one:", [1, 2])

# Onglets
# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# Conteneurs extensibles

expand = st.expander("My label", icon=":material/info:")
expand.write("Inside the expander.")
pop = st.popover("Button label")
pop.checkbox("Show all")

# Afficher la progression et le statut
st.balloons()
st.snow()
st.toast("Warming up...")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")
# st.exception(e)

# Show a spinner during a process
# with st.spinner(text="In progress"):
#     time.sleep(10)
#     st.success("Done")

# Show and update progress bar
# bar = st.progress(50)
# time.sleep(10)
# bar.progress(100)