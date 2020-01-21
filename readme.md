# Ripple - Tech Challenge

##### Questions
###### In a few paragraphs, describe your process and results:
- How does your script work?  
It makes an API call to the provided ripple server, gets the  relevant information from the response and also the current local time and writes these two values to a .csv file
- How did you decide on your polling interval?  
I observed that normally it takes 3 seconds to have a new sequence number.
- What do the results tell you?  
That a validation takes around 3s to happen.
- What might explain the variation in time between new ledgers? (this description of the consensus algorithm may help you: https://developers.ripple.com/consensus-principles-and-rules.html)  
The individual transactions are grouped and the validation of the groups run in rounds. So I believe that when the transactions are removed of the current set and moved to the next ledger level version, we can see it as a time increase(4s, 5s) in the plot.