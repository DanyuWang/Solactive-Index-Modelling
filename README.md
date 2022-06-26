# Assessment Index Modelling

The required input prices can be found at `data_sources\stock_prices.csv`. 

The model output prices can be found at `export.csv`.



# Index Notes

- The index is a stock index made up of imaginary stocks. 
- There are no further corporate actions to consider here 
- The index doesn't resemble any real existing index.
- The model should be able to calculate the index levels based on the rules below.
- All provided prices are total return. 
- All companies got the same amount of shares outstanding.




# Index Rules

- The index is a total return index.

- The index universe consists of all stocks from "Stock_A" to including "Stock_J".

- Every first business day of a month the index selects from the universe the top three stocks based on their market capitalization, based on the close of business values as of the last business day of the immediately preceding month.

- The selected stock with the highest market capitalization gets assigned a 50% weight, while the second and third each get assigned 25%.

- The selection becomes effective close of business on the first business date of each month.

- The index starts with a level of 100.

- The default index start date is January 1st 2020 and end date is Decemeber 31st 2020.

- The index business days are Monday to Friday.

- There are no additional holidays.

  

# Index Model 

- The Index Model class is in the  `index_model/index.py` . The object of Index Class has the attributes of stock prices data, index universe



# Running

Just execute  `__main__.py` in command prompt or other python environment. The result of index would be saved in the given path. If want to modify the file path, please change it in `__main__.py`. 

The only required packages for the model are  `numpy` , `pandas` and `datetime`. 



# Submission

I have sent you the project as a link to my GitHub repo via mail to jobs@solactive.com. 


