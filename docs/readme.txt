Content

1: Program Functions
2: How to Run
3: Assumptions
4: Rational and Misc Notes

___________________________________________________________________________________________
===========================================================================================
===========================================================================================
1: Program Functions
	The purpose of this program is to take an input from a CSV file that has data 
	recorded as hourly running totals and de-accumulate that data into individual data 
	points. The data is then written to a CSV file with the original file name + Output
	and stored in the output folder. CSV files can be run in batches.

===========================================================================================
===========================================================================================

2: Running the program
	1: Copy chosen CSV files into the "src/csv_files/input" directory.
	2: Open command prompt and move to the "src" directory.
	3: If python.exe is in the PATH environment variable type "python.exe "__main__.py"
	   If python is not in the PATH environment variable replace python.exe with the absolute
	   path to python.exe

	The output file will be created in the output directory
		
===========================================================================================
===========================================================================================	

3: Assumptions
	The customers database contains a table with the same layout as the supplied CSV
	The measurements are from Pennsylvania, USA so it is assumed they are in inches
	The CSV files provided in future will be comma delimited 
	Any machine running the scripts will have Python3 installed
	Any further development will be written in Python3 not Python2
	Operators of the script have an understanding of invalid data 
	Added data could go back as far as the unix Epoch (time = 0)

===========================================================================================
===========================================================================================
4: Rational and Misc Notes
	A test file has been added to run logic tests in the event of future refactoring.

	A maximum to the rain collection data was considered but not added. The world 
	record of 12 inches in an hour was considered, but rainfall greater than that is 
	possible albiet extremely unlikely in Pennsylvania. Any buffer added to the record
	would be pure speculation and scientifically unsound.  

	IO scripts could changed to remove/ignore data and time values that are not sensible
	but I decided on throwing exceptions and exiting as any operator of the script should 
	be informed of invalid data. A compromise would be to catch the exception and print
	the issue, but an operator may not check the error log if they get an output csv.

	I considered adding argument inputs to give the user more control of how the script
	runs (such as choosing output names/directories) but decided that simplicity is more 
	useful, and adding unnecessary parameters would decrease usability. 

	The given data had a few limitations that made it unideal for testing functionality
	properly. Every record was recorded at 12:00am and was seperated by at least a day.
	This meant that there was no hourly running totals to deaccumulate and any peak thirty
	minute would simply be the peak record. The data_generation script generated realistic
	data that created a running total if the new data points occurred within the same hour.

	The peak thirty minute data is returned through the console. This was chosen as it is 
	the cleanest way to display the data. Alternatives would be simple to implement should
	the client want it returned in another format.

	All data manipulation is input independent. To run an SQL database or API, create 
	an IO script to convert the chosen data into a list of tuples and to convert the 
	tuples back for the output. A the 'main' file can be edited to run other input 
	types with if statements and arguments. 

	

	

