from flask import Flask, render_template, request, jsonify
import script
app = Flask("IndiTranslate")
@app.route('/')
def index():
    return render_template("index.html")  
@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text')
    target_language = request.form.get('target_language')
    if not text or not target_language:
        return jsonify({'error': 'Missing input'}), 400
    translated_text = script.process_data(text, target_language)   
    return jsonify({'translated_text': translated_text})  
if __name__ == '__main__':
    app.run(debug=True)
