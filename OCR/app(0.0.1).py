from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# # HTML Modle
# HTML_TEMPLATE = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>OCR Web App</title>
# </head>
# <body>
#     <h1>Tesseract OCR</h1>
#     <form method="POST" enctype="multipart/form-data">
#         <input type="file" name="image" required>
#         <input type="submit" value="submit">
#     </form>
#     {% if recognized_text %}
#     <h2>Result:</h2>
#     <pre>{{ recognized_text }}</pre>
#     {% endif %}
# </body>
# </html>
# """   

def perform_ocr(image_path, lang='eng+jpn'):
    """
    对指定路径的图像进行 OCR 识别。

    Args:
        image_path (str): 图像文件的路径。
        lang (str): 识别的语言。

    Returns:
        str: 识别出的文本。
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except FileNotFoundError:
        return f"错误：找不到图像文件 '{image_path}'"
    except Exception as e:
        return f"OCR 识别过程中发生错误：{e}"


# Flask 路由
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    recognized_text = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No file part'
        file = request.files['image']
        if file.filename == '':
            return 'No selected file'
        if file:
            # 保存上传的图片
            image_path = os.path.join('uploads', file.filename)
            os.makedirs('uploads', exist_ok=True)
            file.save(image_path)
            # 进行 OCR 识别
            recognized_text = perform_ocr(image_path)
            # 删除临时保存的图片
            os.remove(image_path)
    return render_template('index(0.0.2).html', recognized_text=recognized_text)

if __name__ == '__main__':
    app.run(debug=True)