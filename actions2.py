from SeleniumLibrary import SeleniumLibrary
import time


class Oracle:
    lib = SeleniumLibrary()

    def __init__(self):
        pass

    def get_lib(self):
        return Oracle.lib

    def login(self, input_parameter, application):
        lib = Oracle.lib
        param_arr = input_parameter.split('>')
        lib.open_browser(param_arr[0], application)
        lib.maximize_browser_window()
        lib.input_text('xpath://input[@placeholder=\'User ID\']', param_arr[1])
        lib.input_text('xpath://input[@placeholder=\'Password\']', param_arr[2])
        lib.click_element('xpath://button[text()=\'Sign In \']')
        print("Successfully logged into application")

    def navigation(self, input_parameter):
        lib = Oracle.lib
        lib.wait_until_element_is_visible('xpath://a[@title=\'Navigator\']', 20)
        lib.click_element('xpath://a[@title=\'Navigator\']')
        if input_parameter.__contains__('>'):
            param_arr = input_parameter.split('>')
            parent = f'xpath://div[@title=\'{param_arr[0]}\']'
            child = f'xpath://span[text()=\'{param_arr[1]}\']'

            lib.wait_until_element_is_visible(parent, 20)
            lib.click_element(parent)
            lib.wait_until_element_is_visible(child, 20)
            lib.click_element(child)
            print(f'Successfully navigated to {input_parameter}')
        else:
            pass

    def open_task(self, input_parameter):
        lib = Oracle.lib
        lib.wait_until_element_is_enabled('xpath://img[@title=\'Tasks\']', 15)
        lib.click_element('xpath://img[@title=\'Tasks\']')
        time.sleep(5)
        lib.click_element(f'xpath://a[text()=\'{input_parameter}\']')
        print(f'Opened task {input_parameter} successfully')

    def logout(self):
        lib = Oracle.lib
        lib.click_element('xpath://img[@title=\'Settings and Actions\']')
        time.sleep(3)
        lib.click_element('xpath://a[text()=\'Sign Out\']')
        time.sleep(3)
        lib.click_element('xpath://button[contains(text(),\'Confirm\')]')
        print('Successfully logged out from application')

    def close_browser(self):
        Oracle.lib.close_browser()


class Generic:
    def __init__(self, lib):
        self.lib = lib

    def navigator(self, title='Navigator'):
        lib = self.lib
        lib.wait_until_element_is_visible(f'xpath://a[@title=\'{title}\']', 20)
        lib.click_element(f'xpath://a[@title=\'{title}\']')

    def navigation(self, input_parameter):
        lib = self.lib
        self.navigator()
        if input_parameter.__contains__('>'):
            params = input_parameter.split('>')
            parent = f'xpath://div[@title=\'{params[0]}\']'
            child = f'xpath://span[text()="{params[0]}"]//ancestor::div[3]/following-sibling::div//span[text()="{params[1]}"]'
            lib.wait_until_element_is_visible(parent, 20)
            lib.click_element(parent)
            lib.wait_until_element_is_visible(child, 20)
            lib.click_element(child)
            print(f'Successfully navigated to {input_parameter}')
        else:
            pass

    def tab(self, input_parameter):
        lib = self.lib
        lib.press_key(input_parameter, 'TAB')
        print(f'Successfully clicked TAB {input_parameter}')

    def click_link(self, input_parameter):
        lib = self.lib
        lib.wait_until_element_is_visible(input_parameter, 120)
        lib.click_element(input_parameter)
        print(f'Successfully clicked on link {input_parameter}')

    def select_dropdown(self, input_parameter):
        lib = self.lib
        if input_parameter.__contains__('>'):
            param_arr = input_parameter.split('>')
            lib.wait_until_element_is_visible(param_arr[0], 120)
            lib.click_element(param_arr[0])
            lib.wait_until_element_is_visible(param_arr[1], 120)
            lib.click_element(param_arr[1])
            print(f'Successfully clicked on link {input_parameter}')
        else:
            pass

    def click_button(self, input_parameter):
        lib = self.lib
        lib.wait_until_element_is_visible(input_parameter, 120)
        lib.click_element(input_parameter)
        print(f'Successfully click on button {input_parameter}')

    def text_field(self, input_parameter, data):
        lib = self.lib
        lib.wait_until_element_is_visible(input_parameter, 120)
        lib.input_text(input_parameter, data)
        print(f'Successfully data added to {input_parameter}')

    def enter(self, input_parameter):
        lib = self.lib
        lib.press_keys(input_parameter, 'ENTER')

    def wait(self, s):
        time.sleep(s)
