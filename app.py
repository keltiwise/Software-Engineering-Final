from flask import Flask, render_template, request
import collections
collections.MutableSequence = collections.abc.MutableSequence
collections.Iterable = collections.abc.Iterable
from flask_navigation import Navigation
from azuresqlconnector import *
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Database', 'information'), 
    nav.Item('Write A Review', 'review'), 
    nav.Item('Chat', 'chat'), 
    nav.Item('About', 'about')
])

@app.route('/') 
def index():
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()

    sql_query = """SELECT BarName, Longitude, Latitude, PositiveRatings, NegativeRatings FROM FinalProjectOne.TableOne"""
    cursor.execute(sql_query)
    records = cursor.fetchall()
    cursor.close()
    return render_template('home.html', records = records)

@app.route('/database')
def information():
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()

    sql_query = """SELECT BarID, Latitude, Longitude, BarName, PositiveRatings, NegativeRatings FROM FinalProjectOne.TableOne"""
    cursor.execute(sql_query)
    records = cursor.fetchall()
    cursor.close()
    return render_template('database.html', records = records)

@app.route('/database', methods=['POST']) 
def information_home(): 
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'delete':
            bar_id = request.form.get('BarID')
            conn = SQLConnection()
            conn = conn.getConnection()
            cursor = conn.cursor()
            delete_query = """DELETE FROM FinalProjectOne.TableOne WHERE BarID = ?"""
            cursor.execute(delete_query, (bar_id,))
            conn.commit()
            cursor.close()
            return "Entry deleted successfully"
        
        elif action == 'add':
            conn = SQLConnection()
            conn = conn.getConnection()
            cursor = conn.cursor()
            query = "SELECT BarID FROM FinalProjectOne.TableOne"
            cursor.execute(query)
            existing_ids = cursor.fetchall()
            used_ids = set(id[0] for id in existing_ids if id[0] is not None)
            
            bar_id = 1
            while bar_id in used_ids:
                bar_id += 1
            
            Latitude = request.form.get('Latitude')
            Longitude = request.form.get('Longitude')
            BarName = request.form.get('BarName')
            
            insert_query = """INSERT INTO FinalProjectOne.TableOne (BarID, Latitude, Longitude, BarName, PositiveRatings, NegativeRatings) VALUES (?, ?, ?, ?, 0, 0)"""
            cursor.execute(insert_query, (bar_id, Latitude, Longitude, BarName))
            conn.commit()
            cursor.close()
            return "Entry added successfully"

        
        elif action == 'update':
            barID = request.form.get('BarID')
            latitude = request.form.get('Latitude')
            longitude = request.form.get('Longitude')
            barName = request.form.get('BarName')
            positive = request.form.get('PositveRatings')
            negative = request.form.get('NegativeRatings')

            conn = SQLConnection()
            conn = conn.getConnection()
            cursor = conn.cursor()
            update_query = """UPDATE FinalProjectOne.TableOne SET Latitude=?, Longitude=?, BarName = ?, PositiveRatings = ?, NegativeRatings = ? WHERE BarID=?"""
            cursor.execute(update_query, (float(latitude), float(longitude), barName, positive, negative, barID))
            conn.commit()
            cursor.close()
            return "Entry updated successfully"


@app.route('/review', methods=['GET', 'POST'])
def review():
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT BarID, BarName FROM FinalProjectOne.TableOne")
    bars = cursor.fetchall()
    
    return render_template('review.html', bars=bars)

@app.route('/chat') 
def chat(): 
    conn = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()

    sql_query = """SELECT ChatID, Chat FROM FinalProjectTwo.TableTwo"""
    cursor.execute(sql_query)
    records = cursor.fetchall()
    cursor.close()
    return render_template('chat.html', records = records)

@app.route('/chat', methods=['POST']) 
def chat_home(): 
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'add':
            conn = SQLConnection()
            conn = conn.getConnection()
            cursor = conn.cursor()
            
            query = "SELECT ChatID FROM FinalProjectTwo.TableTwo"
            cursor.execute(query)
            existing_ids = cursor.fetchall()
            used_ids = set(id[0] for id in existing_ids if id[0] is not None)
            
            chat_id = 1
            while chat_id in used_ids:
                chat_id += 1
            
            Chat = request.form.get('Chat')
            
            insert_query = """INSERT INTO FinalProjectTwo.TableTwo (ChatID, Chat) VALUES (?, ?)"""  
            cursor.execute(insert_query, (chat_id, Chat))
            conn.commit()
            cursor.close()
            
            return "Entry added successfully"
        
        elif action == 'delete':
            chat_id = request.form.get('ChatID')

            conn = SQLConnection()
            conn = conn.getConnection()
            cursor = conn.cursor()
            delete_query = """DELETE FROM FinalProjectTwo.TableTwo WHERE ChatID = ?"""
            cursor.execute(delete_query, (chat_id,))
            conn.commit()
            cursor.close()
            return "Entry deleted successfully"


# Azure text analytics key and endpoint
endpoint = "https://languagewisekelti.cognitiveservices.azure.com/"
key = "ce17be8ef4a44851b26070386b4dbb71"
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

@app.route('/review', methods = ['GET', 'POST'])
def review(): 
    conn = = SQLConnection()
    conn = conn.getConnection()
    cursor = conn.cursor()

    cursor.execute("SELECT BarID, BarName FROM FinalProjectOne.TableOne")
    bars = cursor.fetchall()

    if request.method == 'POST':
        bar_id = request.form.get('bar_id')
        review_text = request.form.get('review_text')

        # Analyze sentiment of the review
        response = text_analytics_client.analyze_sentiment(review_text)
        sentiment = response[0].sentiment

        # Adding to positive and negative
        if sentiment == "positive":
            update_query = """
            UPDATE FinalProjectOne.TableOne
            SET PositiveRatings = PostiveRatings + 1
            WHERE BarID = ?
            """
        elif sentiment == "negative":
            update_query = """
            UPDATE FinalProjectOne.TableOne
            SET NegativeRatings = NegativeRatings + 1
            WHERE BarID = ?
            """
        else:
            pass

        cursor.execute(update_query, (BarID,))
        conn.commit()

        # Store the review and sentiment in the database
        insert_query = """
        INSERT INTO FinalProjectOne.Reviews (BarID, ReviewText, Sentiment)
        VALUES (?, ?, ?)
        """
        cursor.execute(insert_query, (bar_id, review_text, sentiment))
        conn.commit()

        return "Review submitted successfully"

    return render_template('review.html', bars = bars)

@app.route('/about') 
def about(): 
    return render_template('about.html')

if __name__ == '__main__': 
    app.run()
