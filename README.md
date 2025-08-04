# Springboard Data Pipeline Mini Project
## Objective
In this project, we:
1. Write the table definition DDL and use it to create the sales table.
2. Read the CSV file and load the new sales records into the ticket sales table.
3. Use the loaded data to provide the 3 most popular tickets in the database.

## Project Files
- data_pipeline.py (main Python script)
- third_party_sales.csv (data file being loaded to the mySQL server)

## Instructions
Note: This section assumes that user has MySQL Workbench correctly set up.

### Create MySQL Database
In MySQL Workbench, use the code below to create a database named eventtickets (or any name you prefer). Remember the name given to the database as this will be used in our Python code.
In this step, it's recommended that root account is used unless another account has been configured with great familiarity.
```
CREATE DATABASE eventtickets;
```

### Running the Python Script
1. Download both the Python script and CSV file, ensuring they are in the same folder. This ensures that the script can locate the CSV without needing to specify the full file path. This step is crucial so the following code lines within the script will run as designed:
```
# Set work directory to script location
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join (base_dir, "third_party_sales.csv")
...
load_third_party(conn, file_path)
```
2. Inside the Python script, update the following section with your own MySQL credentials:
   - Replace username with your MySQL username. As stated before, root is recommended
   - Replace password with your MySQL password
   - Replace hostname with localhost or your host
   - Repace database_name with eventticket (or whatever you chose to name the database in the Create MySQL Database section
```
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='<username>'
                                            ,password='<password>'
                                            ,host='<hostname>'
                                            ,port='3306'
                                            ,database='<database_name>')
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
```
3. Open a terminal or command prompt. Set work directory to the location where this project was downloaded to
```
cd C:\insert\folder\path\here
```
4. Once work directory has been set up correctly, run the script by typing the following in the command prompt
```
python data_pipeline.py
```
5. The output should look like the following:
   
   <img width="588" height="115" alt="image" src="https://github.com/user-attachments/assets/9eee359a-b202-4656-aaf3-2032d16cfa6b" />

   
