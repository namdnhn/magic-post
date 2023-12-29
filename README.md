# magic-post
## Hướng dẫn cài đặt môi trường cho back-end
- Cần cài đặt Python sẵn trong máy (bản đang sử dụng: 3.10.11)
- Truy cập vào folder MagicPost-be trong project bằng lệnh ```cd MagicPost-be```, tạo một file .env có nội dung giống trong file .env example và sửa lại các thông tin tương ứng với máy của người dùng.
- Tạo môi trường ảo: ```python -m venv magic-post-env```
- Kích hoạt môi trường ảo:
  + Với Windows: ```magic-post-env\Scripts\activate```
  + Với MacOS và Linux: ```source head-hunter-env/bin/activate```
- Di chuyển ra thư mục gốc của dự án ```cd ..```
- Cài đặt các dependencies cho môi trường ảo: ```pip install -r requirements.txt```
- Di chuyển lại vào thư mục backend: ```cd MagicPost-be``` rồi chạy server trong local (di chuyển vào thư mục chứa file main.py): ```uvicorn main:app --reload```
- Khi không cần dùng môi trường ảo nữa, có thể tắt kích hoạt môi trường ảo: ```deactivate```
- Muốn test API, vui lòng sử dụng đường link: ```http://localhost:8000/docs```
## Hướng dẫn cài đặt môi trường cho front-end
- di chuyển vào thư mục front-end: ```cd MagicPost-fe```
- Cài đặt môi trường cho front-end: ```npm install```
- Chạy front-end: ```npm run dev -- --open```
