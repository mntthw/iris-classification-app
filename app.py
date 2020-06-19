from flask import*

import joblib as jlb
iris_names=['Iris_setosa' ,'Iris_versicolor' ,'Iris_virginica']
app=Flask(__name__)
model=jlb.load('iris_model')

#pre=model.predict([[1,2,1,1]])
#print(iris_names[pre[0]])

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/result',methods=['POST'])
def result():
	try:
		result=request.form
		sl=float(request.form['Sepal_length'])
		sw=float(request.form['Sepal_width'])
		pl=float(request.form['petal_length'])
		pw=float(request.form['petal_width'])
		data=[sl,sw,pl,pw]	
		pre=model.predict([data])
		res=iris_names[pre[0]]
		return render_template('result.html',title='Result',result=result,predicted=res)
	except:
		return redirect(url_for('home'))
if(__name__=='__main__'):
	app.run(debug=True)
