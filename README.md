# Multilogin X Automation Project

## Overview

This project automates interactions with the Multilogin X platform and performs various web scraping tasks using Selenium WebDriver. The project includes functionalities for logging in, managing profiles, and extracting data from web pages.

## Project Structure

- **common_components**: Contains common utilities and constants used across the project.
- **drivers**: Contains the Selenium WebDriver setup and Multilogin X connection logic.
- **locators**: Contains locators for web elements used in the project.
- **mixins**: Contains mixin classes for additional functionalities like mouse movements.
- **pages**: Contains page object models for different web pages.
- **main.py**: The main script to run the automation tasks.

## Setup

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the root directory and add the necessary environment variables:
    ```sh
    MLX_EMAIL_FIELD=<your_email>
    MLX_PASSWORD_FIELD=<your_password>
    ```

2. Update any other configuration settings in `common_components/constants.py` as needed.

## Usage

### Running the Automation

To run the main automation script, execute:
```sh
python main.py
```

### Additional Scripts

- **scrape_data.py**: This script is used to scrape data from a specific web page.
- **analyze_data.py**: This script is used to analyze the scraped data.



### Key Functions

- **Logging In**: The login functionality is handled in `drivers/mlx_connection.py`:
    ```python:drivers/mlx_connection.py
    startLine: 20
    endLine: 39
    ```

- **Opening Browser**: The browser is opened and connected using:
    ```python:drivers/mlx_connection.py
    startLine: 42
    endLine: 94
    ```

- **Google Search Interaction**: The main Google search interaction is defined in `main.py`:
    ```python:main.py
    startLine: 13
    endLine: 25
    ```

- **Extracting Data**: Data extraction functions are defined in `main.py`:
    ```python:main.py
    startLine: 51
    endLine: 98
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Selenium WebDriver
- PyAutoGUI
- Requests
- WebDriver Manager

For any questions or issues, please open an issue in the repository.
