import requests
import os

def download_images_from_api(search_query, download_path, per_page=10, total_images=30):
    access_key = ''  # Ganti dengan Pixabay Access Key Anda
    total_downloaded = 0
    page = 1

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    while total_downloaded < total_images:
        url = f"https://pixabay.com/api/?key={access_key}&q={search_query}&per_page={per_page}&page={page}"
        response = requests.get(url)
        data = response.json()

        for idx, photo in enumerate(data['hits']):
            if total_downloaded >= total_images:
                break
            img_url = photo['webformatURL']
            img_name = f"image_{total_downloaded + 1}.jpg"
            img_path = os.path.join(download_path, img_name)
            with open(img_path, 'wb') as img_file:
                img_file.write(requests.get(img_url).content)
            print(f"Downloaded: {img_name}")
            total_downloaded += 1

        page += 1

if __name__ == "__main__":
    search_query = "husky"
    download_path = "husky2"
    download_images_from_api(search_query, download_path, total_images=200)  # Ubah total image sesuai keinginan Anda
