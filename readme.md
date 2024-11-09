# Startup Guide

This project comprises a PostgreSQL database, a data collection service, and a Jupyter notebook environment for analyzing the collected data.

## Prerequisites

1. **Docker**: Make sure Docker is installed and running on your system.
2. **.env file**: Create a `.env` file in the root directory with the following variables: (already created for testing purposes)
   ```plaintext
   POSTGRES_DB=open_flights
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=P@ssw0rd
   JUPYTER_TOKEN=eD3hMsNBocXV_bNYUXL8fOTY-2BgwcKjBSkBhE4GSDQ
   ```

## Running the Project

### 1. Start the Database

The PostgreSQL service needs to be fully up and running before starting the data collection service.

Run the following command to start all services:
   ```bash
   docker-compose up postgres_db
   ```

### 2. Run the Data Collection Service

Once the database is running, start the data collection service, which will fetch and insert data into the database.
   ```bash
   docker-compose up data_collection
   ```
Wait for the data collection service to complete its task and automatically terminate. This ensures all data has been successfully loaded into the database.

### 3. Start the Jupyter Notebook

With the data collection complete, you can now start Jupyter for data analysis:
   ```bash
   docker-compose up jupyter
   ```
This will start a Jupyter notebook server accessible at:
http://localhost:8888/?token=eD3hMsNBocXV_bNYUXL8fOTY-2BgwcKjBSkBhE4GSDQ 
you may need to change host accordingly. 

### 4. Open the Analysis Notebook

In the Jupyter interface, navigate to the `notebooks` directory and open `notebook_flights_analysis.ipynb`. This notebook contains SQL queries and analysis tools for exploring the flight data loaded into PostgreSQL.

Notes
-----

*   **Service Dependencies**: The data collection service depends on the database. If the database is not fully ready, `data_collection` may fail.
*   **Data Collection Completion**: Ensure `data_collection` has fully terminated before starting Jupyter to avoid incomplete data analysis.
*   **Jupyter Access**: If prompted, use the token specified in your `.env` file (or use the direct URL provided above).