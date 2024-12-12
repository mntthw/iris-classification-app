Iris-Classification
===================
Dự án học máy dự đoán loài hoa Iris.

Bối Cảnh
========
Dữ liệu hoa Iris là một bộ dữ liệu đa biến được giới thiệu bởi nhà thống kê và nhà sinh học người Anh Ronald Fisher trong bài báo năm 1936 của ông, *The use of multiple measurements in taxonomic problems*. Dữ liệu này còn được gọi là bộ dữ liệu hoa Iris của Anderson vì Edgar Anderson đã thu thập dữ liệu này để đo lường sự biến động hình thái học của các loài hoa Iris thuộc ba loài liên quan.

Bộ dữ liệu bao gồm 50 mẫu từ mỗi loài hoa Iris (Iris Setosa, Iris Virginica và Iris Versicolor). Bốn đặc trưng được đo từ mỗi mẫu: chiều dài và chiều rộng của đài hoa và cánh hoa, tính bằng centimet.

Bộ dữ liệu này trở thành một bài toán điển hình cho nhiều kỹ thuật phân loại trong học máy, chẳng hạn như máy vector hỗ trợ (Support Vector Machine - SVM).

Nội Dung
========
Bộ dữ liệu gồm 150 mẫu, với 5 thuộc tính:
- Chiều dài cánh hoa
- Chiều rộng cánh hoa
- Chiều dài đài hoa
- Chiều rộng đài hoa
- Loại loài hoa (Species)

Mục tiêu của bộ dữ liệu là dự đoán loài hoa Iris dựa trên các giá trị của bốn đặc trưng trên.

Cảm Ơn
=======
Bộ dữ liệu này miễn phí và có sẵn công khai tại kho dữ liệu UCI Machine Learning Repository:
https://archive.ics.uci.edu/ml/datasets/Iris

Tổng Quan Dự Án
===============
Dự án này sử dụng học máy để phân loại ba loài hoa Iris bằng cách sử dụng mô hình Support Vector Machine (SVM). Các bước chính trong quy trình bao gồm:
1. Tải và chuẩn bị bộ dữ liệu Iris.
2. Tiền xử lý dữ liệu (ví dụ: mã hóa nhãn và chia dữ liệu thành tập huấn luyện và kiểm tra).
3. Huấn luyện mô hình SVM trên bộ dữ liệu.
4. Đánh giá độ chính xác của mô hình trên dữ liệu kiểm tra.
5. Lưu mô hình đã huấn luyện để sử dụng trong tương lai.

Các Bước Chạy Dự Án
==================
1. Cài đặt các thư viện yêu cầu ở requirements.txt
   - Cài đặt bằng lệnh pip install -r requirements.txt

2. Chuẩn bị bộ dữ liệu:
   - Có thể sử dụng bộ dữ liệu từ module `sklearn.datasets` hoặc tải bộ dữ liệu từ kho lưu trữ UCI và nạp vào bằng `pandas`.

3. Huấn luyện mô hình:
   - Sử dụng source code có sẵn để huấn luyện mô hình Support Vector Machine trên bộ dữ liệu.

4. Sử dụng mô hình:
   - Sau khi huấn luyện thì mô được lưu bằng `joblib` và tải lại mô hình để dự đoán trên dữ liệu mới.

