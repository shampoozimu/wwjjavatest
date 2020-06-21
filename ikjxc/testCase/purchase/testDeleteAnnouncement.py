product_number ='123445'

url = 'api/reports/product_inventory_flow.json?page=1&per=15&warehouse_id=&product_category_id=&product_id=&documentable_category=&attr_status=1&keyword=%s&keyword_type=products.number' % product_number
print(url)