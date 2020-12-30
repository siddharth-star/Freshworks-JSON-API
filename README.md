# Freshworks-JSON-API
The snapshots of the execution of all the commands are attached here in the repository.
Step1:
Execute the python file. 

Make sure to always enter a valid input otherwise you will get the error as:
"please enter a valid input"

Step2:
You have to choose the option for file path.
1.Default path 
2.User defined path

If you choose the "1." option then a userDetails.json file will be created in the same folder in which you executed the python file final.py otherwise if you choose the option "2.", then the userDetails.json file will be created in the directory which will be the desired directory according to the path given as input by the user from the current directory.

Make sure that the path given is in the required format or else  the system will instruct you to write the path in the format as given below:
Enter the path in this format : --/--/--

Step3:
Choose option for operation
1.Create data
2.Delete data 
3.Read data 
4.Read All
5.Exit

If you choose the option -"1."
To create data :
a. Enter the id : sid 
b. Enter the live time of request : 200(in seconds)
c. Enter the name : Siddharth

Make sure that the id is in range of 32 chars and if not, it will display the error as :
"Enter a key under 32 character"
Also make sure that the id that you enter does not already exist in the system , in such case , it will display the error as :
"Key already exists"

If you choose the option -"2."
To delete the data , make sure that the deletion operation is performed within the timestamp otherwise you will get the following error:
"This Key does not exist due to Time Stamp"
If you perform the delete operation within the timestamp then the key will be deleted.

If you choose the option -"3."
To read the data , make sure that the the read operation is performed within the timestamp otherwise you will get the following error:
"This Key does not exist due to Time Stamp"
If the key you input does not exist then it will display the following error:
"Key does not exist"
If you perform the read operation within the timestamp and the key exist,then the data about the entered key as input will be displayed.
Enter the key which you want to read : sidhya
{
  "_id": "sidhya",
  "life_time": "200",
  "name": "yashi",
  "time_build": "1609305599"
}

If you choose the option -"4."
It will display data associated with all the keys.

If you choose the option - "5."
The program will get exit.
