from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    hadith_data = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-abudawud.json')
    hadiths = json.loads(hadith_data.content)
    hadith = random.choice(hadiths['hadiths'])
    
    verse = random.randint(1, 6236)
    quran_translation_data = requests.get(f'http://api.alquran.cloud/v1/ayah/{verse}/en.asad')
    quran_english_verse = json.loads(quran_translation_data.content)
    
    quran_arabic_data = requests.get(f'http://api.alquran.cloud/v1/ayah/{verse}')
    quran_arabic_verse = json.loads(quran_arabic_data.content)
    

    print(quran_english_verse['data']['surah']['number'], quran_english_verse['data']['numberInSurah'])
    return render_template('index.html',  data1=hadith, data2=quran_english_verse, data3 = quran_arabic_verse)