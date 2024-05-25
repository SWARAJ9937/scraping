import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd


# Database connection parameters
dbname = "rsb"
user = "postgres"
password = "postgres"
host = "localhost"




engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}/{dbname}')

def create_table(engine):
    try:
        with engine.connect() as conn:
            conn.execute(sqlalchemy.text('''
                CREATE TABLE IF NOT EXISTS Payment_mapping (
                    Sl_no BIGINT PRIMARY KEY,
                    AR_Category VARCHAR(12),
                    status VARCHAR(10),
                    GK_order_ID_or_AMD_Chart BIGINT,
                    Accession VARCHAR,
                    Patient_id BIGINT NOT NULL UNIQUE,
                    Claim_id_or_AMD_Visit BIGINT,
                    Patient_Name VARCHAR, 
                    DOB DATE, 
                    Payer_family VARCHAR,
                    Payer VARCHAR,
                    Date_of_Service DATE,
                    AMD_CPT_Codes INT,
                    Billed_amt FLOAT, 
                    Last_Billed_Date DATE,
                    Date_x DATE,
                    Aging_Days_from_DOS VARCHAR,
                    Aging_Bucket_from_DOS VARCHAR(20),
                    TFL_Bucket VARCHAR(20),
                    Paid_Amount FLOAT,
                    Balance FLOAT,
                    check_no VARCHAR,
                    Billed_Status VARCHAR(15),
                    Pay_status VARCHAR,
                    Paid_date DATE,
                    Claim_status VARCHAR,
                    AR_Status VARCHAR,
                    Response VARCHAR,
                    Denial_Category VARCHAR,
                    Medi_Cal_Claims_Remark VARCHAR,
                    GK_location VARCHAR,
                    Report VARCHAR,
                    Billed_Amount FLOAT,
                    Allowed_Amount FLOAT,
                    Paid_Amount_DEC FLOAT,
                    Adjustment_Amount FLOAT,
                    Denied FLOAT,
                    Remark_Code INT,
                    Check_Amount FLOAT,
                    File_name_or_Remarks VARCHAR,
                    Page VARCHAR(5),
                    comments VARCHAR,
                    names VARCHAR
                );
            '''))
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        # Optionally, re-raise the error if you want it to propagate:
        raise

# Use this function call within your main function or directly if testing
# create_table(engine)
def insert_data_from_excel(excel_file_path):
    data = pd.read_excel(excel_file_path, engine='openpyxl')
    data.to_sql('Payment_mapping', engine, if_exists='append', index=False, method='multi')

# Main function
def main():
    create_table(engine)
    insert_data_from_excel('/home/swaraj/Desktop/jupyter notebook/cleaned_data3.xlsx')

if __name__ == "__main__":
    main()
