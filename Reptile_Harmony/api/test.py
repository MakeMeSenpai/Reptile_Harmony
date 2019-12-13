#pylint throws an error. But this works
import stripe
from dotenv import load_dotenv

stripe.api_key = load_dotenv()

#this is only available in the US and Canada areas, this can be changed with intentpurchases
charge = stripe.Charge.create(
  amount=1000,
  currency='usd',
  source='tok_visa',
  receipt_email='totallynotafakeemail@yahoo.com', #this needs business email
)