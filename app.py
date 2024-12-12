from flask import Flask, render_template, request, redirect, url_for
import joblib as jlb

# Danh sách tên các loại hoa Iris
iris_names = ['Iris_setosa', 'Iris_versicolor', 'Iris_virginica']

app = Flask(__name__)

# Tải mô hình đã được huấn luyện từ file "iris_model"
model = jlb.load('iris_model')

# Trang chủ của ứng dụng
@app.route('/')
def home():
    # Kết nối Flask với file HTML (index.html) và trả về giao diện cho người dùng
    return render_template('index.html')

# Xử lý kết quả khi người dùng gửi thông tin
@app.route('/result', methods=['POST'])
def result():
    try:
        # Lấy dữ liệu từ form được gửi bởi người dùng
        result = request.form.to_dict()

        # Mapping các trường dữ liệu từ tiếng Anh sang tiếng Việt để hiển thị
        field_mapping = {
            'Sepal_length': 'Chiều dài đài hoa',
            'Sepal_width': 'Chiều rộng đài hoa',
            'petal_length': 'Chiều dài cánh hoa',
            'petal_width': 'Chiều rộng cánh hoa',
        }

        # Chuyển đổi key trong dữ liệu sang tiếng Việt
        display_data = {field_mapping.get(k, k): v for k, v in result.items() if k != 'btn'}

        # Xử lý dữ liệu đầu vào từ người dùng (chuyển sang dạng float)
        sl = float(request.form['Sepal_length'])  # Chiều dài đài hoa
        sw = float(request.form['Sepal_width'])   # Chiều rộng đài hoa
        pl = float(request.form['petal_length'])  # Chiều dài cánh hoa
        pw = float(request.form['petal_width'])   # Chiều rộng cánh hoa
        data = [sl, sw, pl, pw]  # Dữ liệu đầu vào dưới dạng danh sách

        # Dự đoán loại hoa dựa trên dữ liệu đầu vào
        pre = model.predict([data])  # Gọi mô hình để dự đoán
        res = iris_names[pre[0]]  # Lấy tên loại hoa từ danh sách dựa trên kết quả dự đoán

        # Hiển thị kết quả dự đoán và dữ liệu đầu vào cho người dùng trên trang kết quả
        return render_template('result.html', title='Result', result=display_data, predicted=res)
    except:
        # Nếu có lỗi xảy ra, quay lại trang chủ
        return redirect(url_for('home'))

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)  # Chế độ debug giúp kiểm tra lỗi trong quá trình phát triển
