import requests
key="bee4a434-8754-4e82-b3b8-002520af8753-d0c306bf-3343-459c-99f0-84420e438e25:2c47ed15-b154-4031-82ad-fffb0d993abf"


url = "https://ecommerce.gelatoapis.com/v1/stores/{{storeId}}/products:create-from-template"
headers = {
    "X-API-KEY": key,
    "Content-Type": "application/json"
}

data = {
    "templateId": "c12a363e-0d4e-4d96-be4b-bf4138eb8743",
    "title": "Classic Unisex Crewneck T-shirt",
    "description": "<div><p>A classic unisex t-shirt that works well with any outfit. Made of a heavier cotton with a double-stitched neckline and sleeves.</p><p>- Rolled-forward shoulders for a better fit<br>- Stylish fitted sleeve<br>- Seamless double-needle collar<br>- Taped neck and shoulders for durability<br>- Tubular fit for minimal torque</p><p>This product is made on demand. No minimums.</p></div>",
    "isVisibleInTheOnlineStore": True,
    "salesChannels": ["web"],
    "variants": [
        {
            "templateVariantId": "83e30e31-0aee-4eca-8a8f-dceb2455cdc1",
            "imagePlaceholders": [
                {
                    "name": "ImageFront",
                    "fileUrl": "https://s3-eu-west-1.amazonaws.com/developers.gelato.com/product-examples/test_print_job_BX_4-4_hor_none.pdf"
                }
            ]
        },
        # ... Add other variants here ...
    ]
}

response = requests.post(url, headers=headers, json=data)

print("Response:", response.status_code)
print("Response Content:", response.text)
