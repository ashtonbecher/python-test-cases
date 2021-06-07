# python-test-cases
 Set of automated test cases for use with Selenium

# Installation
 1. Install selenium using pip (see requirements.txt)
     * open Powershell or CMD and type: 
	*`pip install selenium`
 2. Ensure desired webdriver dependencies are installed to your PATH
     * IF YOU DO NOT HAVE AN EXISTING WEBDRIVER PATH: 
	* create or use an existing location for your webdriver libraries (in the example here, I will use C:\Webdriver\bin)
	* open Powershell or CMD and type: 
	    *`setx /m path "%path%;C:\WebDriver\bin\"`
 3. Place any webdriver files (such as chromedriver for Chrome) into the folder you created in step 2
 4. To ensure the install worked correctly, you can type the name of the binaries you installed in Powershell or CMD

# Expected output of a failed test case
 * Traceback logs should appear in Pycharm console with a message like:
     * `selenium.common.exceptions.TimeoutException: Message`

 * Passing test cases will not show any message and will be marked as 'Passed' in the PyCharm console

# Other information
 * Python version - 3.9.5
 * Selenium version - 3.141.0
 * Chromedriver version - 91.0.4472.19
 * Chrome version - 91
 
 * Tested on Windows 10




