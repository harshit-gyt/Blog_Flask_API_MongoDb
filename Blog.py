from flask import *
import pymongo

myclient = pymongo.MongoClient("localhost")
mydb = myclient["Blog_Database"]
mycol = mydb["Blog_collection"]

#mycol.delete_many({})
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('adduser.html')


@app.route("/GET")
def get():
    l1=[]
    user=mycol.find()
    for x in user:
        user_dict = {"name" : x['name'], "email":x['email'], "blog":x['blog'] }
        l1.append(user_dict)
    return {"UserInfo": l1}



@app.route("/POST", methods=['POST'])
def post_user():
    uname = request.form['uname']
    email = request.form['email']
    blog = request.form['blog']

    user1 = {"name": uname, "email": email , "blog": blog}
    mycol.insert_one(user1)

    return redirect("/GET")


@app.route("/DELETE/<string:name>")
def delete_user(name):
    uname = name
    query={"name":uname}
    mycol.delete_one(query)

    return redirect("/GET")


if __name__=="__main__":
    app.run(debug=True)




