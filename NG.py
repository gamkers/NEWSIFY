
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from bs4 import BeautifulSoup
import streamlit as st
from gtts import gTTS
from io import BytesIO


def speak(text):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang='en')
    tts.write_to_fp(mp3_fp)
    return mp3_fp




st.set_page_config(page_title="NEWSIFY", page_icon=":tada:", layout='wide')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden; }
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


def webscrape_GlobalNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    images = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/world-news/page-{i}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('h2', class_="newsHdng")
        new = data.find_all('p', class_="newsCont")
        author = data.find_all('span', class_="posted-by")
        image = data.find_all('img', class_="img_brd marr10")
        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text.replace("\n", "")
            news.append(i)
        for j in author:
            j = j.text.split("|")
            j = j[0]
            if "by" in j:
                s = j.split("by")
                j = s[-1]
            authors.append(j[:-3])
        for k in author:
            k = k.text.split("|")
            k = k[-1]
            k = k.split(",")
            if len(k) == 2:
                Date.append(",".join(k[0:2])[:-112])
            else:
                Date.append(",".join(k[0:2]))
        for l in new:
            catogory.append("Global")
        for m in author:
            m = m.text.split("|")
            m = m[-1]
            m = m.split(",")
            m = m[-1]
            country.append(m[:-112].replace("2022", "NA"))
        for im in image:
            link = im.get('src')
            images.append(link)

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory,images))]





    return data






def webscrape_IndianNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    images=[]
    for i in range(1, 5):
        url = f"https://www.ndtv.com/latest/page-{i}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('h2', class_="newsHdng")
        new = data.find_all('p', class_="newsCont")
        author = data.find_all('span', class_="posted-by")
        image = data.find_all('img', class_="img_brd marr10")
        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text.replace("\n", "")
            news.append(i)
        for j in author:
            j = j.text.split("|")
            j = j[0]
            if "by" in j:
                s = j.split("by")
                j = s[-1]
            authors.append(j[:-3])
        for k in author:
            k = k.text.split("|")
            k = k[-1]
            k = k.split(",")
            if len(k) == 2:
                Date.append(",".join(k[0:2])[:-112])
            else:
                Date.append(",".join(k[0:2]))
        for l in new:
            catogory.append("Indan")
        for m in author:
            m = m.text.split("|")
            m = m[-1]
            m = m.split(",")
            m = m[-1]
            country.append(m[:-112].replace("2022", "NA"))
        for im in image:
            link = im.get('src')
            images.append(link)

    for i in range(1, 5):
        url = f"https://www.ndtv.com/india/page-{i}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('h2', class_="newsHdng")
        new = data.find_all('p', class_="newsCont")
        author = data.find_all('span', class_="posted-by")
        image = data.find_all('img', class_="img_brd marr10")
        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text.replace("\n", "")
            news.append(i)
        for j in author:
            j = j.text.split("|")
            j = j[0]
            if "by" in j:
                s = j.split("by")
                j = s[-1]
            authors.append(j[:-3])
        for k in author:
            k = k.text.split("|")
            k = k[-1]
            k = k.split(",")
            if len(k) == 2:
                Date.append(",".join(k[0:2])[:-112])
            else:
                Date.append(",".join(k[0:2]))
        for l in new:
            catogory.append("Indan")
        for m in author:
            m = m.text.split("|")
            m = m[-1]
            m = m.split(",")
            m = m[-1]
            country.append(m[:-112].replace("2022", "NA"))

        for im in image:
            link = im.get('src')
            images.append(link)

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory,images))]

    return data


def webscrape_News(cat,n):
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    images=[]
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/{cat}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")
        image =data.find_all('img', class_="img_brd marr10")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            j = j[0]
            if "by" in j:
                s = j.split("by")
                j = s[-1]
                authors.append(j)
            else:
                authors.append(j[25:])
        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Sports")
        for m in author:
            country.append("India")
        for im in image:
            link = im.get('src')
            images.append(link)

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory,images))]

    return data


def display(data):
    voice = []
    for i in range(5):
        data1 = data[i][1].split(";")
        voice.append(f"news number{str(i + 1)}," + data1[0] + '.')
    audio_bytes = speak('.'.join(map(str, voice)))
    st.audio(audio_bytes, format='audio/ogg')
    if submit:
        for i in data:
            for j in i:
                if selected in j:
                    st.header(f' {i[0]}')

                    original_title = f'<p style="font-family:Times New Roman; font-size: 18px;">{i[1]}</p>'
                    st.markdown(original_title, unsafe_allow_html=True)

                    st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                    st.write("_______________________________________________________________________________")
                break

    for i in range(n):
        data1 = data[i][0].split(";")
        st.header(f'{data1[0]}')
        with st.container():
            left_coloumn, right_coloumn = st.columns(2)
            with left_coloumn:
                st.image(data[i][6], width=355)
            with right_coloumn:
                st.write("                                                                                ")
                st.write("                                                                                ")
                original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')

        st.write("_______________________________________________________________________________")




selected2 = option_menu(None, ["Home", "Search", 'Developers'],
                        icons=['house', 'search', 'people'],
                        menu_icon="cast", default_index=0, orientation="horizontal")



def lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = lottieurl("https://assets8.lottiefiles.com/packages/lf20_qmfs6c3i.json")
lottie_coding2 = lottieurl("https://assets8.lottiefiles.com/packages/lf20_2LdLki.json")
lottie_coding3 = lottieurl("https://assets8.lottiefiles.com/packages/lf20_oyi9a28g.json")


if selected2 == 'Home':
    with st.container():
        st.write("---")
        left_coloumn, right_coloumn = st.columns(2)
        with left_coloumn:
            st.subheader("North East West South all in one Place")
            st.title("NEWSIFY")
            st.write(
                "NEWSIFY is Web-Based Application, helps users to find News Articles related to multiple categories like Sports,Technologies,political,Global,lifestyle,etc and We fully depends upon our own Machine learning model which categorise news from Realtime DataSet which is a well optimized dataset extracted from internet, We Provides you a best in class news from all over the WORLD")
            st.write("[Project Link >](https://github.com/gamkers/STUDENTBAE)")
        with right_coloumn:
            st_lottie(lottie_coding, height=500, key="DEVELOPERS")

    with st.container():
        st.write("---")
        left_coloumn, right_coloumn = st.columns(2)
        with left_coloumn:
            st_lottie(lottie_coding2, height=400, key="STUDENTS")

        with right_coloumn:
            st.header("WHY NEWSIFY?")
            st.write("##")
            st.write(
                """
                Nowadays NEWS companies develop a model which manipulated data for their gains. 
                so we developed our own model and feed our model with the well- optimized dataset. 
                we create our dataset by extracting data which are already segregated by multiple companies 
                and performing tasks like  data cleaning, Data mining, features engineering, NLP, sentiment analysis, 
                Feature selection and so and so... every time we feed our model it learns from the different dataset 
                and provides accurate and meaningful data to user""")




elif selected2 == 'Developers':

    with st.container():
        st.write("---")
        left_coloumn, right_coloumn = st.columns(2)
        with left_coloumn:

            st.header("DEVELOPERS")
            st.subheader("AKASH M")
            st.write("B.Tech CSE")
            st.subheader("Surendharan TG")
            st.write("B.Tech CSE")
            st.subheader("SUDHA SIRISHA K")
            st.write("B.Tech CSE")
        with right_coloumn:
            st_lottie(lottie_coding3, height=400, key="DEVELOPERS")
elif selected2 == "Search":
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    def remote_css(url):
        st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


    def icon(icon_name):
        st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


    local_css("style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    st.header("Explore The World")
    form = st.form(key='my-form')
    selected = form.text_input("", "")
    submit = form.form_submit_button("SEARCH")


    options = st.multiselect(
        'What you Looking for?',
        ['Sports', 'Political', 'Technology', 'Music', 'Global', 'LifeStyle', "Entertainment", 'Crime', 'Food', 'Business']
        )

    n = st.slider('News Count', 0, 130, 25)


    if submit:
        data = webscrape_News(selected,n)
        voice=[]
        for i in range(n):
            data1 = data[i][0].split(":")
            voice.append(f"news number{str(i + 1)}," + data1[0] + '.')
        audio_bytes = speak('.'.join(map(str, voice)))
        st.audio(audio_bytes, format='audio/ogg')
        for i in range(n):
            data1 = data[i][0].split(":")
            st.header(f'{data1[0]}')
            with st.container():
                left_coloumn, right_coloumn = st.columns(2)
                with left_coloumn:
                    st.image(data[i][6],width=355)
                with right_coloumn:
                    st.write("                                                                                ")
                    st.write("                                                                                ")
                    original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
                    st.markdown(original_title, unsafe_allow_html=True)
                    st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')

            st.write("_______________________________________________________________________________")



    if "Global" in options:
        data=webscrape_GlobalNews()
        display(data)

    elif "LifeStyle" in options:
        data=webscrape_News("life-style",n)
        display(data)
    elif "Sports" in options:
        data=webscrape_News("Sports",n)
        display(data)
    elif "Political" in options:
        data=webscrape_News("politics",n)
        display(data)
    elif "Crime" in options:

        data=webscrape_News("crime",n)
        display(data)
    elif "Music" in options:
        data=webscrape_News("music",n)
        display(data)
    elif "Technology" in options:
        data = webscrape_News("technology",n)
        display(data)

    elif "Food" in options:
        data = webscrape_News("food",n)
        display(data)
    elif "Business" in options:
        data = webscrape_News("business",n)
        display(data)
    elif "Entertainment" in options:
        data = webscrape_News("entertainment",n)
        display(data)







