
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load the JSON data from a file
with open('cards.json', 'r') as f:
    json_data = json.load(f)

@app.route('/cards', methods=['GET'])
def get_cards():
    parallel_filter = request.args.get('parallel')
    keyword = request.args.get('keyword')
    rarity_filter = request.args.get('rarity')
    name_filter = request.args.get('name')
    subtype_filter = request.args.get('subtype')
    
    filtered_data = json_data
    
    if parallel_filter:
        filtered_data = [card for card in filtered_data if card.get('Parallel') == parallel_filter]
    
    if rarity_filter:
        filtered_data = [card for card in filtered_data if card.get('Rarity') == rarity_filter]
        
    if name_filter:
        filtered_data = [card for card in filtered_data if name_filter.lower() in card.get('Card', '').lower()]
        
    if subtype_filter:
        filtered_data = [card for card in filtered_data if card.get('Subtype') == subtype_filter]
    
    if keyword:
        filtered_data = [card for card in filtered_data if keyword.lower() in card.get('Text', '').lower()]
    
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
