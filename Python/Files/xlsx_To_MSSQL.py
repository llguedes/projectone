import pyodbc
import xlrd as ex
import pandas as pd

# create Connection and Cursor objects
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SPOBRSQLPRD17;"
                      "Database=ITXpeer;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

cursor.execute("DELETE FROM dbo.Backlog WHERE Number LIKE 'INC%'")
conn.commit()

# Open the workbook and define the worksheet
xFile = (r"C:\Integration\Backlog.xlsx")

# read data
data = pd.read_excel(xFile)

# rename columns
data = data.rename(columns={'Number' : 'Number',
                            'Customer Ref #' : 'Customer_ref',
                            'Short description' : 'Short_description',
                            'Caller company' : 'Caller_company', 
                            'Affected end user' : 'Affected_user', 
                            'Impacted Business Service' : 'Impacted_Business_Service',
                            'Assignment group' : 'Assignment_group',
                             'Access Media' : 'Access_Media',
                             'Opened by' : 'Opened_by',
                             'Opened' : 'Opened'})


#writer = pd.ExcelWriter(xFile, engine='xlsxwriter')

# export
data.to_excel(xFile, index=False)

#writer.save()

# Open the workbook and define the worksheet
wb = ex.open_workbook(xFile)
sheet = wb.sheet_by_name("Sheet1")

#cursor.execute('SELECT * FROM ITXpeer.dbo.Backlog')
#for row in cursor:
#    print('row = %r' % (row,))

query = """
INSERT INTO [DBO].[Backlog] (    
    Number,
    Customer_Ref,
    Short_description,
    Caller_company,
    Affected_user,
    Impacted_Business_Service,
    Assignment_group,
    Access_Media,
    Opened_by,
    Opened
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

for r in range(1, sheet.nrows):   
    Number = sheet.cell(r,0).value
    Customer_Ref = sheet.cell(r,1).value
    Short_description = sheet.cell(r,2).value
    Caller_company = sheet.cell(r,3).value
    Affected_user = sheet.cell(r,4).value
    Impacted_Business_Service = sheet.cell(r,5).value
    Assignment_group = sheet.cell(r,6).value
    Access_Media = sheet.cell(r,7).value
    Opened_by = sheet.cell(r,8).value
    Opened = sheet.cell(r,9).value

    # Assign values from each row
    values = (Number, Customer_Ref, Short_description, Caller_company, Affected_user,
              Impacted_Business_Service, Assignment_group, Access_Media, Opened_by, Opened)

    # Execute sql Query
    cursor.execute(query, values)

# Commit the transaction
conn.commit()

# If you want to check if all rows are imported
cursor.execute("SELECT count(*) FROM DBO.Backlog")
result = cursor.fetchone()

# Close the database connection
conn.close()