import doctest


def test_chapter12_deploying_slow():
    """

    >>> import playsound
    >>> playsound.playsound('hello.mp3')

    """

def test_chapter13_web_scraping_slow():
    """
    >>> import requests
    >>> response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    >>> type(response)
    <class 'requests.models.Response'>
    >>> response.status_code == requests.codes.ok
    True
    >>> len(response.text)
    178978



    >>> import requests
    >>> response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    >>> response.raise_for_status()
    >>> with open('RomeoAndJuliet.txt', 'wb') as play_file:
    ...     for chunk in response.iter_content(100000):
    ...         play_file.write(chunk)
    ...
    100000
    78978

    >>> import os;os.unlink('RomeoAndJuliet.txt')

    >>> import auto3esecrets
    >>> import requests
    >>> city_name = 'San Francisco'
    >>> state_code = 'CA'
    >>> country_code = 'US'
    >>> API_key = auto3esecrets.openweatherkey
    >>> response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
    >>> #response.text
    >>> import json
    >>> response_data = json.loads(response.text)
    >>> #response_data # This is a Python data structure.
    >>> response_data[0]['lat']
    37.7790262
    >>> response_data[0]['lon']
    -122.419906

    >>> import requests, bs4
    >>> res = requests.get('https://autbor.com/example3.html')
    >>> res.raise_for_status()
    >>> example_soup = bs4.BeautifulSoup(res.text)
    >>> type(example_soup)
    <class 'bs4.BeautifulSoup'>


    >>> from selenium import webdriver
    >>> from selenium.webdriver.common.by import By
    >>> browser = webdriver.Firefox()
    >>> browser.get('https://autbor.com/example3.html')
    >>> link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
    >>> type(link_elem)
    <class 'selenium.webdriver.remote.webelement.WebElement'>
    >>> link_elem.click() # Follows the "This text is a link" link


    >>> from selenium import webdriver
    >>> browser = webdriver.Firefox()
    >>> type(browser)
    <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
    >>> browser.get('https://inventwithpython.com')

    >>> browser.close()


    >>> from selenium import webdriver
    >>> from selenium.webdriver.common.by import By
    >>> browser = webdriver.Firefox()
    >>> browser.get('https://autbor.com/example3.html')
    >>> link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
    >>> type(link_elem)
    <class 'selenium.webdriver.remote.webelement.WebElement'>
    >>> link_elem.click() # Follows the "This text is a link" link

    >>> browser.close()


    >>> from selenium import webdriver
    >>> from selenium.webdriver.common.by import By
    >>> browser = webdriver.Firefox()
    >>> browser.get('https://autbor.com/example3.html')
    >>> user_elem = browser.find_element(By.ID, 'login_user')
    >>> user_elem.send_keys('your_real_username_here')
    >>> password_elem = browser.find_element(By.ID, 'login_pass')
    >>> password_elem.send_keys('your_real_password_here')
    >>> password_elem.submit()

    >>> browser.close()


    >>> from selenium import webdriver
    >>> from selenium.webdriver.common.by import By
    >>> from selenium.webdriver.common.keys import Keys
    >>> browser = webdriver.Firefox()
    >>> browser.get('https://nostarch.com')
    >>> html_elem = browser.find_element(By.TAG_NAME, 'html')
    >>> html_elem.send_keys(Keys.END) # Scrolls to bottom
    >>> html_elem.send_keys(Keys.HOME) # Scrolls to top

    >>> browser.close()



    >>> from playwright.sync_api import sync_playwright
    >>> playwright = sync_playwright().start()
    >>> browser = playwright.firefox.launch(headless=False, slow_mo=50)
    >>> page = browser.new_page()
    >>> page.goto('https://autbor.com/example3.html')
    <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
    >>> browser.close()
    >>> playwright.stop()


    >>> from playwright.sync_api import sync_playwright
    >>> playwright = sync_playwright().start()
    >>> browser = playwright.firefox.launch(headless=False, slow_mo=50)
    >>> page = browser.new_page()
    >>> page.goto('https://autbor.com/example3.html')
    <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
    >>> page.click('input[type=checkbox]') # Checks the checkbox.
    >>> page.click('input[type=checkbox]') # Unchecks the checkbox.
    >>> page.click('a') # Clicks the link.
    >>> page.go_back()
    <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
    >>> checkbox_elem = page.get_by_role('checkbox') # Calls a Locator method.
    >>> checkbox_elem.check() # Checks the checkbox.
    >>> checkbox_elem.uncheck() # Unchecks the checkbox.
    >>> checkbox_elem.set_checked(True) # Checks the checkbox.
    >>> checkbox_elem.set_checked(False) # Unchecks the checkbox.
    >>> page.get_by_text('is a link').click() # Uses Locator method.
    >>> browser.close()
    >>> playwright.stop()


    >>> from playwright.sync_api import sync_playwright
    >>> playwright = sync_playwright().start()
    >>> browser = playwright.firefox.launch(headless=False, slow_mo=50)
    >>> page = browser.new_page()
    >>> page.goto('https://autbor.com/example3.html')
    <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
    >>> page.locator('#login_user').fill('your_real_username_here')
    >>> page.locator('#login_pass').fill('your_real_password_here')
    >>> page.locator('input[type=submit]').click()
    >>> browser.close()
    >>> playwright.stop()


    >>> from playwright.sync_api import sync_playwright
    >>> playwright = sync_playwright().start()
    >>> browser = playwright.firefox.launch(headless=False, slow_mo=50)
    >>> page = browser.new_page()
    >>> page.goto('https://autbor.com/example3.html')
    <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
    >>> page.locator('html').press('End') # Scrolls to bottom
    >>> page.locator('html').press('Home') # Scrolls to top
    >>> browser.close()
    >>> playwright.stop()

    """



def test_chapter15_google_sheets_slow():
    """
    >>> import ezsheets
    >>> ss = ezsheets.Spreadsheet()
    >>> ss.title = 'Title of My New Spreadsheet'
    >>> ss.title
    'Title of My New Spreadsheet'
    >>> ss.delete(permanent=True) # TEST CLEAN UP


    >>> import ezsheets
    >>> ss1 = ezsheets.Spreadsheet('https://autbor.com/examplegs')
    >>> ss2 = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI/')
    >>> ss3 = ezsheets.Spreadsheet('1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI')
    >>> ss1 == ss2 == ss3 # These are the same spreadsheet.
    True



    >>> import ezsheets
    >>> ss = ezsheets.upload('my_spreadsheet.xlsx')
    >>> ss.title
    'my_spreadsheet'
    >>> ss.delete(permanent=True) # TEST CLEAN UP


    >>> import ezsheets
    >>> example_ss = ezsheets.Spreadsheet('https://autbor.com/examplegs')
    >>> ss = ezsheets.Spreadsheet()
    >>> example_ss.sheets[0].copyTo(ss)
    >>> ss.sheets[0].delete() # Delete the Sheet1 sheet.




    >>> import ezsheets
    >>> example_ss = ezsheets.Spreadsheet('https://autbor.com/examplegs')
    >>> ss = ezsheets.Spreadsheet()
    >>> example_ss.sheets[0].copyTo(ss)
    >>> ss.sheets[0].delete() # Delete the Sheet1 sheet.

    >>> ss.title # The title of the spreadsheet.
    'Untitled spreadsheet'
    >>> ss.title = 'Sweigart Books' # Change the title.
    >>> DUMMY = ss.id # The unique ID (this is a read-only attribute).
    >>> DUMMY = ss.url # The URL (a read-only attribute).
    >>> ss.sheetTitles # The titles of all the Sheet objects
    ('Copy of Books',)
    >>> DUMMY = ss.sheets # The Sheet objects in this Spreadsheet, in order.
    >>> DUMMY = ss.sheets[0] # The first Sheet object in this Spreadsheet.
    >>> DUMMY = ss['Copy of Books'] # Sheets can also be accessed by title.
    >>> DUMMY = ss.Sheet('New blank sheet') # Create a new sheet.
    >>> ss.sheets[1].delete() # Delete the second Sheet object in this Spreadsheet.

    >>> ss.refresh()




    >>> import ezsheets
    >>> ss = ezsheets.Spreadsheet('https://autbor.com/examplegs')
    >>> ss.title
    'Sweigart Books (DO NOT DELETE)'
    >>> ss.downloadAsExcel() # Downloads the spreadsheet as an Excel file.
    'Sweigart_Books_(DO_NOT_DELETE).xlsx'
    >>> ss.downloadAsODS() # Downloads the spreadsheet as an OpenOffice file.
    'Sweigart_Books_(DO_NOT_DELETE).ods'
    >>> ss.downloadAsCSV() # Only downloads the first sheet as a CSV file.
    'Sweigart_Books_(DO_NOT_DELETE).csv'
    >>> ss.downloadAsTSV() # Only downloads the first sheet as a TSV file.
    'Sweigart_Books_(DO_NOT_DELETE).tsv'
    >>> ss.downloadAsPDF() # Downloads the spreadsheet as a PDF.
    'Sweigart_Books_(DO_NOT_DELETE).pdf'
    >>> ss.downloadAsHTML() # Downloads the spreadsheet as a ZIP of HTML files.
    'Sweigart_Books_(DO_NOT_DELETE).zip'

    >>> import os;os.unlink('Sweigart_Books_(DO_NOT_DELETE).xlsx')
    >>> import os;os.unlink('Sweigart_Books_(DO_NOT_DELETE).ods')
    >>> import os;os.unlink('Sweigart_Books_(DO_NOT_DELETE).csv')
    >>> import os;os.unlink('Sweigart_Books_(DO_NOT_DELETE).tsv')
    >>> import os;os.unlink('Sweigart_Books_(DO_NOT_DELETE).pdf')
    >>> import os;os.unlink('Sweigart_Books_(DO_NOT_DELETE).zip')


    >>> import ezsheets
    >>> ss = ezsheets.Spreadsheet() # Create the spreadsheet.
    >>> DUMMY = ezsheets.listSpreadsheets() # Confirm that we've created a spreadsheet.
    >>> ss.delete() # Delete the spreadsheet.
    >>> DUMMY = ezsheets.listSpreadsheets() # Spreadsheets in the Trash folder are still listed.

    >>> ss = ezsheets.Spreadsheet() # Create the spreadsheet.
    >>> ss.delete(permanent=True)
    >>> DUMMY = ezsheets.listSpreadsheets()



    >>> import ezsheets
    >>> ss = ezsheets.Spreadsheet() # Starts with a sheet named Sheet1.
    >>> sheet2 = ss.Sheet('Spam')
    >>> sheet3 = ss.Sheet('Eggs')
    >>> DUMMY = ss.sheets # The Sheet objects in this Spreadsheet, in order.
    >>> ss.sheets[0] # Gets the first Sheet object in this Spreadsheet.
    <Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>
    >>> ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet.
    ('Sheet1', 'Spam', 'Eggs')
    >>> ss.delete(permanent=True) # TEST CLEAN UP


    >>> import ezsheets
    >>> ss = ezsheets.Spreadsheet()
    >>> ss.title = 'My Spreadsheet'
    >>> sheet = ss.sheets[0] # Get the first sheet in this spreadsheet.
    >>> sheet.title
    'Sheet1'
    >>> sheet['A1'] = 'Name' # Set the value in cell A1.
    >>> sheet['B1'] = 'Age'
    >>> sheet['C1'] = 'Favorite Movie'
    >>> sheet['A1'] # Read the value in cell A1.
    'Name'
    >>> sheet['A2'] # Empty cells return a blank string.
    ''
    >>> sheet[2, 1] # Column 2, Row 1 is the same address as B1.
    'Age'
    >>> sheet['A2'] = 'Alice'
    >>> sheet['B2'] = 30
    >>> sheet['C2'] = 'RoboCop'
    >>> sheet['B2'] # Note that all data is returned as strings.
    '30'
    >>> ss.delete(permanent=True) # TEST CLEAN UP




    >>> import ezsheets
    >>> ezsheets.convertAddress('A2') # Converts addresses...
    (1, 2)
    >>> ezsheets.convertAddress(1, 2) # ...and converts them back, too.
    'A2'
    >>> ezsheets.getColumnLetterOf(2)
    'B'
    >>> ezsheets.getColumnNumberOf('B')
    2
    >>> ezsheets.getColumnLetterOf(999)
    'ALK'
    >>> ezsheets.getColumnNumberOf('ZZZ')
    18278


    >>> import ezsheets
    >>> ss = ezsheets.upload('produceSales.xlsx')
    >>> sheet = ss.sheets[0]
    >>> sheet.getRow(1) # The first row is row 1, not row 0.
    ['PRODUCE', 'COST PER POUND', 'POUNDS SOLD', 'TOTAL', '', '']
    >>> sheet.getRow(2)
    ['Potatoes', '0.86', '21.6', '18.58', '', '']
    >>> DUMMY = sheet.getColumn(1)
    >>> DUMMY = sheet.getColumn('A') # The same result as getColumn(1)
    >>> sheet.getRow(3)
    ['Okra', '2.26', '38.6', '87.24', '', '']
    >>> sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
    >>> sheet.getRow(3)
    ['Pumpkin', '11.50', '20', '230', '', '']
    >>> columnOne = sheet.getColumn(1)
    >>> for i, value in enumerate(columnOne):
    ...  # Make the Python list contain uppercase strings:
    ...  columnOne[i] = value.upper()
    ...
    >>> sheet.updateColumn(1, columnOne) # Update the entire column in one request.

    >>> rows = sheet.getRows() # Get every row in the spreadsheet.
    >>> rows[0] # Examine the values in the first row.
    ['PRODUCE', 'COST PER POUND', 'POUNDS SOLD', 'TOTAL', '', '']
    >>> rows[1]
    ['POTATOES', '0.86', '21.6', '18.58', '', '']
    >>> rows[1][0] = 'PUMPKIN' # Change the produce name.
    >>> rows[1]
    ['PUMPKIN', '0.86', '21.6', '18.58', '', '']
    >>> rows[10]
    ['OKRA', '2.26', '40', '90.4', '', '']
    >>> rows[10][2] = '400' # Change the pounds sold.
    >>> rows[10][3] = '904' # Change the total.
    >>> rows[10]
    ['OKRA', '2.26', '400', '904', '', '']
    >>> sheet.updateRows(rows) # Update the online spreadsheet with the changes.


    >>> sheet.rowCount # The number of rows in the sheet.
    23758
    >>> sheet.columnCount # The number of columns in the sheet.
    6
    >>> sheet.columnCount = 4 # Change the number of columns to 4.
    >>> sheet.columnCount # Now the number of columns in the sheet is 4.
    4

    >>> ss.delete(permanent=True) # TEST CLEAN UP




    >>> import ezsheets
    >>> ss = ezsheets.Spreadsheet()
    >>> ss.title = 'Multiple Sheets'
    >>> ss.sheetTitles
    ('Sheet1',)
    >>> DUMMY = ss.Sheet('Spam') # Create a new sheet at the end of the list of sheets.
    >>> DUMMY = ss.Sheet('Eggs') # Create another new sheet.
    >>> ss.sheetTitles
    ('Sheet1', 'Spam', 'Eggs')
    >>> DUMMY = ss.Sheet('Bacon', 0) # Create a sheet at index 0 in the list of sheets.
    >>> ss.sheetTitles
    ('Bacon', 'Sheet1', 'Spam', 'Eggs')

    >>> ss.sheetTitles
    ('Bacon', 'Sheet1', 'Spam', 'Eggs')
    >>> ss.sheets[0].index
    0
    >>> ss.sheets[0].index = 2 # Move the sheet at index 0 to index 2.
    >>> ss.sheetTitles
    ('Sheet1', 'Spam', 'Bacon', 'Eggs')
    >>> ss.sheets[2].index = 0 # Move the sheet at index 2 to index 0.
    >>> ss.sheetTitles
    ('Bacon', 'Sheet1', 'Spam', 'Eggs')

    >>> ss.sheetTitles
    ('Bacon', 'Sheet1', 'Spam', 'Eggs')
    >>> ss.sheets[0].delete() # Delete the sheet at index 0: the "Bacon" sheet.
    >>> ss.sheetTitles
    ('Sheet1', 'Spam', 'Eggs')
    >>> ss['Spam'].delete() # Delete the "Spam" sheet.
    >>> ss.sheetTitles
    ('Sheet1', 'Eggs')
    >>> sheet = ss['Eggs'] # Assign a variable to the "Eggs" sheet.
    >>> sheet.delete() # Delete the "Eggs" sheet.
    >>> ss.sheetTitles
    ('Sheet1',)
    >>> ss.sheets[0].clear() # Clear all the cells on the "Sheet1" sheet.
    >>> ss.sheetTitles # The "Sheet1" sheet is empty but still exists.
    ('Sheet1',)

    >>> ss.delete(permanent=True) # TEST CLEAN UP



    >>> import ezsheets
    >>> ss1 = ezsheets.Spreadsheet()
    >>> ss1.title = 'First Spreadsheet'
    >>> ss1.sheets[0].title = 'Spam' # ss1 will have a sheet named Spam.
    >>> ss2 = ezsheets.Spreadsheet()
    >>> ss2.title = 'Second Spreadsheet'
    >>> ss2.sheets[0].title = 'Eggs' # ss2 will have a sheet named Eggs.
    >>> ss1[0]
    <Sheet sheetId=0, title='Spam', rowCount=1000, columnCount=26>
    >>> ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
    >>> ss1[0].copyTo(ss2) # Copy the ss1's Sheet1 to the ss2 spreadsheet.
    >>> ss2.sheetTitles # ss2 now contains a copy of ss1's Sheet1.
    ('Eggs', 'Copy of Spam')

    >>> ss1.delete(permanent=True) # TEST CLEAN UP
    >>> ss2.delete(permanent=True) # TEST CLEAN UP

    """

    # TODO: Test "Project: Fake Blockchain Cryptocurrency Scam"



if __name__ == '__main__':
    doctest.testmod()

