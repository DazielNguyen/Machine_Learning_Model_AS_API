# Deploy Model qua API (Private) 

*Mình sẽ hướng dẫn các bạn chạy thử phần này, mình chạy trên hệ điều hành MacOS*

## Bật Terminal trên VS 

Chạy lệnh sau: 

- Tải môi trường: **brew install python@3.13**
- Tạo môi trường: **python3 -m venv ml-env** (ml-env là tên môi trường bạn có thể đặt tên khác cũng được)
- Kích hoạt môi trường: **source ml-env/bin/activate**
- Sau đó chạy server Uvicorn: uvicorn ml_api:app
  + Sau khi chạy xong nó sẽ xuất hiện: URL
- Copy URL đó thay vào URL trong file api_implementation.py 
- Trong file này: **api_implementation.py**
  + Bạn có thế thay đổi số liệu rồi chạy hết file thì nó sẽ trả về kết quả bạn có bị tiểu đường hay không.


