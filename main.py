import base64
import json
import os
import base64
import json
import os

def formatJson():

    input_file = 'data/input.json'
    output_file = 'Data/input.json'

    with open(input_file, 'r') as file:
        data = file.read()
    json_data = '[' + data + ']'

    with open(output_file, 'w') as file:
        file.write(json_data)
    print(f'{output_file} dosyasına veriler başarıyla yazıldı.')

def SaveImages(image_list, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, image_data in enumerate(image_list):
        image_bytes = base64.b64decode(image_data)
        image_path = os.path.join(output_folder, f'image_{index + 1}.png')

        with open(image_path, 'wb') as image_file:
            image_file.write(image_bytes)
    print("Dosyalar kaydedildi...")

formatJson()
with open('Data/input.json', 'r') as jsonFile:
    JsonData = json.load(jsonFile)

print(JsonData)

Images = [item['Img'] for item in JsonData if 'Img' in item]
if Images:
    output_folder = 'Data/Images'  # Klasör yolunu burada belirtiyoruz
    SaveImages(Images, output_folder)
else:
    print("JSON dosyasından 'Img' verisi alınamadı.")

