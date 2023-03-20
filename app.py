import flask
from flask import Flask, request, render_template, url_for, send_file , Response, jsonify
import fitz
import json
from flask import request as req
import os
import pandas as pd
import numpy as np
from gtts import gTTS
from bs4 import BeautifulSoup
import requests
import io
import speech_recognition as sr
import pyttsx3
from io import BytesIO
from fpdf import FPDF
import re
from langdetect import detect
import pathlib
import requests
from flask import Flask, session, abort, redirect, request , render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import pdfsplitter
import hindiSummary
import predictCategory
import english_textRank
import pdf_repo
# import summary_using_BART
import enchant
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter, landscape
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
from fpdf import FPDF, HTMLMixin


# BART_PATH = 'model/bart-large'

app = Flask(__name__)

app.secret_key = "CodeSpecialist.com"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "434837932139-dueupt66ll82dlianr43a14d4nf9qvjv.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


### Working ###

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    return render_template('login.html')



@app.route("/protected_area")
@login_is_required
def protected_area():
    return render_template('index.html')

### End ###



# upload pdf text
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        # get the uploaded PDF file
        uploaded_file = request.files['file']

        filename, file_extension = os.path.splitext(uploaded_file.filename)
        print(filename)
        print(file_extension)
        if file_extension.lower() == '.txt':
            # read the content of the text file
            text = uploaded_file.read().decode('utf-8')

            # return the text to the HTML page
            return render_template('index.html', text=text)

        # if the uploaded file is a PDF file, extract the text
        elif file_extension.lower() == '.pdf':
            # open the PDF file using PyMuPDF
            pdf_document = fitz.open(stream=uploaded_file.read(), filetype='pdf')

            # extract the text from each page
            text = ''
            for page in pdf_document:
                text += page.get_text()

            # close the PDF file
            pdf_document.close()
            # return the extracted text to the HTML page
            return render_template('index.html', text=text)

    # if the request method is GET, return the HTML page
    return "There is an error in the file upload."

# API
def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()



### Prediction

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sentence = request.json['input_text']
        num_words = request.json['num_words']
        num_beams = request.json['num_beams']
        model = request.json['model']

        lan = detect(sentence)
        Result = '***Not Available, Try English Text***'

        if lan == 'en':
            # Split the text into lines
            lines = sentence.split('\n')
            # Remove the empty spaces in each line
            processed_lines = [line.strip() for line in lines if line.strip()]
            # Join the lines together without spaces
            output_text = ''.join(processed_lines)
            # print(output_text)

            if model.lower() == 'bart':
                # output = summary_using_BART.bart_summarize(output_text, num_beams, num_words)
                output = ''

            elif model.lower() == 'fast-summary':

                data = str(output_text)
                maxL = int(num_words)
                maxL = maxL
                minL = maxL//2
                output = query({
                    "inputs": data,
                    "parameters": {"min_length": minL, "max_length": maxL},
                })[0]["summary_text"]

            elif model.lower() == 'text-rank':
                top_n = int(num_beams)
                output = english_textRank.textRank_summary(sentence, top_n)
            else:
                output = "Wrong Summarization Model: Try some other Models"
                app.logger.error('Requested Summarization Model not Exist: , ❌ERROR❌')

            Result = predictCategory.categoryPredict(sentence)

        elif lan == 'hi':
            # if model.lower() == 'bart':
            sample = sentence
            clean_sentences = hindiSummary.get_clean_sentences(sample)
            best_sentences, textrank_scores = hindiSummary.summarize(clean_sentences, percentage=0.4)
            summary_textrank = hindiSummary.generate_summary_textrank(clean_sentences, best_sentences)
            output = summary_textrank
                # pass
        else:
            model="Alien"
            output = "Language not supported"
            response = {}
            response['response'] = {
                'summary': "News Category:" + "   " + lan + os.linesep + os.linesep + "Summary:" + os.linesep + "   " + str(
                    output),
                'category': lan,
                'model': model.lower()
            }
            app.logger.error('Language not supported: , ❌ERROR❌ lan')
            return flask.jsonify(response)


        response = {}
        response['response'] = {
            'summary': "Language:" + "   " + lan + os.linesep +"News Category:" + "   " + Result + os.linesep + os.linesep + "Summary:" + os.linesep + "   " + str(
                output),
            'category': Result,
            'model': model.lower()
        }
        app.logger.info('Requested for Summary+Category: , 🎉🎉🎉Done')
        return flask.jsonify(response)

    except Exception as ex:
        res = dict({'message': str(ex)})
        print(res)
        app.logger.error('Requested for Exception: , 🎉🎉🎉Done')
        return app.response_class(response=json.dumps(res), status=500, mimetype='application/json')


@app.route("/speak", methods=["POST"])
def speak():
    url = request.form["url"]
    summary_text = request.form["summary_text"]

    # create text-to-speech audio file
    tts = gTTS(text=summary_text, lang='en')
    tts_file = f"{os.urandom(16).hex()}.mp3"  # generate unique filename
    tts.save(tts_file)
    app.logger.info('Requested for download: , 🎉🎉🎉Done')

    # read audio file as binary data and delete the file
    with open(tts_file, 'rb') as f:
        app.logger.info('Requested for Speak: , 🎉🎉🎉Done')
        audio_data = f.read()
    os.remove(tts_file)

    # send binary data to client for playback
    return send_file(io.BytesIO(audio_data), mimetype="audio/mpeg")



@app.route('/download', methods=['POST'])
def download_summary():
    summary = request.form['summary']
    format = request.form['format']
    if format == 'txt':
        response = Response(summary, mimetype='text/plain')
        response.headers['Content-Disposition'] = 'attachment; filename=summary.txt'
        app.logger.info('Requested for .txt file download , 🎉🎉🎉Done')
    elif format == 'pdf':
        pdf_report = pdf_repo.PDFReport(summary)
        pdf_report.build_report()
        data = io.BytesIO(pdf_report.output(dest='S').encode('latin1'))
        mimetype = 'application/pdf'
        extension = 'pdf'
        app.logger.info('Requested for .pdf file download, Done')

        app.logger.info('Requested for .pdf file download , 🎉🎉🎉Done')
    else:
        return 'Invalid format', 400
        app.logger.error('Invalid format : Error 400')
    data.seek(0)
    return Response(data, mimetype=mimetype, headers={
        'Content-Disposition': 'attachment; filename=summary.' + extension
    })


### pdf splitter......

@app.route("/splitpdf")
def upload():
    return render_template("file_upload.html")


@app.route("/splitpdf/success",methods=["POST"])
def success():
    success.start_page=int(request.form['start'])
    success.end_page=int(request.form['end'])
    f=request.files['file']
    success.file_name=f.filename
    f.save(success.file_name)
    return render_template("success.html",start=success.start_page, end=success.end_page,name=success.file_name)

@app.route("/splitpdf/convert")
def cropper():
    pdfsplitter.cropper(success.start_page,success.end_page,success.file_name)
    return render_template("download.html")



@app.route("/splitpdf/download")
def download():
    filename=success.file_name.split(".")[0]+"cropped.pdf"
    return send_file(filename,as_attachment=True)

### spel Checker and Recommender

@app.route('/speldetect', methods=['POST'])
def speldetect():
    data = request.form['data']
    # Create an instance of enchant dictionary for English language
    d = enchant.Dict("en_US")
    suggestions = {}
    for word in data.split():
        # Check if word is misspelled
        if not d.check(word):
            # Get a list of suggestions for the misspelled word
            word_suggestions = d.suggest(word)
            suggestions[word] = word_suggestions
    return jsonify(suggestions)



if __name__ == '__main__':
    app.run(debug=True)
