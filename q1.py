transactions = [
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_15'},
    {'orderId': 1003, 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_10'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
]

catalog = {
    'prod_10': 'Wireless Mouse',
    'prod_12': 'Keyboard',
    'prod_15': 'USB-C Hub',
}

def build_customer_profiles(log):
    data = {}
    for entry in log:
        cust = entry['customerId']
        prod = entry['productId']
        data.setdefault(cust, set()).add(prod)
    return data

def count_product_pairs(customer_dict):
    pair_freq = {}
    for products in customer_dict.values():
        items = sorted(products)
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                pair = (items[i], items[j])
                pair_freq[pair] = pair_freq.get(pair, 0) + 1
    return pair_freq

def recommend_products(target_id, pair_data):
    related = {}
    for (p1, p2), freq in pair_data.items():
        if target_id in (p1, p2):
            other = p2 if p1 == target_id else p1
            related[other] = freq
    return sorted(related.items(), key=lambda x: x[1], reverse=True)

def print_recommendations(target_id, suggestions, product_catalog):
    print(f"\nProducts frequently bought with '{product_catalog[target_id]}':\n")
    for idx, (pid, freq) in enumerate(suggestions, start=1):
        print(f"{idx}. {product_catalog[pid]} — purchased together {freq} times.")

def main():
    customers = build_customer_profiles(transactions)
    pairs = count_product_pairs(customers)
    recs = recommend_products('prod_12', pairs)
    print_recommendations('prod_12', recs, catalog)

if __name__ == "__main__":
    main()
