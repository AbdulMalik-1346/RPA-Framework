import json

import oracledb
import pandas as pd


class Oracle:
    user_name = 'winbot'
    password = 'Welcome1'
    service_name = 'EBSVIS'
    host_name = 'winfo106.winfosolutions.com'
    port = 1556

    def __init__(self):
        try:
            dsn = oracledb.makedsn(Oracle.host_name, Oracle.port, service_name=Oracle.service_name)
            oracledb.init_oracle_client()
            self.conn = oracledb.connect(dsn, user=Oracle.user_name, password=Oracle.password)
            print(str(self.conn))
            self.cursor = self.conn.cursor()
            print('Database connected successfully....')
        except oracledb.DatabaseError as e:
            print("Error connecting to Oracle:", e)

    def get_connection(self):
        if self.conn:
            return self.conn
        return None

    def get_application_df(self):
        self.cursor.execute("select * from wb_process_apps")
        return pd.DataFrame(data=self.cursor.fetchall(), columns=[x[0] for x in self.cursor.description])

    def get_locators_df(self):
        self.cursor.execute("select * from wb_process_apps_actions")
        return pd.DataFrame(data=self.cursor.fetchall(), columns=[x[0] for x in self.cursor.description])

    def get_wb_processes_df(self):
        self.cursor.execute("select * from wb_processes")
        return pd.DataFrame(data=self.cursor.fetchall(), columns=[x[0] for x in self.cursor.description])

    def get_filter_wb_processes_cfg(self, wb_processes_df, wb_processes_steps_cfg_df, application_name, process_name):
        processes_id = wb_processes_df.loc[(wb_processes_df['APPLICATION'] == application_name) & (wb_processes_df['PROCESS_NAME'] == process_name)].values[0][1]
        return wb_processes_steps_cfg_df[(wb_processes_steps_cfg_df['PROCESS_ID'] == processes_id)]

    def get_wb_processes_steps_cfg_df(self):
        self.cursor.execute("select * from wb_processes_steps_cfg")
        return pd.DataFrame(data=self.cursor.fetchall(), columns=[x[0] for x in self.cursor.description])

    def get_actions_name(self):
        self.cursor.execute("select distinct action from wb_processes_steps_cfg")
        return self.cursor.fetchall()

    def insert_value(self, input_parameter):
        try:
            self.cursor.execute(input_parameter)
            print("Inserted successfully!")
        except Exception as e:
            print("Error during insertion due to :", e)
            self.cursor.connection.rollback()

    def update_value(self, input_parameter):
        try:
            self.cursor.execute(input_parameter)
            print("Updated successfully!")
        except Exception as e:
            print("Error during deletion due to:", e)

    def get_value(self, input_parameter, step_no, value_dictionary):
        try:
            self.cursor.execute(input_parameter)
            fetched_data = self.cursor.fetchall()
            if len(fetched_data[0]) == 1:
                value_dictionary[step_no] = fetched_data
            else:
                # Convert the fetched data to a list of dictionaries
                columns = [desc[0] for desc in self.cursor.description]
                result_data = [dict(zip(columns, row)) for row in fetched_data]
                # Convert the result_data to JSON format
                json_data = json.dumps(result_data, indent=4)
                value_dictionary[step_no] = json_data
            print('Data fetched successfully...')

        except Exception as e:
            print(f'Error while fetching data due to : {e}')

    def filter_locators(self, action, application_name, applications_df, locators_df, no_of_params):
        application_id = applications_df.loc[applications_df['APPLICATION'] == application_name, 'PROCESS_APPS_ID'].values[0]
        filters_df = locators_df[(locators_df['PROCESS_APPS_ID'] == application_id) & (locators_df['ACTION'] == action) & (locators_df['NO_OF_INPUT_PARAMS'] == no_of_params)]
        return filters_df


if __name__ == '__main__':
    db = Oracle()

    if hasattr(db, 'conn') and hasattr(db, 'cursor'):
        db.cursor.close()
        print('Cursor closed successfully....')
        db.conn.close()
        print('Connection closed successfully....')
