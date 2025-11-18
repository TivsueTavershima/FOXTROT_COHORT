import json
from django.http import JsonResponse



# ====== SAMPLE PRODUCT DATA (List of Dicts) ====== #
market_product = [
    {
        "id": 1,
        "name": "Wireless Mouse",
        "category": "Electronics",
        "price": 29.99,
        "stock": 120,
        "description": "A smooth and responsive wireless mouse."
    },
    {
        "id": 2,
        "name": "Laptop Backpack",
        "category": "Accessories",
        "price": 49.99,
        "stock": 80,
        "description": "Water-resistant backpack with padded laptop compartment."
    },
    {
        "id": 3,
        "name": "Bluetooth Speaker",
        "category": "Electronics",
        "price": 59.99,
        "stock": 40,
        "description": "Portable speaker with rich bass and long battery life."
    },
    {
        "id": 4,
        "name": "Running Sneakers",
        "category": "Fashion",
        "price": 89.99,
        "stock": 50,
        "description": "Lightweight running shoes designed for comfort and speed."
    },
    {
        "id": 5,
        "name": "Smart Watch",
        "category": "Electronics",
        "price": 129.99,
        "stock": 35,
        "description": "Touchscreen smartwatch with fitness tracking features."
    },
    {
        "id": 6,
        "name": "Office Chair",
        "category": "Furniture",
        "price": 199.99,
        "stock": 20,
        "description": "Ergonomic office chair with lumbar support."
    },
]


# ====== VIEW: GET ALL PRODUCTS ====== #
def get_product(request):
    if request.method == 'GET':
        category = request.GET.get('category')
           #print(category, "CATEGORY")
        filtered_products = []    
        if category != None:
            for product in market_product:
                if category == product['category']:
                    filtered_products.append(product)
                else:
                    if len(filtered_products) == 0:
                        return JsonResponse({"what you are looking for is not available"}, status=400)
                    return JsonResponse({"message": "Get products successful", "products": filtered_products}, status=200)
        else:
                    return JsonResponse({"message": "Get product successful", "products": market_product}, status=200)
    else:
        return JsonResponse({'message': 'invalid request method'}, status=405)
    
    
    
def create_product(request):
        if request.method == 'POST':
     # requset. body # bytes format
            incoming_data = request.body.decode()
            to_dict = json.loads(incoming_data)
            
            print(to_dict)
            market_product.append({"id":len(market_product) +1, **to_dict})
            return JsonResponse({'message': 'product created succesful'} , status=201)
            
            
            
def update_product(request, id):
        if request.method == 'PUT':
            # REUQEST.BODY # BYTES FORMAT
            incoming_data = request.body.decode() # STRING FORMAT
            to_dict = json.loads(incoming_data) #dictionary format
            for product in market_product:
                if id == product["id"]:
                    product["name"] = to_dict["name"]
                    product["category"] = to_dict["category"]
                    product["price"] = to_dict["price"]
                    product["stock"] = to_dict["stock"]
                    product["description"] = to_dict["description"]
                    
            return JsonResponse({'message': 'product updated succesful'} , status=201)
        else:
            return JsonResponse({'message': 'invalid request method'}, status=405)            
                    
                    
def delete_product(request, id):
            if request.method == 'DELETE':
                market_product.pop(id - 1)
                print(market_product)
                return JsonResponse(data=None,safe=False, status=200)
            else:
                 return JsonResponse({'message': 'you are using the wrong method'}, status=405) 
                
                    
            
            