from flask import Flask,jsonify,request

app=Flask(__name__)
List=[
    {
        'id':1,
        'name':"Raju",
        'contact':"9987644456"
        'done':false
    },
    {
        'id':2,
        'name':"Rahul",
        'contact':"9876543222"
        'done':false
    }
]
@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            'status':"error",
            'message':"please provide the data"
        },400)
    contact={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':false
    }
    List.append(contact)
    return jsonify({
        'status':"success",
        'message':"contact added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        'data':List
    })

if __name__=='__main__':
    app.run()