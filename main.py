from polygon import RESTClient
from flask import Flask, url_for, render_template, request
from polygon_api_handler import PolygonAPIHandler

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "yan"
    return app

app = create_app()
key = "i3lqYgb9p3cDmAxwmOmRvOSSF5ucaXIe"
polygon_handler = PolygonAPIHandler(key)

@app.route("/home", methods = ["POST", "GET"])
def home():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        stock_name = request.form.get("name")
        try:
            previous_close_data = polygon_handler.get_previous_close(stock_name.upper())[0]
            return render_template("index.html", name = "Stock Name: "+ stock_name.upper(), open_price="Open Price (Previous Close): "+ str(previous_close_data['o']), close_price = "Close Price (Previous Close): "+str(previous_close_data['c']), highest_price = "Highest Price (Previous Close): "+str(previous_close_data['h']))
        except:
            return render_template("index.html", name="Enter a valid stock")
            

        

if __name__ == '__main__':
    app.run(debug=True)