import json
import numpy as np


actions = [
    'hello', 'thanks', 'iloveyou', 'Help', 'All Done', 'Please',
    'More', 'Good', 'Happy', 'Sad', 'Sleep', 'Drink', 'Eat', 'Cheese',
    'Cookie', 'Spoon', 'Apple', 'Bed', 'Blanket', 'Diaper', 'Music',
    'Book', 'Doll', 'Balloon', 'Hat', 'Jacket', 'Pacifier', 'Mommy',
    'Daddy', 'Grandma', 'Grandpa', 'Brother', 'Sister', 'Baby', 'Rain',
    'Cat', 'Dog', 'House', 'Store', 'Car', 'Stroller', 'Hug', 'kiss', 'Cold', 'Pain'
    'open', 'close', 'cry', 'play', 'stop', 'go', 'laugh'
]

json.dump(actions, open("labels/actions.json", "w"))