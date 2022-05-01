## Sample payload

- Method: `POST`
- URL: `http://localhost:8080/gpt2`

```
curl --location --request POST 'http://localhost:8080/gpt2' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "nasa is a space agency.",
    "max_length": 150
}'
```
