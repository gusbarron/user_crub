# Mini challenge 1
### Create an endpoint for our JOIN statement
#### Acceptance criteria 
1. A route definition so we can issue HTTP requests to get the report data.
2. A separate database module (reports.py) within database that handles the database logic.
  2.1. Consider formatting the data so that it is compatible with JSON.
3. Test your solution. You should see a JSON with all matching results in the browser.

GET /reports/cars

Result could be:

{
  "ok": True,
  "cars": [
    {
      "last_name": "Barron",
      "first_name": "Gustavo",
      "hobbies": "Coding",
      "active": 1,
      "license_plate":
      "something",
      "color": "red",
      "vehicle_type": "truck",
      "brand": "toyota",
      "model": "tacoma"
    },
    
  ]
}