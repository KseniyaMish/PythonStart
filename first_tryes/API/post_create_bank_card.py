import requests

headers = {'Authorization': 'Basic dXNlcm5hbWU6cS5oU2c1KVAke3JLUUBwcSU7TiVdSjQ7Vn5eL11oQTU=', 'Idempotency-Key': 'd4d34027-f514-4013-a238-b5067602319a'}
domain = 'https://sm-api.getdisco.dev'
url = domain+'/spending/v1/bank/cards/issue'
data = {
  "usecase_type": "one_time_payment",
  "account_id": "9df58cef-f449-49d8-88e2-1350334bc5a6",
  "cardholder_id": "fca6185a-6551-4ded-99d2-9283de2e2307",
  "budget_department_id": "74035d15-c4cd-43fc-94e0-4cc3a818861f",
  "user_defined_name": "1547",
  "payment_policy": {
    "merchant_policy": {
      "merchant": {
        "allowed": [
          "e3143c75-a527-4687-a2aa-faa5f6be2427"
        ],
        "declined": [
          "8f9bf1d6-6df9-4651-88ed-9bcc570cf533"
        ]
      },
      "category": {
        "allowed": [
          "a1f276fa-9eda-45bf-93b3-d5e321adab02"
        ],
        "declined": [
          "3aee75c8-6d86-4b85-959c-d7686f41fc47"
        ]
      }
    },
    "transaction_policy": {
      "txs_sum_limit": "1000",
      "txs_sum_currency": "USD",
      "txs_sum_reset_period": "daily",
      "tx_amount_limit": "100",
      "tx_count_limit": 2,
      "tx_count_reset_period": "daily"
    }
  },
  "card_activity_dates": {
    "from": "2024-05-30T08:08:23.589Z",
    "to": "2024-06-30T08:08:23.589Z"
  },
  "billing_address": {
    "country": "USA",
    "state": "California",
    "city": "Los Angeles",
    "addr_line_1": "Moll street-r",
    "house": "176/2873",
    "zip": "GFGDF78384"
  },
  "shipping_address": {
    "country": "Great Britain",
    "state": "England",
    "city": "London",
    "addr_line_1": "Backer street",
    "house": "4",
    "zip": "NBF-u76"
  },
  "location_control": {
    "country": {
      "allowed": [
        "AM"
      ],
      "declined": [
        "USD"
      ]
    },
    "currency": {
      "allowed": [
        "RU"
      ],
      "declined": [
        "GBP"
      ]
    }
  }
}
A = requests.post(url, json=data, headers=headers)
print(A.request.body)
print(A.text)
