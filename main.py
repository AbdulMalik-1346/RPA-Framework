from SeleniumLibrary import SeleniumLibrary

from Actions import Actions
from actions2 import Oracle, Generic
from Actions import Generic as Generic1
from Oracle import Oracle as Oc

if __name__ == '__main__':
    url = 'https://login-etaj-dev18-saasfademo1.ds-fa.oraclepdemos.com/'
    user_id = 'IGS_USER'
    password = 'n6%Kx^h3'
    application = 'chrome'

    db = Oc()
    application_df = db.get_application_df()
    locators_df = db.get_locators_df()
    db_conn = db.get_connection()
    # print(application_df)
    # print(locators_df)

    bot = Oracle()
    grnc = Generic(bot.get_lib())
    bot.login(url + ">" + user_id + ">" + password, application)
    grnc.wait(5)
    grnc.navigation("Payables>Invoices")
    action = Actions(bot.get_lib())
    # input_parameter = 'Create Order'
    # action.open_task(input_parameter)
    lib = bot.get_lib()
    lib.wait_until_element_is_visible('//span[text()="18"]', timeout=30)
    lib.click_element('//span[text()="18"]')
    # selector = '//button[contains(text(),"code_var0")]'
    selector = '//div[@title="Query By Example"]//a;//span[text()="Invoice Number"]/ancestor::tr[1]/preceding-sibling::tr[1]/td[1]/span/input'
    input_parameter = 'Query By Example>Accounting Period'

    # action.click_button(db, input_parameter=input_parameter, selector=selector, action='Click Button', application_name='Chrome', applications_df=application_df, locators_df=locators_df)
    # action.click_image(db, input_parameter=input_parameter, selector=selector, action='Click Image', application_name='Chrome', applications_df=application_df, locators_df=locators_df)
    # action.click_link(db, input_parameter=input_parameter, selector=selector, action='Click Link', application_name='Chrome', applications_df=application_df, locators_df=locators_df)
    # action.wait_for_request(input_parameter='6166115', max_iteration_time=3600, iteration_time=30)
    # copied_text = action.copy_text(db, input_parameter=input_parameter, selector=selector, action='Copy Text', application_name='Chrome', applications_df=application_df, locators_df=locators_df)
    # print(f'Copied text is -------------->  {copied_text}')
    # action.click_dropdown(db, input_parameter=input_parameter, selector=selector, action='Button Dropdown', application_name='Chrome', applications_df=application_df, locators_df=locators_df)
    # action.scroll_to_element(db, input_parameter=input_parameter, selector=selector)
    # action.radio_button(db, input_parameter=input_parameter, selector=selector, action='Radio Button', application_name='Chrome', applications_df=application_df, locators_df=locators_df)
    action.table_filter(db, input_parameter=input_parameter, input_data='09-23', selector=selector, action='Table Filter', application_name='Chrome', applications_df=application_df, locators_df=locators_df)

    # url1 = 'https://docs.python.org/3/library/'
    # lib = SeleniumLibrary()
    # lib.open_browser(url1, application)
    # lib.maximize_browser_windowm()
    # action = Actions(lib)
    # action.switch_between_tabs()

    grnc.wait(30)
    bot.close_browser()

    # dict = {}
    # db.get_value("Select * from ABDUL_TEMP", 100, dict)
    # print(dict[100])







    # lib.wait_until_element_is_visible('xpath://button[text()="Create"]', timeout=30)
    # lib.click_element('xpath://button[text()="Create"]')
    # lib.wait_until_element_is_visible('xpath://img[@title="Add Row"]', timeout=30)
    # lib.scroll_element_into_view('xpath://img[@title="Add Row"]')
    #
    # # lib.scroll_element_into_view('xpath://span[text()="Requested Delivery Date"]')
    # xpath = 'xpath://span[text()="Requested Delivery Date"]'
    #
    # # lib.wait_until_element_is_visible(xpath, timeout=120)
    # # element = lib.get_webelement(xpath)
    # # lib.execute_javascript("arguments[0].scrollIntoView(true);", element)
    # # lib.scroll_element_into_view(xpath)
    # # lib.wait_until_element_is_visible(xpath, timeout=10)
    # # lib.set_focus_to_element(xpath)
    # # lib.click_element(xpath)

# Generic1.take_screenshot(None, bot.get_lib(), 'C:\\Users\\AbdulMalik\\OneDrive - Winfo Solutions\\Desktop\\Python Projects\\Screenshots')
# Generic1.zip_and_unzip_files(self=None, source_folder='Screenshots', zip_file_name='screenshots_zip', extract_folder='Python Projects', operation='zip')
# print(Generic1.create_random_value(None, 6))