
import re
import pandas as pd

df_initial = pd.read_csv('data_row100.csv', engine='python',
                         dtype={'SalesOrganizationName': str,
                                'FirmID': str, 'OrderTypeName': str,
                                'CustomerCode': int,
                                'CustomerTypeName': str, 'CustomerCategoryName': str,
                                'RegionName': str, 'OrderDate': str,
                                'OrderNote': str, 'SOPNote': str,
                                'CustomerOrderNumber': str,
                                'SAPSyncDate': str,
                                'ProductCode': str,
                                'InternationalCode': str, 'ProductName': str,
                                'ProcutBarcode': str, 'Signature': str,
                                'Brand': str, 'SubBrand': str, 'ProductWeight': str,
                                'ProductLength': int, 'ProductWidth': int,
                                'ProductHeight': int, 'ProductBoxQuantity': int,
                                'ProductPaletQuantity': int, 'ProductTypeName': str,
                                'MaterialGroupName': str, 'ItemCategory': str,
                                'Amount': str, 'Point': str,
                                'OrderProductType': str, 'Price': str, 'ProductPrice': str})

#print(df_initial.dtypes)
print('Dataframe dimensions:', df_initial.shape)

temp1 = df_initial[['CustomerCode', 'CustomerOrderNumber', 'InternationalCode']].groupby(['CustomerCode', 'CustomerOrderNumber', 'InternationalCode']).count()
temp1 = temp1.reset_index(drop=False)

customer_code = temp1['CustomerCode'].value_counts()
print('Number of Customer Code: {}'.format(len(customer_code)))

customer_order = temp1['CustomerOrderNumber'].value_counts()
print('Number of Customer Order {}'.format(len(customer_order)))

inter_code = temp1['InternationalCode'].value_counts()
print('Number of Inter Code: {}'.format(len(inter_code)))


temp2 = df_initial[['SalesOrganizationName', 'CustomerTypeName', 'OrderDate',
                    'ProductCode']].groupby(['SalesOrganizationName', 'CustomerTypeName', 'OrderDate', 'ProductCode']).count()

temp2 = temp2.reset_index(drop=False)

sales_org_name = temp2['SalesOrganizationName'].value_counts()
print('Number of Sales Organization Name: {}'.format(len(sales_org_name)))

customer_type_name = temp2['CustomerTypeName'].value_counts()
print('Number of Customer Type Name {}'.format(len(customer_type_name)))

order_date = temp2['OrderDate'].value_counts()
print('Number of Order Date: {}'.format(len(order_date)))

product_code = temp2['ProductCode'].value_counts()
print('Number of Product Code: {}'.format(len(product_code)))

"""
temp3 = df_initial[['CustomerCode', 'CustomerOrderNumber', 'InternationalCode',
                    'SalesOrganizationName', 'CustomerTypeName',
                    'OrderDate', 'ProductCode']].groupby(['CustomerCode', 'CustomerOrderNumber',
                     'InternationalCode', 'SalesOrganizationName',
                     'CustomerTypeName', 'OrderDate', 'ProductCode']).count()

temp3 = temp3.reset_index(drop=False)

customer_code = temp3['CustomerCode'].value_counts()
print('Number of Customer Code: {}'.format(len(customer_code)))

customer_order = temp3['CustomerOrderNumber'].value_counts()
print('Number of Customer Order {}'.format(len(customer_order)))

inter_code = temp3['InternationalCode'].value_counts()
print('Number of Inter Code: {}'.format(len(inter_code)))

sales_org_name = temp3['SalesOrganizationName'].value_counts()
print('Number of Sales Organization Name: {}'.format(len(sales_org_name)))

customer_type_name = temp3['CustomerTypeName'].value_counts()
print('Number of Customer Type Name {}'.format(len(customer_type_name)))

order_date = temp3['OrderDate'].value_counts()
print('Number of Order Date: {}'.format(len(order_date)))

product_code = temp3['ProductCode'].value_counts()
print('Number of Product Code: {}'.format(len(product_code)))
"""
"""

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

print(df)
print(df.groupby('Company').count())
df = df.reset_index(drop=True)
print(df.groupby('Company').count().value_counts())
"""