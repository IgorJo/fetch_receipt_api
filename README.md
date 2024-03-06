# fetch_receipt_api
Implementation of https://github.com/fetch-rewards/receipt-processor-challenge

To run:

Clone repo locally

From repo directory, run the following commands
```
docker build -t receipt_controller .
docker run -p 5000:5000 receipt_controller
```
