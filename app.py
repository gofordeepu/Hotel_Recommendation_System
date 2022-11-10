from flask import Flask , render_template,request
import pandas as pd
app=Flask(__name__)
# Function to recommend hotels
def based_on_city(city):
    hotel_data=pd.read_csv('datasets/hotel_data.csv')
    hotel_data['city']=hotel_data['city'].str.lower()
    matched_city=hotel_data[hotel_data['city']==city.lower()]
    matched_city=matched_city.sort_values(by='starrating',ascending=False)
    if matched_city.empty==False:
        data=matched_city.iloc[:,[5,3,2,6,7,8,4,9]]
        count=data.shape[0]
        return data.to_html(index=False),count
    else:
        return "",0
        print("No Hotel Found!")



# routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result",methods=['GET','POST'])
def result():
    if request.method=='POST':
        data,count=based_on_city(request.form['city'])
        return render_template("result.html",data=data,data_count=count)
    else:
        return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


# code execution
if __name__=="__main__":
    app.run(debug=True)
