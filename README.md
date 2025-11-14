## Deligent-R22EH147-ecom-data-challenge

### AI Tools Used
- **Perplexity Pro @ Comet** — Used to generate high-quality synthetic datasets through Python-based generation prompts.  
- **Cursor IDE** — Used to write the ingestion script and import multiple CSV files into an SQLite database.  
- **Gemini 2.5 Pro** — Used for quick clarifications, improving prompts, and refining ideas during development.  
- **ChatGPT 5.1** — Used for debugging, refining SQL/Python code, and creating this README.

---

### Prompting Approach Followed
My workflow for interacting with AI during this project was:

1. **Define the Objective** — Clearly state what output or task is required.  
2. **Draft the Prompt** — Include details such as task, context, reasoning, constraints, and desired format.  
3. **Iterate and Communicate** — Refine prompts based on the AI's responses for more accurate results.  
4. **Review Outcomes** — Validate the generated code, datasets, scripts, and outputs.

---

### Guiding Principles
- **Never treat AI as a servant — treat it as a collaborative partner.**  
- **Use AI responsibly and follow ethical practices at all times.**

---

### Prompts Used

#### **Dataset Generation (Comet / Perplexity)**  
```

Generate the Python code for five separate CSV files that contain synthetic e-commerce data.
customers.csv: columns: customer_id, name, email, city. (50 rows)
products.csv: columns: product_id, name, category, price. (10 rows)
orders.csv: columns: order_id, customer_id, order_date, total_amount. (100 rows, use IDs from customers.csv)
order_items.csv: columns: item_id, order_id, product_id, quantity. (Link to orders and products)
returns.csv: columns: return_id, order_id, reason. (10 rows, use IDs from orders.csv)
The code must save these 5 files into a directory called data/.

```

#### **SQLite Ingestion Script (Cursor IDE)**
```

Write a complete Python script that does the following:
Connects to an SQLite database named ecom.db.
Reads the five CSV files (customers.csv, products.csv, orders.csv, order_items.csv, returns.csv) from the data/ directory.
Creates a separate table in the ecom.db database for each CSV file, using the file name as the table name (e.g., customers).
Ingests all the data from the CSV files into their respective SQLite tables.

```

#### **ChatGPT**
```

Context for Readme file → markdown language


