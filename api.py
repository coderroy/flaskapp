import flask
from flask import Flask
from flask import Flask, render_template,request




app = Flask(__name__)
outarray=[]

@app.route("/")
@app.route("/index")


def index():
   return flask.render_template('index.html')


def do_prediction(file):		#function to do predictions.
	model = joblib.load('pune_model.sav')
	input1 = pd.read_csv(file)
	X = input1.drop(['Clear sky GHI','Date_UnixTimeStamp','TimeSunRise_UnixTimeStamp','TimeSunSet_UnixTimeStamp'] , axis=1).as_matrix()
	inputmatrix = xgb.DMatrix(X)
	outarray=model.predict(inputmatrix)
	df = pd.DataFrame(outarray)
	df.to_csv("Predictions.csv")
		


@app.route('/predict', methods=['POST'])
def make_prediction():
   if request.method=='POST':
      file = request.files['inputfile']
#      do_prediction(file)
      return render_template('index.html', label=" Output Saved to Predictions.csv File")


if __name__ == '__main__':
		app.run(host='0.0.0.0', port=8000, debug=True)
		app.static_folder = 'static'		# defining static folder to use images js css
