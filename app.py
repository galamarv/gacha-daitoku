from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Define hadiah (prizes) and their associated probabilities for each set
hadiah_sets = {
    'set1': ["1 Sticker", "2 Sticker","1 Poster", "2 Poster","Ride Chemy / Ganbaride Card","Astro Switch", 
    "Kyutama", "Toq Ressha / ranger key / Sentai gear", "Progrise key / Sofubi Ultra Monster ", "little figure kamen rider saber and revice"],
    'set2': ["1 Sticker + 1 Ride Chemy / Ganbaride Card", "2 Sticker + Ride Chemy / Ganbaride Card","1 Poster + Ride Chemy / Ganbaride Card", "2 Poster + Ride Chemy / Ganbaride Card",
             "Astro Switch", "Kyutama", "Toq Ressha / ranger key / Sentai gear", "Progrise key / Sofubi Ultra Monster / ridewatch", "little figure kamen rider saber and revice",  "Bima S Figures"],
    'set3': ["1 gantungan kunci ", " 1 kyutama / astro switch","1 Ride Chemy / Ganbaride Card + 1 gantungan kunci ", 
             " 1 Ride Chemy / Ganbaride Card + kyutama / astro switch", " 2 Astro Switch", "2 Kyutama", "Toq Ressha / ranger key / Sentai gear", 
             "Progrise key / Sofubi Ultra Monster / ridewatch", "little figure kamen rider saber and revice",  "Bima S Figures", "Ultraman Dyna Macaho armor"],
    'set4': ["gold kamen rider saber", "progrise key", "Raise buckle", "Kamen Rider Genm figure", "Ultraman Sofvi (Ginga / Victory)"],
    'set5': ["Entry Grade Kamen Rider Zero ONe", "Tamashii nations box"],
    'set6': ["1 Sticker", "2 Sticker", "1 Poster", "2 Poster", "Ride Chemy / Ganbaride Card", "Wizard Ring", 
             "Kyutama", "Ultra Vehicle Series/ Toq Ressha / ranger key", "Bima S Figures / Ultra Sofubi /New Boy chara kid / gold kamen rider saber / progrise key", 
             "Raise buckle / Kamen Rider Genm figure / Ultraman Sofvi (Ginga / Victory)", "Entry Grade Kamen Rider Zero ONe / Tamashii nations box "]
}

probabilities_sets = {
    'set1': [0.20, 0.20, 0.20, 0.15, 0.10, 0.05, 0.05, 0.03, 0.015, 0.005],
    'set2': [0.20, 0.20, 0.20, 0.10, 0.10, 0.10, 0.05, 0.03, 0.015, 0.005],
    'set3': [0.20, 0.20, 0.15, 0.15, 0.075, 0.075, 0.05, 0.05, 0.03, 0.018, 0.002],
    'set4': [0.2, 0.2, 0.15, 0.15, 0.1],
    'set5': [0.5, 0.5],
    'set6': [0.20, 0.20, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.008, 0.002]
}

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML file

@app.route('/gacha', methods=['POST'])
def gacha():
    set_key = request.form.get('set_key')
    number_of_results = int(request.form.get('number_of_results', 1))

    if set_key not in hadiah_sets:
        return jsonify(error="Invalid set key"), 400

    hadiah = hadiah_sets[set_key]
    probabilities = probabilities_sets[set_key]

    # Generate random choices based on the number of results requested
    gacha_result = np.random.choice(hadiah, number_of_results, p=probabilities).tolist()
    
    return jsonify(gacha_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
