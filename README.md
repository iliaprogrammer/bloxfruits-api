# Blox Fruits API

A simple REST API built with Python and FastAPI that provides information about Blox Fruits items, gamepasses, limited items, and current in-game stock.

The API collects data from public Blox Fruits value websites and exposes it through simple HTTP endpoints, making the information easier to access programmatically.

## Features

* Fruit information lookup
* Gamepass information lookup
* Limited item information lookup
* Current Normal and Mirage stock
* Fruit list with URL-friendly names
* Gamepass list
* Limited item list
* Automatic stock reset countdown
* JSON responses
* FastAPI interactive API documentation

## Tech Stack

* Python
* FastAPI
* Requests
* BeautifulSoup4
* Uvicorn

## API Endpoints

### Fruits

Get information about a specific fruit:

```text
GET /info/fruits/{fruit_name}
```

Example:

```text
GET /info/fruits/kitsune
```

The response can include:

* Value
* Beli Price
* Best Used For
* Demand
* Rarity
* Fruit Type

### Gamepasses

Get information about a specific gamepass:

```text
GET /info/gamepasses/{gamepass_name}
```

Example:

```text
GET /info/gamepasses/fruit-notifier
```

The response can include:

* Value
* Robux Price
* Tradeable
* Demand
* Tier
* Type
* Trend

### Limited Items

Get information about a specific limited item:

```text
GET /info/limiteds/{limited_name}
```

Example:

```text
GET /info/limiteds/fiend-yeti
```

The response can include:

* Value
* Robux Price
* Tradeable
* Demand
* Tier
* Type
* Trend

### Current Stock

Get the current Normal and Mirage stock:

```text
GET /info/stock
```

The endpoint also returns the number of seconds remaining until the next Normal and Mirage stock reset.

### Available Fruits

Get the list of supported fruits and their URL-friendly names:

```text
GET /fruits
```

### Available Gamepasses

Get the list of supported gamepasses:

```text
GET /gamepasses
```

### Available Limited Items

Get the list of supported limited items:

```text
GET /limiteds
```

## Installation

Clone the repository:

```bash
git clone https://github.com/iliaprogrammer/bloxfruits-api.git
```

Move into the project directory:

```bash
cd bloxfruits-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the development server with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger UI to test the available endpoints directly from your browser.

## Example Response

A successful fruit request returns a JSON response similar to:

```json
{
    "message": "found",
    "value": "...",
    "beli_price": "...",
    "best_use": "...",
    "demand": "...",
    "rarity": "...",
    "type": "..."
}
```

The exact values depend on the current data available from the source website.

## Project Structure

```text
blox-fruits-api/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Notes

This project uses web scraping to retrieve information from external websites. Because the API depends on the structure and availability of those websites, changes to their pages may affect the returned data.

The stock endpoint calculates the time remaining until the next stock reset based on UTC time.

## Disclaimer

This project is an independent project and is not affiliated with or endorsed by the developers of Blox Fruits.

The data provided by this API is collected from publicly available sources and may change or become unavailable without notice.

## License

No license has been specified for this project yet.
