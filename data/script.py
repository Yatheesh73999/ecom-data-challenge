
import pandas as pd
import os
from datetime import datetime, timedelta
import random

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Set random seed for reproducibility
random.seed(42)

# 1. Generate Customers CSV (50 rows)
customers_data = {
    'customer_id': range(1, 51),
    'name': [f'Customer_{i}' for i in range(1, 51)],
    'email': [f'customer_{i}@email.com' for i in range(1, 51)],
    'city': random.choices(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'], k=50)
}
customers_df = pd.DataFrame(customers_data)
customers_df.to_csv('data/customers.csv', index=False)
print("✓ customers.csv created (50 rows)")

# 2. Generate Products CSV (10 rows)
products_data = {
    'product_id': range(1, 11),
    'name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'USB Hub', 'Desk Lamp', 'Phone Charger', 'Screen Protector'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Furniture', 'Accessories', 'Accessories'],
    'price': [999.99, 25.99, 49.99, 299.99, 79.99, 49.99, 29.99, 39.99, 19.99, 9.99]
}
products_df = pd.DataFrame(products_data)
products_df.to_csv('data/products.csv', index=False)
print("✓ products.csv created (10 rows)")

# 3. Generate Orders CSV (100 rows)
base_date = datetime.now() - timedelta(days=365)
orders_data = {
    'order_id': range(1, 101),
    'customer_id': [random.randint(1, 50) for _ in range(100)],
    'order_date': [base_date + timedelta(days=random.randint(0, 365)) for _ in range(100)],
    'total_amount': [round(random.uniform(50, 5000), 2) for _ in range(100)]
}
orders_df = pd.DataFrame(orders_data)
orders_df['order_date'] = orders_df['order_date'].dt.strftime('%Y-%m-%d')
orders_df.to_csv('data/orders.csv', index=False)
print("✓ orders.csv created (100 rows)")

# 4. Generate Order Items CSV
# Create order items linked to existing orders and products
order_items_data = {
    'item_id': [],
    'order_id': [],
    'product_id': [],
    'quantity': []
}

item_id = 1
for order_id in range(1, 101):
    # Each order has 1-3 items
    num_items = random.randint(1, 3)
    for _ in range(num_items):
        order_items_data['item_id'].append(item_id)
        order_items_data['order_id'].append(order_id)
        order_items_data['product_id'].append(random.randint(1, 10))
        order_items_data['quantity'].append(random.randint(1, 5))
        item_id += 1

order_items_df = pd.DataFrame(order_items_data)
order_items_df.to_csv('data/order_items.csv', index=False)
print(f"✓ order_items.csv created ({len(order_items_df)} rows)")

# 5. Generate Returns CSV (10 rows)
returns_data = {
    'return_id': range(1, 11),
    'order_id': random.sample(range(1, 101), 10),  # 10 unique orders
    'reason': ['Defective', 'Wrong item', 'Not as described', 'Changed mind', 'Damaged in shipping', 'Defective', 'Wrong item', 'Not as described', 'Changed mind', 'Damaged in shipping']
}
returns_df = pd.DataFrame(returns_data)
returns_df.to_csv('data/returns.csv', index=False)
print("✓ returns.csv created (10 rows)")

print("\n✓ All CSV files successfully created in 'data/' directory!")
print("\nFiles created:")
print("  - data/customers.csv")
print("  - data/products.csv")
print("  - data/orders.csv")
print("  - data/order_items.csv")
print("  - data/returns.csv")
