#3 write a function called linear_search_product that takes the list of products and atarget product name as input. The fuction should perform a linear search to find the target product in the list and a return a list of indices of all occurences of the product if found, or an empty list if the product is not found   
def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
product =["apple","banana","apple","orange","apple",]
target = "apple"
result = linear_search_product(product, target)
if result:
    print (f"the product '{target}'was found at indices:{result}")