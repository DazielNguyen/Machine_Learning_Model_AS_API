# Deploy Model qua API (Private) 

*Mình sẽ hướng dẫn các bạn chạy thử phần này, mình chạy trên hệ điều hành MacOS*

## Bật Terminal trên VS 

Chạy lệnh sau: 

- Tải môi trường: **brew install python@3.13**
- Tạo môi trường: **python3 -m venv ml-env** (ml-env là tên môi trường bạn có thể đặt tên khác cũng được)
- Kích hoạt môi trường: **source ml-env/bin/activate**
- Bạn tải tất cả thư viện mình để sẵn trong file requirements.txt : **pip install -r requirements.txt**
- Sau đó chạy server Uvicorn: **uvicorn ml_api:app**
  + Sau khi chạy xong nó sẽ xuất hiện: URL
- Copy URL đó thay vào URL trong file api_implementation.py 
- Trong file này: **api_implementation.py**
  + Bạn có thế thay đổi số liệu rồi chạy hết file thì nó sẽ trả về kết quả bạn có bị tiểu đường hay không.
### Mình tham khảo và học từ Video sau:
[https://www.youtube.com/watch?v=EUWLdW_i0EQ&list=PLfFghEzKVmjuCMQqnONUX6N72RoJq4MSY&index=2]

**Troubleshooting của mình trong video sau:**

- Trong video sử dụng python3.8 -> Phiên bản này đã dừng và không cung cấp tải 
- Vì trong Python3.8 thì bạn mới dùng được Pickle5 (Pickle5 chỉ dùng được cho phiên bản dưới 3.8)
- Mình đã thử tải phiên bản khác thấp hơn nhưng nó sẽ bị lỗi Numpy (No module named 'numpy._core')
  + Mình đã thay thế Pickle5 bằng joblib và có thể load được model.
