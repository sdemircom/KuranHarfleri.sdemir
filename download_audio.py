import os
import urllib.request
import urllib.parse
import time

harfler = [
    'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي'
]

# Ensure audio directory exists
os.makedirs('audio', exist_ok=True)

# Google Translate TTS might block simple urllib requests without User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for i, harf in enumerate(harfler):
    filename = f'audio/{i+1}.mp3'
    if not os.path.exists(filename):
        encoded_harf = urllib.parse.quote(harf)
        url = f'https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q={encoded_harf}'
        
        req = urllib.request.Request(url, headers=headers)
        
        try:
            with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
                out_file.write(response.read())
            print(f'Downloaded {filename} for {harf}')
        except Exception as e:
            print(f'Failed to download {filename} for {harf}: {e}')
        
        time.sleep(1) # Be nice to Google's servers
    else:
        print(f'{filename} already exists.')

print("All downloads finished.")
