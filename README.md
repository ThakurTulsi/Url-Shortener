# URL Shortener

This project is a simple Python-based URL shortener that leverages the `pyshorteners` library to convert long URLs into shortened versions using TinyURL.

## Features
- Takes a user input URL and converts it into a shortened link using TinyURL.
- Easy to use and can be extended with other URL shortening services.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- The `pyshorteners` library

You can install `pyshorteners` by running:

```bash
pip install pyshorteners
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

2. Run the script:

```bash
python shortener.py
```

3. Enter the URL you want to shorten when prompted.

Example:

```bash
enter your url: https://www.example.com/very/long/url
```

Output:

```bash
the shortened url is: https://tinyurl.com/abc123
```

## Code Explanation

```python
import pyshorteners

# Request the user to input a URL
user_url = input("enter your url: ")

# Initialize the URL shortener service (TinyURL in this case)
s = pyshorteners.Shortener()

# Shorten the URL using TinyURL
url_short = s.tinyurl.short(user_url)

# Output the shortened URL
print("the shortened url is: ", url_short)
```

- The script takes a URL input from the user and uses the `pyshorteners.Shortener()` class to create a TinyURL-shortened version of the original URL.
- The shortened URL is then printed to the console.

- Here's an additional section for your README that highlights the benefits of using this URL shortener script compared to third-party websites like Bitly:

---

## Why Use This URL Shortener?

Many people visit third-party websites like [Bitly](https://bitly.com/) or [TinyURL](https://tinyurl.com/) to shorten their URLs. While these services are popular and easy to use, they come with certain limitations:

- **Time-consuming:** You need to visit the website, paste the URL, and manually copy the shortened link back.
- **Account creation:** Some services may require you to create an account to access advanced features.
- **Dependency on a third-party platform:** Your workflow depends on an external website, which might have restrictions or be unavailable.

### Advantages of This Project

With this Python-based URL shortener, you can:

- **Shorten URLs instantly:** Just run the script, enter the URL, and get your shortened link within seconds—no need to open a browser or visit any external websites.
- **Save time:** Automate the URL shortening process as part of your workflow, ideal for developers or frequent users of URL shortening services.
- **Maintain control:** You aren’t dependent on third-party websites that could have outages, delays, or privacy concerns.
- **Customizable:** The script is fully customizable, and you can easily switch between URL shortening services supported by `pyshorteners` (such as Bitly, TinyURL, and others).

This project gives you more control over the process and allows you to streamline your tasks by reducing dependency on external platforms.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to update the repository URL and license section as per your project's details!
