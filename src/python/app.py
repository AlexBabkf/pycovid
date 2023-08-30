from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def get_visualization():
    df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
    fig = px.choropleth(df, locations='Country', locationmode='country names', color='Confirmed', animation_frame='Date', scope='europe')
    fig.update_layout(title='Map of confirmed until today', template='plotly_dark')

    fig_html = fig.to_html(full_html=False)

    return render_template('visualization.html', visualization=fig_html)

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, jsonify
# import pandas as pd
# import plotly.express as px
# import folium
# import geopy
# from geopy.geocoders import Nominatim


# app = Flask(__name__)

# @app.route('/')
# def get_visualization_data():
#     df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
#     # df2 = df.groupby(['Country'])[['Confirmed', 'Recovered', 'Deaths']].max().reset_index()
#     # geolocator = Nominatim(user_agent='app')
#     # lat_lon = []
#     # for location in df2["Country"]:
#     #     location = geolocator.geocode(location)
#     #     if location is None:
#     #         lat_lon.append(np.nan)
#     #     else:
#     #          geo=(location.latitude, location.longitude)
#     #          lat_lon.append(geo)
    
#     # df2['geo_loc'] = lat_lon
#     # df2[['lat', 'lon']] = df2['geo_loc'].apply(lambda x: pd.Series(x))
#     # df2.dropna(inplace=True)
    
#     # m = folium.Map(location=[54, 15], tiles='openstreetmap', zoom_start=2)
#     # for id, row in df2.iterrows():
#     #     folium.Marker(location=[row['lat'], row['lon']], popup = f"Confirmed: {row['Confirmed']} Recovered: {row['Recovered']} Deaths: {row['Deaths']}").add_to(m)

    
#     fig = px.choropleth(df, locations='Country', locationmode='country names', color='Confirmed', animation_frame='Date', scope='europe')
#     fig.update_layout(title='Map of confirmed until today', template='plotly_dark')
#     return jsonify(fig.to_json())

# if __name__ == '__main__':
#     app.run(debug=True)
