## Deligent-R22EH147-ecom-data-challenge
#AI Tools Used:
      * Perplexity-Pro @comet : To generate Datasets as it gives best data operation features
      * Cursor IDE: To import data from multiple CSV files into  SQLite database
      * Gemini 2.5PRO : For basic queries about the project.
      * Chat-Gpt 5.1 : For analysing code errors
Prompts used: 
  Comet for dataset generation using python: 
    "Generate the Python code for five separate CSV files that contain synthetic e-commerce data.
customers.csv: columns: customer_id, name, email, city. (50 rows)
products.csv: columns: product_id, name, category, price. (10 rows)
orders.csv: columns: order_id, customer_id, order_date, total_amount. (100 rows, use IDs from customers.csv)
order_items.csv: columns: item_id, order_id, product_id, quantity. (Link to orders and products)
returns.csv: columns: return_id, order_id, reason. (10 rows, use IDs from orders.csv) The code must save these 5 files into a directory called data/."

Chat GPT :
