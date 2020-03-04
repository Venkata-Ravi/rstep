from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound   #imported to handle http responses
import json   # imported to convert the data into json format which will be used to send the response

# Create your views here.

#The class "CheckServer" is a sample class written to check whether the server is functioning
#properly or not.  It contains one get method in which it displays some value in server and
#returns some value to the client

class CheckServer(View):

    def get(self, request, *args, **kwargs):
	    d = {"Msg" : "Message from server"}
	    print ("This message will be printed in server")
		
	    json_data = json.dumps(d)
	    return HttpResponse(json_data, content_type = 'application/json')

'''
This exercise is handled with only "get" method as we don't have to store any data.
A new class named "Total" is created to handle this functionality.
It contains the below three class methods
        "get": This method handles the server request and returns the response in json format.
               It internally calls private class methods "_callBS", "_calcsum"
    "_callBS": This is a private method created to call the backend service 
	           from where we expect the list of numbers for calculating the total
   "_calcsum": This is another private method created to calculate the sum of all the elements 
               and returns the total.  It expects "integer list of elements" as an input parameter
'''
class Total(View):

    #Class method to handle the get request of the server
    def get(self, request, *args, **kwargs):
        #Calling private method to fetch the list of elements to be summed up.  
        #This list is expected from a backend service.
        lst_values = self._callBS()
 
        #Calling private method by passing the list of values as an argument and fetching the total
        res = self._calcsum(lst_values)

        #creating a dictionary with the returned total
        result = {"Total": res}

        #Converting the dictionary data in to JSON data
        json_data = json.dumps(result)

        #sending the HttpResponse to the client
        return HttpResponse(json_data, content_type = 'application/json')

    def _callBS(self):
        #Hard coding the list of values.  This method can be modified at a later stage to call any 
        #backend service to get the required list of elements
        lv = []
        lv = list(range(10000001))

        #retuning the list of elements to the called method
        return (lv)
		
    def _calcsum(self, lst_values):
        #Intializing the total value to zero
        total = 0

        #looping through all the values in the list and summing up in "total"
        for val in lst_values:
            total += val

        #returning the summed up value to the called method
        return total
