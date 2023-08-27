# Flask Card API

This Flask API serves card data in JSON format and allows filtering based on various attributes like `parallel`, `rarity`, `name`, `subtype`, and `keyword`.

## Requirements

-   Python 3.x
-   Flask

## Setup

1. Download `app.py` and `cards.json` and place them in the same directory.
2. Open a terminal and navigate to the directory containing the files.
3. Run `python app.py` to start the Flask server.
4. Open a web browser and navigate to `http://localhost:5000/cards` to access the API.

## API Usage

### Endpoints

-   `GET /cards`: Fetches all cards with optional filtering.

#### Query Parameters

-   `parallel`: Filter cards based on their parallel attribute. (e.g., `?parallel=augencore`)
-   `rarity`: Filter cards based on their rarity attribute. (e.g., `?rarity=legendary`)
-   `name`: Filter cards based on their name. Partial names are allowed. (e.g., `?name=Trade`)
-   `subtype`: Filter cards based on their subtype attribute. (e.g., `?subtype=your_subtype_here`)
-   `keyword`: Search for a keyword within the 'Text' attribute of cards. (e.g., `?keyword=attack`)

You can combine multiple filters like so: `?rarity=legendary&name=Trade&parallel=augencore`

## Examples

1. To get all cards with a rarity of "legendary":

    ```
    http://localhost:5000/cards?rarity=legendary
    ```

2. To search for the keyword "attack" in the 'Text' attribute:

    ```
    http://localhost:5000/cards?keyword=attack
    ```

3. To combine multiple filters:
    ```
    http://localhost:5000/cards?rarity=legendary&name=Trade&parallel=augencore
    ```

## License

MIT
