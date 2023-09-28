def bill_total(bill, tax_rate):
    taxable = list(filter(lambda item: item["taxable"] == True, bill))
    not_taxable = list(filter(lambda item: item["taxable"] == False, bill))

    untaxed = not_taxable[0]["quantity"] * not_taxable[0]["item_cost"]


    subtotal = sum([item["quantity"] * item["item_cost"] for item in taxable])
    taxes = subtotal * tax_rate

    return subtotal + taxes + untaxed

data = [{'quantity': 3, 'item_cost': 4.0, 'taxable': True},
        {'quantity': 7, 'item_cost': 1.0, 'taxable': False},
        {'quantity': 3, 'item_cost': 11.0, 'taxable': True},
        {'quantity': 1, 'item_cost': 10.0, 'taxable': True}]

result = bill_total(data, 0.1)
print(result)