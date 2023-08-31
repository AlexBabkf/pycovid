from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')

@app.route('/europe-timeline')
def europe_timeline():
    
    fig = px.choropleth(df, locations='Country', locationmode='country names', color='Confirmed', animation_frame='Date', scope='europe')
    fig.update_layout(title='Map of confirmed until today', template='plotly_dark')
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

@app.route('/world-timeline')
def world_timeline():
    
    fig = px.choropleth(df,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date')
    fig.update_layout(title='Choropleth Map of Confirmed Cases -till today',template="plotly_dark")
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

if __name__ == '__main__':
    app.run(debug=True)



