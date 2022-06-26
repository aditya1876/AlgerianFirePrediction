from flask import Flask, request, jsonify
import logging
import prediction
import sklearn
logging.basicConfig(filename = "Alg_flask.log", level = logging.DEBUG, format ='%(asctime)s >> %(levelname)s >> %(message)s')


app = Flask(__name__)

logging.info("Flask app started!!")

@app.route('/', methods=['GET','POST'])
def home_page():
    logging.info("Home page loaded...")
    return "Hello World!"

# API routes-- single predict Temperature
@app.route('/api/temp_single', methods=['POST'])
def single_predict():
    try:
        if (request.method=='POST'):
            logging.info("1")
            #temp=request.json["Temperature"]
            rh=float(request.json["RH"])
            ws=float(request.json["Ws"])
            rain=float(request.json["Rain"])
            ffmc=float(request.json["FFMC"])
            dmc=float(request.json["DMC"])
            dc=float(request.json["DC"])
            isi=float(request.json['ISI'])
            fwi=float(request.json["FWI"])
            classes=request.json["Classes"] #fire or not_fire
            if classes=='fire':
                class_code=1
            elif classes=='not_fire':
                class_code=0
            else:
                raise Exception("Sorry, only 'fire' and 'not_fire' allowed")
            logging.info("2")
            #prepare the payload to send to model for prediction
            payload=[rh,ws,rain,ffmc,dmc,dc,isi,fwi,class_code]
            logging.info("3")
            #call the prediction function
            result=prediction.predictTemp(payload)
            logging.info("4")
            #return result to API
            return jsonify(result.tolist())
        else:
            raise Exception("Sorry, please provide parameters correctly.")
    except Exception as e:
        logging.exception("Exception while reading data from api request: /api/temp_single :"+str(e))
    
    return jsonify(result.tolist())

# API routes-- single predict Classes
@app.route('/api/class_single', methods=['POST'])
def single_predict_class():
    try:
        if (request.method=='POST'):
            temp=float(request.json["Temperature"])
            rh=float(request.json["RH"])
            ws=float(request.json["Ws"])
            rain=float(request.json["Rain"])
            ffmc=float(request.json["FFMC"])
            dmc=float(request.json["DMC"])
            dc=float(request.json["DC"])
            isi=float(request.json['ISI'])
            fwi=float(request.json["FWI"])
    except Exception as e:
        logging.exception("Exception while reading data from api request: /api/temp_single :"+str(e))
    
    #prepare the payload to send to model for prediction
    payload=[temp,rh,ws,rain,ffmc,dmc,dc,isi,fwi]

    #call the prediction function
    result=prediction.predictClasses(payload)
    
    #return result to API
    return jsonify(result.tolist())



if __name__== '__main__':
    app.run(debug=True)
