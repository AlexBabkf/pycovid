from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')

@app.route('/europe-timeline')
def europe_timeline():
    
    fig = px.choropleth(df, locations='Country', locationmode='country names', color='Confirmed', animation_frame='Date', scope='europe')
    fig.update_layout(title='Choropleth Map of Confirmed Cases - Europe', template='plotly_dark')
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

@app.route('/world-timeline')
def world_timeline():
    
    fig = px.choropleth(df,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date')
    fig.update_layout(title='Choropleth Map of Confirmed Cases - World',template="plotly_dark")
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

@app.route('/asia-timeline')
def asia_timeline():
    
    fig = px.choropleth(df,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date',scope='asia')
    fig.update_layout(title='Choropleth Map of Confirmed Cases - Asia',template="plotly_dark")
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

@app.route('/scatterplot')
def scatterplot():
    
    fig = px.scatter_geo(df,locations='Country',locationmode='country names',color='Confirmed',size='Confirmed',hover_name="Country",animation_frame='Date',title='Spread over Time')
    fig.update(layout_coloraxis_showscale=False,layout_template="plotly_dark")
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

@app.route('/choro-recovered')
def choro_recovered():
    
    fig = px.choropleth(df,locations='Country',locationmode='country names',color='Recovered',animation_frame='Date')
    fig.update_layout(title='Choropleth Map of Recovered Cases ',template="plotly_dark")
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

@app.route('/scatter-recovered')
def scatter_recovered():
    
    fig = px.scatter_geo(df,locations='Country',locationmode='country names',color='Recovered',size='Recovered',hover_name="Country",animation_frame='Date',title='Recovery over Time')
    fig.update(layout_coloraxis_showscale=False,layout_template="plotly_dark")
    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

if __name__ == '__main__':
    app.run(debug=True)



