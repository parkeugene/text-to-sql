from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
import re

llm = Ollama(model = "aya:8b")

db = SQLDatabase.from_uri("postgresql://@localhost:5432/mydatabase")

#db.get_usable_table_names()
#['employees']

chain = create_sql_query_chain(llm = llm, db = db)


database_description = (
    "The database consists of two tables: `public.employees_table` and `public.departments_table`. This is a PostgreSQL database, so you need to use postgres-related queries.\n\n"
    "The `public.employees_table` table records details about the employees in a company. It includes the following columns:\n"
    "- `id`: A unique identifier for each employee.\n"
    "- `name`: The name of the employee.\n"
    "- `position`: The position of the employee.\n"
    "- `salary`: The salary of the employee.\n"
)
response = chain.invoke({"question": " How many employees have salary above 70k?"})

print(response)

def extract_sql_query(response):
    # Define the regular expression pattern to match the SQL query
    pattern = re.compile(r'SQLQuery:\s*(.*)')
    # Search for the pattern in the response
    match = pattern.search(response)
    if match:
        # Extract and return the matched SQL query
        return match.group(1).strip()
    else:
        return None

sql_query = extract_sql_query(response)

result = db.run(sql_query)
print(result)
