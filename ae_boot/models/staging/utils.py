import typing;

file_names = [
    'customer',
'employee_privileges',
'employees',
'inventory_transaction_types',
'inventory_transactions',
'invoices',
'order_details',
'order_details_status',
'orders_status',
'orders',
'orders_tax_status',
'privileges',
'products',
'purchase_order_details',
'purchase_order_status',
'purchase_orders',
'shippers',
'suppliers',
'strings']

def create_model_file(model_name: str):
    with open(f'./stg_{model_name}.sql', 'w') as f:
        file_content = f"""
        with source as (
            select * from {{{{source('northwind', '{model_name}')}}}}
        )

        select 
            *,
            current_timestamp() as ingestion_timestamp
        from source
        """
        f.write(file_content)
        
for f in file_names:
    create_model_file(f)

