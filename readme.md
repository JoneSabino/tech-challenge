# Ripple - Tech Challenge

##### Questions
###### In a few paragraphs, describe your process and results:
- **How does your script work?**  
_It makes an API call to the provided ripple server, gets the  relevant information from the response, writes these two values to a .csv file. It also calculates and prints the min, max and avg times between the validations._
- **How did you decide on your polling interval?**  
_I used 1s interval to have more precision._
- **What do the results tell you?**  
_That a validation takes between 1s and 4s to happen, most of the times_
- **What might explain the variation in time between new ledgers?**  
_The individual transactions are grouped and the validation of the groups run in rounds. So I believe that when the transactions are removed of the current set and moved to the next ledger level version, we can see it as a time increase(3s, 4s) in the plot._
- **Bonus Question 2**  
I found this method: https://xrpl.org/data-api.html#get-ledger  
It has a "close_time" in the response that can be useful.  
Also, there are others like Get Transaction and Get Transactions.
