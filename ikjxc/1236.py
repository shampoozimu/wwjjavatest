a ={'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_quantity]': '2',
    'product[product_attr_groups_attributes][0][default_inventory_policies_attributes][0][default_cost]': '4.00'}
b= {'product[product_attr_groups_attributes][0][123][0][default_quantity]': '2'}

c = dict( a, **b )
print(c)
default_quantity = 1
print(default_quantity)
if default_quantity is not 0:
    print(1234)
else:
    print(12445677)

