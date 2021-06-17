Step 1: Open Anaconda Prompt 
              We need to go to our file location and type in prompt as cd Desktop\Privacyecommerce\Privacyecommerce\blockchain
Then type python blockchain.py
 It will give a address. We need to copy & paste in our browser.

Step 2: Open Anaconda Prompt 
              We need to go to our file location and type in prompt as cd Desktop\Privacyecommerce\Privacyecommerce\blockchain
Then type python blockchain.py -p5001
It will give a address. We need to copy & paste in our browser.

Step 3: Open Anaconda Prompt 
              We need to go to our file location and type in prompt as cd Desktop\Privacyecommerce\Privacyecommerce\blockchain
Then type python blockchain.py -p5002
It will give a address. We need to copy & paste in our browser.

Step 4: Open Anaconda Prompt 
              We need to go to our file location and type in prompt as cd Desktop\Privacyecommerce\Privacyecommerce\blockchain
Then type python blockchain.py -p5004
It will give a address. We need to copy & paste in our browser.

Step 5: Open Anaconda Prompt 
               We need to go to our file location and type in prompt as cd Desktop\Privacyecommerce\Privacyecommerce\Users
Then type as python dbconnect.py. This will connect to database.
Then type as python blockchain_client.py. 
It will give a address. We need to copy paste in our browser 3 times.

Step 6: Open http://127.0.0.1:8080/  1st  browser
              There are 3 browsers. Go to any one browser.In that in Key Generator, In name type any name (eg: Alice), any mobile No (eg:7894561230) and any address.
Then click Central Authority.
It will generate Master key and Enrollment key.These keys are for seller.

Step 7: Open http://127.0.0.1:8080/  2nd browser
              Go to another browser.In that in Key Generator, In name type any name (eg: Bob), any mobile No (eg:7894561230) and any address.Then click Central Authority.
It will generate Master key and Enrollment key.These keys are for buyer.

Step 8: Open http://127.0.0.1:8080/ 3rd browser
            Go to Node contract. In Sender address give sender's master key, in sender private's key give sender's private key , in product name give any product, 
  in quantity give any quantity and in amount give the amount.Then click generate ledger. It will give a pop up window.In that it will give the URL. 
  Go to that URL(in 5001) click Mine.In Transactions on the blockchain, there will be the items that you purchased.
  
Step 9: Open http://127.0.0.1:8080/ 3rd browser
           Go to USD Node Contract. In address give buyer master key, in Private key give buyer's enrollment key and in USD Amount give the amount. 
   Then click Generate USD Token.It will give a pop up window.In that it will give the URL. Go to that URL(in 5002) click Mine. In Transactions on the blockchain,
   there will be the items that you purchased.
   
Step 10: Open http://127.0.0.1:8080/ 3rd browser
          Go to Payment Transaction. In Sender address give buyer's master key , in sender's private key give buyer's enrollment key, In Recipient Address give seller's 
  master key, in Product ID give any number and in amount to be send give the amount. Then click generate transaction.It will give a pop up window.Then click private contract.
  Go to that URL(in 5004) click Mine. In Transactions on the blockchain, the amount paid will be displayed. 
  
  Step 11: Open http://127.0.0.1:8080/ 3rd browser
         Go to Product Delivery. In Sender address give sender's master key, in sender's private key give buyer's enrollment key. In Recipient address give buyer's master key
   and in product ID give the ID that you previously given.Then click private contract.Go to that URL(in 5000) click Mine.In Transactions on the blockchain, it will show 
   the delivery status.
