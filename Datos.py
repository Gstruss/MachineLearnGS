# Hecho por Geoffrey

import requests, json
class Capture:
    def obtener_datos():
        url = "https://www.datos.gov.co/resource/m5pi-7cau.json"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return
        data = response.json()
        if data:
            for item in data:
                print(f"{item['proveedor']}")
                print("----------")
        else:
            print("No data found")

    obtener_datos()