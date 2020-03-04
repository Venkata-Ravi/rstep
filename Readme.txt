Framework:
This exercise is handled by choosing Django framework to bring up webserver.

Approach:
This exercise is handled in two ways.
	1. By calling the APIs using web browser.
	2. By calling the APIs using a standalone application.  This standalone application is written in python 
	   by using the python library "requests".
    3. This entire exercise is handled using "GET" functionality of API as we don't have to post any data.	   
	   
Implementation:

Calling API using Web Browser:
	1. A new project is created using "Django" commands to handle this exercise.
	2. The APIs created in this exercise are class based APIs.
	3. A set of new class's are created in the file "views.py"
	4. To access the urls, the newly created project is added in "urls.py"
	5. urlpatterns section is edited in "urls.py" to add the api end points.
	6. Detailed explanation of code is been provided at all the places in "views.py"

Calling API using standalone application:
	1. A new python file named "test.py" is created in the same project for convenience
	2. The "requests" library is used in this file to handle the server requests.
	3. This code is totally written using Python 3 supported libraries and no framework specific code is used.
	4. It calls the get method in server and fetches the response.  If the server call is successful it
	   prints the response in the console.  In case of an exception, the details of the exception will be 
	   printed in the console.

Testing:
	1. Start the web server
	
	2. Using web browser:
       i) Ensure web server is running
      ii) Open any web browser (Chrome/IE/Firefox etc)
     iii) In the URLs box simply enter the api endpoint as mentioned below.
	      http://127.0.0.1:8000/total/
      iv) Expected Result: The below details will be displayed in the browser
	      {"Total": 50000005000000}
	   v) Actual Result: The expected result is displayed (in my browser during unit testing)
	
	3. Using Standalone application:
	   i) Ensure web server is running
	  ii) Open the command prompt
	 iii) Navigate to the path in which the file "test.py" is stored.
	  iv) Run the python file using the following command
	      python test.py
	   v) Expected Result: The below details will be displayed in the command window.
	      {'Total': 50000005000000}
	  vi) Actual Result: The expected result is displayed (in my command window during unit testing)
	  
Assumptions:
1. It is assumed that the list of elements will be provided by the backend service and hence hard coded 
   the same as a class method in server.  
2. It is assumed that the list will be properly provided by the backend service and hence no cross checking
   code (ex: length of the list, type of elements in the list) or exception handling is done in server programming.