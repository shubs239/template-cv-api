import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("DIGITAL_FAUCON_API_KEY")
RUNWARE_API_URL = "https://api.runware.ai/v1"

# Replace with a PUBLIC URL to your image
SEED_IMAGE_URL = "img.jpeg"  # ← MUST be public HTTPS URL

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = [
  {
    "taskType": "imageInference",
    "taskUUID":str(uuid.uuid4()),
    "numberResults": 1,
    "outputFormat": "WEBP",
    "width": 1344,
    "height": 768,
    "steps": 8,
    "CFGScale": 4,
    "scheduler": "UniPC",
    # "includeCost": true,
    # "checkNSFW": true,
    "outputType": [
      "dataURI",
      "URL"
    ],
    "referenceImages": [ # Replace this with a publicly accessible URL to your image
      "https://media.allure.com/photos/595f1a341533d771860418bc/1:1/w_4750,h_4750,c_limit/GettyImages-521865021.jpg" 
    ],
    "model": "runware:108@20",
    "positivePrompt": "Make this image a professional headshot. The subject should wear professional clothes in an office building, sitting on an office chair with hands on desk and smiling. High detail, photorealistic, studio lighting, 8k resolution.",
    "negativePrompt": "blurry, lowres, deformed, disfigured, ugly, bad anatomy, poorly drawn, mutation, mutated, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, fused fingers, too many fingers"
  }
]

response = requests.post(f"{RUNWARE_API_URL}/request", json=payload, headers=headers)

if response.status_code == 200:
    result = response.json()
    image_url = result["data"][0]["imageURL"]
    print("Generated headshot:", image_url)
else:
    print("Error:", response.status_code, response.text)