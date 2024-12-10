from flask import Flask, render_template, request, redirect, url_for
import joblib as jlb

iris_names = ['Iris_setosa', 'Iris_versicolor', 'Iris_virginica']
app = Flask(__name__)
model = jlb.load('iris_model')  # Tải mô hình đã được huấn luyện từ tệp iris_models 

@app.route('/')
def home():
    return render_template('index.html')  # Kết nối Flask với HTML, gửi HTML về trình duyệt

@app.route('/result', methods=['POST'])
def result():
    try:
        result = request.form.to_dict()

        field_mapping = {
            'Sepal_length': 'Chiều dài đài hoa',
            'Sepal_width': 'Chiều rộng đài hoa',
            'petal_length': 'Chiều dài cánh hoa',
            'petal_width': 'Chiều rộng cánh hoa',
        }

        # Tạo dữ liệu hiển thị (chuyển key thành tiếng Việt)
        display_data = {field_mapping.get(k, k): v for k, v in result.items() if k != 'btn'}

        # Dự đoán
        sl = float(request.form['Sepal_length'])
        sw = float(request.form['Sepal_width'])
        pl = float(request.form['petal_length'])
        pw = float(request.form['petal_width'])
        data = [sl, sw, pl, pw]
        pre = model.predict([data])
        res = iris_names[pre[0]]

        # Gửi dữ liệu dự đoán và các giá trị nhập liệu trở lại giao diện kết quả
        return render_template('result.html', title='Result', result=display_data, predicted=res)
    except:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
