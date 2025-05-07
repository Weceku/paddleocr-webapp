from flask import Flask, request, render_template
from PIL import Image
import os
import io
import base64
from paddleocr import PaddleOCR, draw_ocr
import paddle

app = Flask(__name__)
ocr = PaddleOCR(use_angle_cls=False, lang='japan', use_gpu=False)  # Initialize PaddleOCR, default language is Japanese

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    visualized_image = None
    recognized_text = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No file part'
        file = request.files['image']
        lang = request.form.get('lang', 'jpan')  # Get language parameter, default is 'japan'
        ocr.lang = lang # Set the language for OCR
        if file.filename == '':
            return 'No selected file'
        if file:
            img_bytes = file.read()
            img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
            image_path = "temp_image.png"
            img.save(image_path)

            result = ocr.ocr(image_path, cls=False)
            print("Raw OCR Result:", result)
            recognized_text_list = []
            if result and isinstance(result, list) and len(result) > 0:
                for item in result[0]: # Assuming result[0] contains the OCR results
                    if isinstance(item, list) and len(item) == 2:
                        bbox, recognition_info = item
                        if isinstance(recognition_info, tuple) and len(recognition_info) == 2 and isinstance(recognition_info[0], str):
                            recognized_text_list.append(recognition_info[0])
                        elif isinstance(recognition_info, str): # Handle cases where only text is returned (less common)
                            recognized_text_list.append(recognition_info)
                        else:
                            print(f"Warning: Unexpected recognition info: {recognition_info}")
                    else:
                        print(f"Warning: Unexpected item in result[0]: {item}")
            else:
                print("Warning: Result is empty or not a list")
            # Join recognized text into a single string
            recognized_text = "\n".join(recognized_text_list)

            # Visualization
            image = Image.open(image_path).convert('RGB')
            boxes = []
            txts = []
            scores = []
            if result and isinstance(result, list) and len(result) > 0:
                for item in result[0]:
                    if isinstance(item, list) and len(item) == 2:
                        bbox, recognition_info = item
                        if isinstance(bbox, list) and len(bbox) == 4 and all(isinstance(coord, list) and len(coord) == 2 and all(isinstance(c, (int, float)) for c in coord) for coord in bbox) and \
                        isinstance(recognition_info, tuple) and len(recognition_info) == 2 and isinstance(recognition_info[0], str) and isinstance(recognition_info[1], (int, float)):
                            boxes.append(bbox)
                            txts.append(recognition_info[0])
                            scores.append(recognition_info[1])
                        elif isinstance(bbox, list) and len(bbox) == 4 and all(isinstance(coord, list) and len(coord) == 2 and all(isinstance(c, (int, float)) for c in coord) for coord in bbox) and \
                            isinstance(recognition_info, str):
                            boxes.append(bbox)
                            txts.append(recognition_info)
            else:
                print("Warning: Result is empty or not a list for visualization")

            font_path = './fonts/simfang.ttf'
            if not os.path.exists(font_path):
                im_show = draw_ocr(image, boxes, txts, scores)
            else:
                im_show = draw_ocr(image, boxes, txts, scores, font_path=font_path)

            im_show = Image.fromarray(im_show)
            buffered = io.BytesIO()
            im_show.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            visualized_image = img_str

            os.remove(image_path)

    return render_template('Oindex(0.0.2).html', visualized_image=visualized_image, recognized_text=recognized_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5656)