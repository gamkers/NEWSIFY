
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from bs4 import BeautifulSoup
import streamlit as st
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
    for i in range(1, 5):
        url = f"https://www.ndtv.com/world-news/page-{i}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('h2', class_="newsHdng")
        new = data.find_all('p', class_="newsCont")
        author = data.find_all('span', class_="posted-by")

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

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]





    return data






def webscrape_IndianNews(n):
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/latest/page-{i}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('h2', class_="newsHdng")
        new = data.find_all('p', class_="newsCont")
        author = data.find_all('span', class_="posted-by")

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

    for i in range(1, 5):
        url = f"https://www.ndtv.com/india/page-{i}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('h2', class_="newsHdng")
        new = data.find_all('p', class_="newsCont")
        author = data.find_all('span', class_="posted-by")

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

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data


def webscrape_SportsNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/sports"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

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

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data



def webscrape_musicNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/music"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Music")
        for m in author:
            country.append("World")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data




def webscrape_INPoliticalNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/indian-politics"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Indian Politics")
        for m in author:
            country.append("India")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data





def webscrape_GlobalPoliticalNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/politics"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Global Politics")
        for m in author:
            country.append("Global")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data






def webscrape_TechNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/tech"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Tech")
        for m in author:
            country.append("Global")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]
    return data






def webscrape_entertainmentNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/entertainment"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Entertainment")
        for m in author:
            country.append("Global")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data





def webscrape_lifestyleNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/life-style"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            elif len(j) == 1:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Life style")
        for m in author:
            country.append("Global")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data






def webscrape_CrimeNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/crime"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            elif len(j) == 1:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Crime")
        for m in author:
            country.append("Global")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]

    return data




def webscrape_businessNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/business"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            elif len(j) == 1:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("business")
        for m in author:
            country.append("Global")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]
    return data






def webscrape_foodNews():
    info = ["HEAD LINES", "NEWS", "AUTHOR", "DATE", "COUNTRY", "CATEGORY"]
    Date = []
    news = []
    authors = []
    catogory = []
    headlines = []
    country = []
    for i in range(1, 5):
        url = f"https://www.ndtv.com/page/topic-load-more/from/allnews/type/news/page/{i}/query/food"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        hl = data.find_all('div', class_="src_itm-ttl")
        new = data.find_all('div', class_="src_itm-txt")
        author = data.find_all('span', class_="src_itm-stx")

        for h in hl:
            headlines.append(h.text)
        for i in new:
            i = i.text
            news.append(i[25:-20])
        for j in author:
            j = j.text.split("|")
            if len(j) == 2:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            elif len(j) == 1:
                j = j[0]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j[25:])
            else:
                j = j[1]
                if "by" in j:
                    s = j.split("by")
                    j = s[-1]
                    authors.append(j)
                else:
                    authors.append(j)

        for k in author:
            k = k.text.split("|")
            k = k[-1]
            Date.append(k[:-20])
        for l in new:
            catogory.append("Food")
        for m in author:
            country.append("Global")

    data = [list(item) for item in list(zip(headlines, news, authors, Date, country, catogory))]
    return data








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
            st.write("[Project Link >](https://github.com/gamkers/NEWSIFY)")
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



    if "Global" in options:
        data=webscrape_GlobalNews()
        if submit:
            for i in data:
                for j in i:
                    if selected in j:
                        st.header(f'{i[0]}')

                        original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{i[1]}</p>'
                        st.markdown(original_title, unsafe_allow_html=True)
                        st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                        st.write("_______________________________________________________________________________")
                    break

        for i in range(n):
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)



            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")



    elif "LifeStyle" in options:
        data=webscrape_lifestyleNews()
        if submit:
            for i in data:
                for j in i:
                    if selected in j:
                        st.header(f' {i[0]}')

                        original_title = f'<p style="font-family:Times New Roman; color:black; font-size: 18px;">{i[1]}</p>'
                        st.markdown(original_title, unsafe_allow_html=True)

                        st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                        st.write("_______________________________________________________________________________")
                    break

        for i in range(n):
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman; font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")

    elif "Sports" in options:
        data=webscrape_SportsNews()
        if submit:
            for i in data:
                for j in i:
                    if selected in j:
                        st.header(f' {i[0]}')

                        original_title = f'<p style="font-family:Times New Roman; color:black; font-size: 18px;">{i[1]}</p>'
                        st.markdown(original_title, unsafe_allow_html=True)

                        st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                        st.write("_______________________________________________________________________________")
                    break

        for i in range(n):
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman; font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")


    elif "Political" in options:
        data=webscrape_INPoliticalNews()
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
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")

    elif "Crime" in options:

        data=webscrape_CrimeNews()
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
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")

    elif "Music" in options:
        data=webscrape_musicNews()
        if submit:
            for i in data:
                for j in i:
                    if selected in j:
                        st.header(f' {i[0]}')

                        original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{i[1]}</p>'
                        st.markdown(original_title, unsafe_allow_html=True)

                        st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                        st.write("_______________________________________________________________________________")
                    break

        for i in range(n):
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")

    elif "Technology" in options:
        data = webscrape_TechNews()
        if submit:
            for i in data:
                for j in i:
                    if selected in j:
                        st.header(f' {i[0]}')

                        original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{i[1]}</p>'
                        st.markdown(original_title, unsafe_allow_html=True)

                        st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                        st.write("_______________________________________________________________________________")
                    break

        for i in range(n):
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")

    elif "Food" in options:
        data = webscrape_foodNews()
        if submit:
            for i in data:
                for j in i:
                    if selected in j:
                        st.header(f' {i[0]}')

                        original_title = f'<p style="font-family:Times New Roman; color:black; font-size: 18px;">{i[1]}</p>'
                        st.markdown(original_title, unsafe_allow_html=True)

                        st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                        st.write("_______________________________________________________________________________")
                    break

        for i in range(n):
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")

    elif "Business" in options:
        data = webscrape_businessNews()
        if submit:
            for i in data:
                for j in i:
                    if selected in j:
                        st.header(f' {i[0]}')

                        original_title = f'<p style="font-family:Times New Roman;  font-size: 18px;">{i[1]}</p>'
                        st.markdown(original_title, unsafe_allow_html=True)

                        st.write(f'AUTHOR & DATE: {i[2]} | {i[3]}')
                        st.write("_______________________________________________________________________________")
                    break

        for i in range(n):
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman; font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")

    elif "Entertainment" in options:
        data = webscrape_entertainmentNews()
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
            st.header(f'{data[i][0]}')

            original_title = f'<p style="font-family:Times New Roman; font-size: 18px;">{data[i][1]}</p>'
            st.markdown(original_title, unsafe_allow_html=True)

            st.write(f'AUTHOR & DATE: {data[i][2]} | {data[i][3]}')
            st.write("_______________________________________________________________________________")









