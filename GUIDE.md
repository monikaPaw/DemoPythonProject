                Automation Framework Details
(Python, Selenium, Pytest, Page Object Model, HTML Reports)
###	Installable Packages, Libraries, and plugins 
    - 	Python
    -   Selenium: Selenium Libraries
    - 	Pytest: Python unit test framework
    -	pytest-html: For pytest html reports
    -	pytest-xdist: Run test in parallel
    -	openpyxl: For MS Excel support


 
###	Details about packages and folders
    -	pageObjects-This package having classes according to pages of the application under test. That classes has Web Elements and   methods to perform actions on them for that class.
    - testCases-This package having all the test cases for application under test.
    - utilities -This package having classes with reusable methods. Which we can use all over the framework.
	- TestData- This is folder which consist of test data XL file for data driven test cases
    - Reports- This is folder which will have test execution reports in HTML format.
    -Logs- This folder will have logs captured while running test case.
    -Screenshots -This is folder where screenshots of failure will get stored.
    -Configurations- This folder is having config.ini file which is having commonly used data for testing.

###	Framework Features with commands to exescute it
 	-Test cases can run from command line.
     Command: pytest -s -v --html=./Reports/report.html testCases/ --browser chrome
    -Test cases can run on multiple browsers which are chrome,   Firefox, and opera. Need to pass browser name from command line while  running as follow.
      Command: pytest -s -v testCases/ --browser chrome
	-In framework html report will get generated with all logs in report folder.
     Command-pytest -s -v --html=./Reports/report.html testCases/ --browser chrome.
    -Test Can run in parallel using below command. In command ‘n’ will represent number of instances of browser.
     Command: pytest -s -v n=2 --html=./Reports/report.html testCases/ --browser chrome.
    - In framework can test application for data driven test cases , for data driven added XL sheet of data which will provide data to test cases for different scenarios.
    - In framework screenshots will get captured on failure.
    - Can run test suite by grouping test cases on functionality. Added group tags as smoke and regression.
     Command: pytest -s -v -m "smoke" testCases/ --browser chrome

### Steps to Run Test cases from Command Prompt with .bat file
               1. Install Python to your machine 
               2.Install pytest (Open CMD type pip install pytest)
               3.Add selenium (In CMD type pip install selenium)
               4.Add webdriver_manager (On CMD type pip install webdriver_manager)
               5. Add pytest-html - (On CMD type pip install pytest-html)
               6.Add openpyxl – (On CMD type pip install openpyxl) 
               7.Double click on .bat file it will start execution




 6. Test cases added to automate application           
     1.	test_homepage_title
     2.	test_login_valid
     3.	test_login_invalid
     4.	test_login_ddt
     5.	test_order_product
     6.	test_remove_product_from_cart    
     7.	test_add_all_products_to_cart 
     8.	test_validate_logout_application

Sr. No	Test Case name	Status
1	test_homepage_title	Passed
2	test_login_valid	Passed
3	test_login_invalid	Passed
4	test_login_ddt	Passed
5	test_order_product	Passed
6	test_remove_product_from_cart	Passed
7	test_add_all_products_to_cart	Passed
8	test_validate_logout_application	Passed

#Test cases are automated with `performance_glitch_user`.


Note: All the required software and libraries are open source.
















 








  
   
                          

            


  





                         






 



      



   

       
                  
