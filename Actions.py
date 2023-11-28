import os
import secrets
import smtplib
import string
import time
import zipfile
import shutil
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import selenium.webdriver
from SeleniumLibrary import SeleniumLibrary

from Oracle import Oracle


# lib = SeleniumLibrary()
# lib.get_window_handles()


class Actions:

    def __init__(self, lib: SeleniumLibrary):
        self.lib = lib

    def click_button(self, oracle, input_parameter, selector, action, application_name, applications_df, locators_df):
        # selector = f"//button[text()='code_var0']"
        # argument for update selector in database -> step_no, db_connection, process_id, table_id_column_name, table_name,
        found = False
        params = input_parameter.split('>')  # genric>sign in>hello

        def get_path(element_selector):
            match len(params):
                case 1:
                    return element_selector.replace("code_var0", params[0])
                case 2:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1])
                case 3:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1]).replace(
                        "code_var2",
                        params[2])

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                print(f'xpath--------------> {xpath}')
                self.lib.wait_until_element_is_visible(xpath, timeout=5)
                self.lib.click_button(xpath)
                found = True
                print(f'Successfully clicked on {input_parameter}')
        except Exception as e:
            # application_id = db_connection.filter_data_by_id(web_desktop_app_dt, process_config_application)
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, len(params))
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'xpath--------------> {xpath}')
                try:
                    self.lib.wait_until_element_is_visible(xpath, timeout=5)
                    self.lib.click_button(xpath)
                    found = True
                    # save_path_to_db(path)
                except Exception as e:
                    found = False
            if found:
                print(f'Successfully clicked on {input_parameter}')

        if not found:
            raise Exception(f'The element {input_parameter} is not found in the page...')

    def click_image(self, oracle, input_parameter, selector, action, application_name, applications_df, locators_df):
        # selector = f"//button[text()='code_var0']"
        found = False
        params = input_parameter.split('>')

        def get_path(element_selector):
            match len(params):
                case 1:
                    return element_selector.replace("code_var0", params[0])
                case 2:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1])
                case 3:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1]).replace("code_var2", params[2])

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                self.lib.wait_until_element_is_visible(xpath, timeout=20)
                self.lib.click_image(xpath)
                print(f'xpath-------------> {xpath}')
                print(f'Successfully clicked on {input_parameter}')
        except Exception as e:
            # application_id = db_connection.filter_data_by_id(web_desktop_app_dt, process_config_application)
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, len(params))
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'xpath-------------> {xpath}')
                try:
                    self.lib.wait_until_element_is_visible(xpath, timeout=5)
                    self.lib.click_image(xpath)
                    found = True
                    # save_path_to_db(path)
                except Exception as e:
                    found = False
            if found:
                print(f'Successfully clicked on {input_parameter}')

        if not found:
            raise Exception(f'The element {input_parameter} is not found in the page...')

    def click_link(self, oracle, input_parameter, selector, action, application_name, applications_df, locators_df):
        # selector = f"//button[text()='code_var0']"
        found = False
        params = input_parameter.split('>')

        def get_path(element_selector):
            match len(params):
                case 1:
                    return element_selector.replace("code_var0", params[0])
                case 2:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1])
                case 3:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1]).replace("code_var2", params[2])

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                self.lib.wait_until_element_is_visible(xpath, timeout=20)
                self.lib.click_link(xpath)
                print(f'Successfully clicked on {input_parameter}')
                found = True
        except Exception as e:
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, len(params))
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'xpath-------------> {xpath}')
                try:
                    self.lib.wait_until_element_is_visible(xpath, timeout=5)
                    self.lib.click_link(xpath)
                    found = True
                    # save_path_to_db(path)
                except Exception as e:
                    found = False
            if found:
                print(f'Successfully clicked on {input_parameter}')

        if not found:
            raise Exception(f'The element {input_parameter} is not found in the page...')

    def click_dropdown(self, oracle, input_parameter, selector, action, application_name, applications_df, locators_df):
        # selector = f"//button[text()='code_var0']"
        found = False
        params = input_parameter.split('>')
        print(selector)
        print(input_parameter)
        search_link = '//span/following-sibling::div//table//a[contains(text(), "Search...")]'
        input_field = '//div[text()="Search and Select: Business Unit"]/ancestor::tr[2]/following-sibling::tr//label[text()="Business Unit"]/parent::td/following-sibling::td//input'
        search_btn = '//div[text()="Search and Select: Business Unit"]/ancestor::tr[2]/following-sibling::tr//button[text()="Search"]'
        select = '//span[text()="Ledger Name"]/ancestor::div[3]/following-sibling::div/table/tbody/tr[1]'
        confirm = '//div[text()="Search and Select: Business Unit"]/ancestor::tr[2]/following-sibling::tr[2]//button[text()="OK"]'

        def get_path(element_selector):
            return element_selector.replace("code_var0", params[0])

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                print(f'xpath 1-------------->  {xpath}')
                self.lib.wait_until_element_is_visible(xpath, timeout=20)
                self.lib.click_element(xpath)
                print('Successfully clicked on dropdown....')
                self.lib.wait_until_element_is_visible(search_link, timeout=20)
                self.lib.click_element(search_link)
                print('Successfully clicked on search link....')
                self.lib.wait_until_element_is_visible(input_field, timeout=20)
                self.lib.input_text(input_field, params[1])
                print('Successfully typed text....')
                self.lib.wait_until_element_is_visible(search_btn, timeout=20)
                self.lib.click_element(search_btn)
                print('Successfully clicked on search button....')
                self.lib.wait_until_element_is_visible(select, timeout=20)
                self.lib.click_element(select)
                print('Successfully selected item....')
                self.lib.wait_until_element_is_visible(confirm, timeout=20)
                self.lib.click_element(confirm)
                print('Successfully clicked on confirm....')
                print(f'Successfully drop down for {input_parameter}')
                found = True
        except Exception as e:
            # application_id = db_connection.filter_data_by_id(web_desktop_app_dt, process_config_application)
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, 1)
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'xpath -------------->  {xpath}')
                try:
                    self.lib.wait_until_element_is_visible(xpath, timeout=20)
                    self.lib.click_element(xpath)
                    print('Successfully clicked on dropdown....')
                    self.lib.wait_until_element_is_visible(search_link, timeout=20)
                    self.lib.click_element(search_link)
                    print('Successfully clicked on search link....')
                    self.lib.wait_until_element_is_visible(input_field, timeout=20)
                    self.lib.input_text(input_field, params[1])
                    print('Successfully typed text....')
                    self.lib.wait_until_element_is_visible(search_btn, timeout=20)
                    self.lib.click_element(search_btn)
                    print('Successfully clicked on search button....')
                    self.lib.wait_until_element_is_visible(select, timeout=20)
                    self.lib.click_element(select)
                    print('Successfully selected item....')
                    self.lib.wait_until_element_is_visible(confirm, timeout=20)
                    self.lib.click_element(confirm)
                    print('Successfully clicked on confirm....')
                    found = True
                except Exception as e:
                    found = False
            if found:
                print(f'Successfully dropdown to {input_parameter}')

        if not found:
            raise Exception(f'The element {input_parameter} is not found in the page...')
        else:
            pass
            # save_path_to_db(path)

    def copy_text(self, oracle, input_parameter, selector, action, application_name, applications_df, locators_df):
        # selector = f"//button[text()='code_var0']"
        copied_text = None
        found = False
        params = input_parameter.split('>')

        def get_path(element_selector):
            match len(params):
                case 1:
                    return element_selector.replace("code_var0", params[0])
                case 2:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1])
                case 3:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1]).replace("code_var2", params[2])

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                print(f'path----------------> {xpath}')
                self.lib.wait_until_element_is_visible(xpath, timeout=30)
                copied_text = self.lib.get_text(xpath)
                # save_text_to_db(copied_text)
                print(f'Successfully text copied text={copied_text} for {input_parameter}')
                found = True
        except Exception as e:
            # application_id = db_connection.filter_data_by_id(web_desktop_app_dt, process_config_application)
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, len(params))
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'path----------------> {xpath}')
                try:
                    self.lib.wait_until_element_is_visible(xpath, timeout=10)
                    copied_text = self.lib.get_text(xpath)
                    found = True
                except Exception:
                    found = False
            if found:
                print(f'Successfully text copied text={copied_text} for {input_parameter}')

        if not found:
            raise Exception(f'The element {input_parameter} is not found in the page...')
        else:
            return copied_text
            # TODO save_text_to_db(copied_text)

    def radio_button(self, oracle, input_parameter, selector, action, application_name, applications_df, locators_df):
        # selector = f"//button[text()='code_var0']"
        found = False
        params = input_parameter.split('>')

        def get_path(element_selector):
            return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1])

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                print(f'xpath------------> {xpath}')
                self.lib.wait_until_element_is_visible(xpath, timeout=120)
                self.lib.click_element(xpath)
                print(f'Successfully clicked Radio Button for {input_parameter}')
                found = True
        except Exception as e:
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, len(params))
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'xpath------------> {xpath}')
                try:
                    self.lib.wait_until_element_is_visible(xpath, timeout=120)
                    self.lib.click_element(xpath)
                    found = True
                except Exception as e:
                    found = False
            print(f'Successfully clicked Radio Button for {input_parameter}')

        if not found:
            raise Exception(f'The clicked Radio Button for {input_parameter} is not found in the page...')
        else:
            pass
            # TODO save_path_to_db(path)

    def scroll_to_element(self, oracle, input_parameter, selector, action, application_name, applications_df, locators_df):
        found = False
        params = input_parameter.split('>')  # genric>sign in>hello

        def get_path(element_selector):
            match len(params):
                case 1:
                    return element_selector.replace("code_var0", params[0])
                case 2:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1])
                case 3:
                    return element_selector.replace("code_var0", params[0]).replace("code_var1", params[1]).replace(
                        "code_var2",
                        params[2])

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                print(f'xpath--------------> {xpath}')
                self.lib.wait_until_element_is_visible(xpath, timeout=5)
                self.lib.scroll_element_into_view(xpath)
                found = True
                print(f'Successfully scrolled to {input_parameter}')
        except:
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, len(params))
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'xpath--------------> {xpath}')
                try:
                    self.lib.wait_until_element_is_visible(xpath, timeout=5)
                    self.lib.scroll_element_into_view(xpath)
                    found = True
                    # save_path_to_db(path)
                except:
                    found = False
            if found:
                print(f'Successfully scrolled to {input_parameter}')

        if not found:
            raise Exception(f'The element {input_parameter} is not found in the page...')

    def open_task(self, input_parameter):
        try:
            self.lib.wait_until_element_is_visible(f'xpath://a//child::img[@title="Tasks"]', timeout=20)
            self.lib.click_element(f'xpath://a//child::img[@title="Tasks"]')
            self.lib.wait_until_element_is_visible(f'xpath://a[text()="{input_parameter}"]', timeout=20)
            self.lib.click_element(f'xpath://a[text()="{input_parameter}"]')
            print(f'Open Task for {input_parameter} opened successfully..')
        except Exception as e:
            print(f'Task not opened due to {e}')

    def wait_for_request(self, input_parameter, max_iteration_time, iteration_time):
        self.lib.wait_until_element_is_visible('xpath://a[contains(@title,"Expand Search")]', timeout=120)
        self.lib.click_link('xpath://a[contains(@title,"Expand Search")]')
        self.lib.wait_until_element_is_visible('xpath://h1[text()="Search"]/following::label[text()="Process ID"]/following::input', timeout=20)
        self.lib.input_text('xpath://h1[text()="Search"]/following::label[text()="Process ID"]/following::input', input_parameter)

        self.lib.wait_until_element_is_visible('xpath://button[text()="Search"]', timeout=20)
        self.lib.click_button('xpath://button[text()="Search"]')

        refresh_path = 'xpath://img[@title="Refresh"]'
        value_path = 'xpath://table[@summary="List of Processes Meeting Search Criteria"]//td[4]//span'

        self.lib.wait_until_element_is_visible(refresh_path, timeout=20)
        self.lib.click_element(refresh_path)

        pending_status = ['Wait', 'Running', 'Ready', 'Paused']
        status = ''

        request_id = input_parameter
        # message = "<body>Hi user,</br></br>The RPA "+Module_Name.ToString+" Automation  "+Report_Name.ToString+" report is taking time</br></br>Period : "+Period_Name.ToString+"</br></br>RPA ID: "+Request_ID+"</br></br>Ledger Name: "+Ledger_Name+"</br></br></br>Thank you,</br>Winfo Bots</body>"
        message = "<body>Hi user,</br></br>The RPA Module_Name Automation  Report_Name report is taking time</br></br>Period : Period_Name</br></br>RPA ID: " + request_id + "</br></br>Ledger Name: Ledger_Name</br></br></br>Thank you,</br>Winfo Bots</body>"
        subject = "Your process status"

        start_time = time.time()
        mail_time = iteration_time
        while time.time() - start_time < max_iteration_time:
            self.lib.wait_until_element_is_visible(refresh_path, timeout=20)
            self.lib.click_element(refresh_path)
            self.lib.wait_until_element_is_visible(value_path, timeout=20)
            status = value = self.lib.get_text(value_path)
            print(value)
            if value not in pending_status:
                break
            else:
                if time.time() - start_time > mail_time:
                    # send mail
                    Actions.send_email(self, subject, message)
                    mail_time = mail_time + iteration_time
                else:
                    time.sleep(3)

        if status in pending_status:
            raise TimeoutError
        else:
            print('wait for request completed successfully...')

    @staticmethod
    def send_email(self, subject, message):
        # Email configuration
        sender_email = "abdul.testing@outlook.com"
        receiver_email = "abdul.malik@winfosolutions.com"
        password = "Abdul@123"

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Establish a connection to the SMTP server
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            # Send the email
            server.sendmail(sender_email, receiver_email, text)
            print('Email sent to user successfully...')

    """
        Table filter according to value in front end
    """
    def table_filter(self, oracle, input_parameter, input_data, selector, action, application_name, applications_df, locators_df):
        found = False
        params = input_parameter.split('>')

        def get_path(element_selector):
            selectors = element_selector.split(';')
            if len(selectors) == 2:
                return [selectors[0].replace("code_var0", params[0]), selectors[1].replace("code_var0", params[1])]
            else:
                return None

        try:
            if len(selector) == 0:
                raise Exception("Selector not found..")
            else:
                xpath = get_path(selector)
                self.lib.wait_until_element_is_visible(xpath[0], timeout=60)
                # is_filter_active = bool(self.lib.get_element_attribute(xpath[0], "aria-pressed"))
                # if not is_filter_active:
                #     self.lib.click_element(xpath[0])
                try:
                    self.lib.wait_until_element_is_visible(xpath[1], timeout=2)
                except:
                    self.lib.click_element(xpath[0])
                    self.lib.wait_until_element_is_visible(xpath[1], timeout=60)
                self.lib.input_text(xpath[1], input_data)
                self.lib.press_keys(xpath[1], 'ENTER')
                self.lib.click_element(xpath[0])
                print(f'Successfully filter table for {input_parameter}')
                found = True
        except:
            filters_df = oracle.filter_locators(action, application_name, applications_df, locators_df, len(params))
            for index, data_row in filters_df.iterrows():
                if found:
                    break
                xpath = get_path(data_row['SELECTOR'])
                print(f'xpath--------------> {xpath}')
                if xpath is None:
                    continue
                try:
                    self.lib.wait_until_element_is_visible(xpath[0], timeout=60)
                    try:
                        self.lib.wait_until_element_is_visible(xpath[1], timeout=2)
                    except:
                        self.lib.click_element(xpath[0])
                    self.lib.wait_until_element_is_visible(xpath[1], timeout=60)
                    self.lib.input_text(xpath[1], input_data)
                    self.lib.press_keys(xpath[1], 'ENTER')
                    self.lib.click_element(xpath[0])
                    found = True
                    # save_path_to_db(path)
                except:
                    found = False
            if found:
                print(f'Successfully filter table for {input_parameter}')

        if not found:
            raise Exception(f'The element {input_parameter} is not found in the page...')

    def switch_between_tabs(self):
        self.lib.wait_until_element_is_visible('//span[text()="The Python Language Reference"]/parent::a', timeout=30)
        link_url1 = self.lib.get_element_attribute('//span[text()="The Python Language Reference"]/parent::a', 'href')
        link_url = 'https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html'
        self.lib.execute_javascript(f"window.open('{link_url}', '');")
        self.lib.execute_javascript(f"window.open('{link_url1}', '');")
        locator = "//h2[contains(text(), 'Introduction')]"
        self.lib.switch_window(locator=locator, timeout=20)
        time.sleep(10)


class Generic:
    @staticmethod
    def take_screenshot(self, lib, folder_path):
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
            screenshot_path = f'{folder_path}/screenshot_{timestamp}.png'
            lib.capture_page_screenshot(screenshot_path)
            print(f'Screenshot taken successfully in {folder_path} folder..')
        except Exception as e:
            print(f'Screenshot failed due to {e}')

    @staticmethod
    def create_random_value(self, length):
        try:
            random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
            print(f'Successfully random string {random_string} has been created...')
            return random_string
        except Exception as e:
            print(f'Random value not generated due to {e}')
            return None

    @staticmethod
    def zip_and_unzip_files(self, source_folder, zip_file_name, extract_folder, operation):
        if operation.lower() == 'zip':
            try:
                # Zip files
                shutil.make_archive(zip_file_name, 'zip', source_folder)
                print(f'Files in {source_folder} have been successfully zipped to {zip_file_name}.')
            except Exception as e:
                print(f'Folder not zipped due to {e}')

        elif operation.lower() == 'unzip':
            try:
                # Unzip files
                shutil.unpack_archive(zip_file_name, extract_folder, 'zip')
                print(f'File {zip_file_name} has been successfully unzipped to {extract_folder}.')
            except Exception as e:
                print(f'File not unzipped due to {e}')
        else:
            print("Invalid operation. Please provide 'zip' or 'unzip'.")
