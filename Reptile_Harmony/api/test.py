#pylint throws an error. But this works
import os
import stripe
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv('API_KEY')
stripe.api_key = API_KEY

#this is only available in the US and Canada areas, this can be changed with intentpurchases
charge = stripe.Charge.create(
  amount=1000, #image this like yen: ¥1000 = $10
  currency='usd',
  source='tok_visa',
  receipt_email='totallynotafakeemail@yahoo.com', #this needs business email
)