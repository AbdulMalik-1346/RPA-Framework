import time

from Oracle import Oracle
from SeleniumLibrary import SeleniumLibrary


def application_navigator(process_name, application_name):
    db = Oracle()
    lib = SeleniumLibrary()
    applications_df = db.get_application_df()
    locators_df = db.get_locators_df()
    wb_processes_df = db.get_wb_processes_df()
    wb_processes_steps_cfg_df = db.get_wb_processes_steps_cfg_df()
    filtered_wb_processes_steps_cfg_df = db.get_filter_wb_processes_cfg(wb_processes_df, wb_processes_steps_cfg_df, application_name, process_name)

    for index, data_row in filtered_wb_processes_steps_cfg_df.iterrows():
        selector = data_row['SELECTOR']
        action = data_row['ACTION']
        input_parameter = data_row['INPUT_PARAMETER']
        step_no = int(data_row['STEP_NO'])
        action_navigator(db, step_no, input_parameter, selector, action, 'Chrome', applications_df, locators_df)
        time.sleep(1)

    db.conn.close()


def action_navigator(db, step_no, input_parameter, selector, action, application_name, applications_df, locators_df):
    match action:
        case 'None':
            print("Do nothing")
        case 'Logout':
            print("Perform Logout")
        case 'Login':
            print("Perform Login")
        case 'DropDown':
            print("Handle Dropdown")
        case 'Send Mail':
            print("Send Mail")
        case 'Expand or Collapse':
            print("Expand or Collapse")
        case 'Compare':
            print("Compare")
        case 'APTB Data Extraction':
            print("APTB Data Extraction")
        case 'Submit Rec Reports - AP':
            print("Submit Rec Reports - AP")
        case 'Insert Steps PCP':
            print("Insert Steps PCP")
        case 'Winbot Data Extraction':
            print("Winbot Data Extraction")
        case 'Kill Application':
            print("Kill Application")
        case 'Download Sharepoint File':
            print("Download Sharepoint File")
        case 'Get Text':
            print("Get Text")
        case 'Contract Close':
            print("Contract Close")
        case 'Wait For Element':
            print("Wait For Element")
        case 'Radio Button':
            print("Radio Button")
        case 'Insert Value - Excel':
            print("Insert Value - Excel")
        case 'Click':
            print("Click")
        case 'Keyboard Input':
            print("Keyboard Input")
        case 'Submit Form Function':
            print("Submit Form Function")
        case 'Process Confirmation':
            print("Process Confirmation")
        case 'Reconciliation Without TB':
            print("Reconciliation Without TB")
        case 'Send Status Mail':
            print("Send Status Mail")
        case 'Get value - ExcelDt':
            print("Get value - ExcelDt")
        case 'Expense Auditing':
            print("Expense Auditing")
        case 'Get Filename':
            print("Get Filename")
        case 'Download - Sharepoint':
            print("Download - Sharepoint")
        case 'Upload - Sharepoint':
            print("Upload - Sharepoint")
        case 'Get Value - Excel':
            print("Get Value - Excel")
        case 'Open Task':
            print("Open Task")
        case 'Capture Error':
            print("Capture Error")
        case 'Assign Value':
            print("Assign Value")
        case 'Read DataBase':
            print("Read DataBase")
        case 'Add Data to Queue':
            print("Add Data to Queue")
        case 'Select Table Row':
            print("Select Table Row")
        case 'Submit Reports Method':
            print("Submit Reports Method")
        case 'Reconcillation-AP':
            print("Reconcillation-AP")
        case 'TBPivot':
            print("TBPivot")
        case 'Exception Transactions':
            print("Exception Transactions")
        case 'WD-1 Reconciliation With TB':
            print("WD-1 Reconciliation With TB")
        case 'Data Validation':
            print("Data Validation")
        case 'Wait For Request':
            print("Wait For Request")
        case 'Mass Addition':
            print("Mass Addition")
        case 'Click Link':
            print("Click Link")
        case 'Tab':
            print("Tab")
        case 'Log Out':
            print("Log Out")
        case 'Select Date':
            print("Select Date")
        case 'Open Excel':
            print("Open Excel")
        case 'Convert Date Time':
            print("Convert Date Time")
        case 'Disconnect-VPN':
            print("Disconnect-VPN")
        case 'Insert Row-DataTable':
            print("Insert Row-DataTable")
        case 'Get Sharepoint Link':
            print("Get Sharepoint Link")
        case 'Read File':
            print("Read File")
        case 'delay':
            print("Delay")
        case 'Get Email Address':
            print("Get Email Address")
        case 'Read Files In Folder':
            print("Read Files In Folder")
        case 'Download - SharePoint':
            print("Download - SharePoint")
        case 'DownloadDBData':
            print("DownloadDBData")
        case 'Switch Responsibilities':
            print("Switch Responsibilities")
        case 'Form Function':
            print("Form Function")
        case 'Contract Validation':
            print("Contract Validation")
        case 'Upload - EBS':
            print("Upload - EBS")
        case 'Button Dropdown':
            print("Button Dropdown")
        case 'Text Field':
            print("Text Field")
        case 'Get Value - DB':
            print("Get Value - DB")
        case 'Copy Text':
            print("Copy Text")
        case 'Read and Write lines Range':
            print("Read and Write lines Range")
        case 'Hover Element':
            print("Hover Element")
        case 'Select Report':
            print("Select Report")
        case 'Table Filter':
            print("Table Filter")
        case 'Connect-VPN':
            print("Connect-VPN")
        case 'Send Mail Attachments':
            print("Send Mail Attachments")
        case 'Increment Value':
            print("Increment Value")
        case 'Upload Sharepoint File':
            print("Upload Sharepoint File")
        case 'AP Reconciliation':
            print("AP Reconciliation")
        case 'Read Mail':
            print("Read Mail")
        case 'GetFullPath':
            print("GetFullPath")
        case 'Project Validation':
            print("Project Validation")
        case 'Custom Internal':
            print("Custom Internal")
        case 'Project Close':
            print("Project Close")
        case 'Select DropDown':
            print("Select DropDown")
        case 'Text Area':
            print("Text Area")
        case 'Insert Value - DB':
            print("Insert Value - DB")
        case 'Read Data':
            print("Read Data")
        case 'Wait for Element':
            print("Wait for Element")
        case 'Click Text':
            print("Click Text")
        case 'HTML Table':
            print("HTML Table")
        case 'Create DataTable':
            print("Create DataTable")
        case 'Full Path':
            print("Full Path")
        case 'GetExcelSheets':
            print("GetExcelSheets")
        case 'ZipUnZip Files':
            print("ZipUnZip Files")
        case 'Check Unacconted Transactions':
            print("Check Unacconted Transactions")
        case 'Multiple Click':
            print("Multiple Click")
        case 'Billing Offset':
            print("Billing Offset")
        case 'Click Button':
            print("Click Button")
        case 'Create Random Value':
            print("Create Random Value")
        case 'Enter':
            print("Enter")
        case 'Navigation':
            print("Navigation")
        case 'Page Tab':
            print("Page Tab")
        case 'Ribbon Tab':
            print("Ribbon Tab")
        case 'Select Date Time':
            print("Select Date Time")
        case 'Search Item':
            print("Search Item")
        case 'Submit Request':
            print("Submit Request")
        case 'Delay':
            print("Delay")
        case 'Get Format ID':
            print("Get Format ID")
        case 'Custom':
            print("Custom")
        case 'RegEx':
            print("RegEx")
        case 'Click Data in Table':
            print("Click Data in Table")
        case 'Click Image':
            print("Click Image")
        case 'Update Value - DB':
            print("Update Value - DB")
        case 'Create Windows Folder':
            print("Create Windows Folder")
        case 'Copy Excel Sheet':
            print("Copy Excel Sheet")
        case 'Click CheckBox':
            print("Click CheckBox")
        case 'Screenshot':
            print("Screenshot")
        case 'Copy Excel':
            print("Copy Excel")
        case 'Update Value':
            print("Update Value")
        case 'Genarate CSV':
            print("Generate CSV")
        case 'Upload File':
            print("Upload File")
        case 'Save File':
            print("Save File")
        case 'Select DataBase Data':
            print("Select DataBase Data")
        case 'Switch Application':
            print("Switch Application")
        case 'Get Header Id':
            print("Get Header Id")
        case _:
            print("Unknown action")


if __name__ == '__main__':
    application_navigator('Period Close Process', 'Oracle EBS')
