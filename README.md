Sure! Here’s the README file in English for your data normalization project:

---

# Data Normalization Project

## Table of Contents
- [Introduction](#introduction)
- [Project Goals](#project-goals)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  - [API](#api)
- [Data Indexing](#data-indexing)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction
This project aims to normalize data from various sources and create new tables, making it easier to manage and work with the data. Additionally, the project includes an API that allows for requests on the unnormalized data, along with an indexing system to enhance search efficiency.

## Project Goals
- **Data Normalization**: Transform unnormalized data into a normalized format to improve efficiency.
- **Create New Tables**: Convert data from different sources into tables that are easy to understand and work with.
- **API**: Provide access to unnormalized data via an API, simplifying data usage.
- **Indexing**: Enhance search performance through data indexing.

## Architecture
The project is built from several components:
- **Normalization Module**: Responsible for normalizing the data.
- **API Module**: Provides a RESTful interface for requests on the data.
- **Indexing Module**: Manages data indexing for fast searching.

## Installation
1. **Prerequisites**:
   - Python 3.7+
   - pip
   - A database (such as PostgreSQL or MySQL)

2. **Installation**:
   ```bash
   git clone https://github.com/username/data-normalization-project.git
   cd data-normalization-project
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Create a database and configure the settings in the `.env` file.

## Usage

### API
After installing the project, you can start the server:
```bash
python app.py
```
The API is available at `http://localhost:5000`.

#### Example Requests:
- **Get Unnormalized Data**:
  ```http
  GET /api/unnormalized-data
  ```

- **Get Normalized Data**:
  ```http
  GET /api/normalized-data
  ```

- **Add a New Record**:
  ```http
  GET /api/mission
  Content-Type: application/json

  {
    "field1": "value1",
    "field2": "value2"
  }
  ```

## Data Indexing
The project includes an indexing system that allows for fast searching of data. To index the data, simply run the command:
```bash
python index_data.py
```
Now, you can search the data using the search API:
```http
GET /api/mission/<your_query>
```

## Contributing
If you would like to contribute to the project, feel free to submit pull requests or open issues in the project repository.

## Contact
For questions, suggestions, or issues, please contact [yonie3921@gmail.com].

---

### Notes
- Be sure to replace `username`, `yonie3921@gmail.com`, and any other details as needed.
- You can also add code snippets, explanations of the fields in the data, and even videos or images to make the README more engaging!

If you have any further questions or would like to make adjustments, I'm here to help!

