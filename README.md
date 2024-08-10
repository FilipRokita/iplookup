# IP Lookup

This project consists of a Python script and a web application to perform IP address lookups using various IP geolocation services. The IP lookup can be executed via command line or through a web interface.

## Components

1. **`iplookup.py`**: A Python script that queries multiple IP geolocation services and returns the results.
2. **`index.html`**: A simple HTML page with a form to input an IP address and display the lookup results.
3. **`app.py`**: A Flask web application that serves the HTML page and handles IP lookup requests by invoking the `iplookup.py` script.

## Requirements

- Python 3.x
- Flask
- Requests library

You can install the required Python libraries using pip:

```bash
pip install flask requests
```

## Usage

### Command Line

1. **Basic Lookup**: 

   To lookup an IP address, run:

   ```bash
   python iplookup.py <ip-address>
   ```

   This will output the results from all the geolocation services in JSON format.

2. **Save to File**:

   To save the results to a file named `ip_lookup_result.json`, use:

   ```bash
   python iplookup.py -s <ip-address>
   ```

### Web Interface

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter an IP address in the input field and click the "Lookup" button. The results will be displayed below the button.

## File Details

### `iplookup.py`

This script performs the IP lookup using various geolocation APIs. It defines a list of APIs and fetches information from each of them. The results are then printed or saved to a file based on the command-line arguments.

### `index.html`

This is a static HTML file providing a user interface to input an IP address and view the lookup results. The page is styled for simplicity and ease of use.

### `app.py`

This Flask application serves the HTML file and handles API requests. It calls the `iplookup.py` script to perform the IP lookup and returns the results as JSON.

## Troubleshooting

- **Error: IP address is required**: Ensure that you provide an IP address as a query parameter when using the web interface.
- **Error running script**: Make sure `iplookup.py` is in the same directory as `app.py` and that it is executable.
- **JSON decoding errors**: Verify that `iplookup.py` is generating valid JSON output.

## Contributing

Feel free to open issues or submit pull requests to improve the functionality or add more features. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For any further questions or assistance, please feel free to contact the project maintainers. Happy IP lookup!
