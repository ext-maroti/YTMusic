from ytmusicapi import YTMusic 

from flask import Flask, jsonify
ytmusic = YTMusic()

app = Flask(__name__)

@app.route('/')
def hello_world():
    get_charts = ytmusic.get_charts(country="IN")
    return get_charts


if __name__ == '__main__':
    app.run(port=5000)
# ytmusic = YTMusic()


# # browse = ytmusic.get_home()
# # print(browse)
 

# # mood_categories = ytmusic.get_mood_categories()
# # print(mood_categories) 


# get_charts = ytmusic.get_charts(country="IN")
# print(get_charts)
# def writeToJsonFile(path,fileName,data):
#     filePathName = "./"+path+'/'+fileName+'.json'
#     with open(filePathName, 'w') as f:
#         json.dump(data, f)



# path="./"
# fileName="explore"

# data = get_charts

# writeToJsonFile(path,fileName,data)

 # search_results = ytmusic.search("Oasis Wonderwall")
  #  category_results = ytmusic.get_mood_categories()
  #  explore_results = YTMusic.get_charts( self ,country = "ISO 3166-1 Alpha-2 IN")
       