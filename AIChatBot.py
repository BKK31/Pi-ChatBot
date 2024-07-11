from flask import Flask, render_template, request, redirect, url_for
import os
import google.generativeai as Genai  # Not recommended for medical use
import PIL.Image
import json

DISCLAIMER = "WARNING: This website is for informational purposes only and should not be used for medical diagnosis or treatment. Always consult a medical professional for wound assessment and treatment."

api_key = "AIzaSyDPv_tQY79QMuf1lGEKmnLXprwp4XIa-Mk"
Genai.configure(api_key=api_key)

model = Genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=Genai.GenerationConfig(
        max_output_tokens=2048,
        temperature=0.7,
    ),
)

def analyze_wound_image(image_path):
    prompt = """
    This image contains a detailed view of a wound, cut, burn, or other injury. Based on what you see in the image, describe the wound or injury as thoroughly as possible. Make sure to note all observable features, including type, size, shape, depth, color, presence of any discharge, and surrounding tissue condition. Do keep in mind that the wounds may look healed, but are actually not.
    Additionally, based on the description, what would be the general first-aid treatment for the wound or injury?
    Return the output in JSON format:
    {
    "description": "description of the wound or injury",
    "features": ["feature1", "feature2", "feature3", ...],
    "first_aid": "first aid treatment for the wound or injury"
    }
    """

    response = model.generate_content([prompt, image_path])
    return response

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['image']
        if uploaded_file.filename != '':
            if uploaded_file.mimetype not in ['image/jpeg', 'image/jpg', 'image/png']:
                return redirect(url_for('upload_file', error="Only JPG and PNG images are allowed."))

            # Generate a unique filename and save the image
            filename = f"{os.urandom(10).hex()}.{uploaded_file.mimetype.split('/')[1]}"
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(image_path)

            # Analyze the image
            try:
                img = PIL.Image.open(image_path)
                response = analyze_wound_image(img)
                response_json = json.loads(response.text)
                description = response_json.get("description", "No description available")
                first_aid = response_json.get("first_aid", "No first aid information available")
                features = response_json.get("features", "No features available")

            except Exception as e:
                print(f"Error analyzing image: {e}")
                return redirect(url_for('upload_file', error="Error processing the image. Please try again."))

            output_json = {
                "description": description,
                "features": features,
                "first_aid": first_aid
            }

            return render_template('results.html', results=output_json, disclaimer=DISCLAIMER, uploaded_image_url=url_for('static', filename=filename))
        else:
            return redirect(url_for('upload_file', error="No image selected."))
    return render_template('upload.html', disclaimer=DISCLAIMER)

@app.route('/results.html')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
