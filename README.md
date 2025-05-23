# Interface Data API

A FastAPI-based REST API for managing and accessing interface data, particularly focused on Azure resources and integration services.

## Project Overview

This project provides a comprehensive API for managing and accessing various Azure resources, including:
- Azure Tenants and Subscriptions
- Data Sources
- Resource Groups
- Integration Accounts
- Logic Apps
- API Management Services
- And more

## Project Structure

```
.
├── main.py              # FastAPI application entry point
├── config.py           # Configuration settings
├── db.py              # Database connection and session management
├── models.py          # SQLAlchemy models for database tables
├── routes/            # API route definitions
│   └── interfaces.py  # Interface-related endpoints
├── relationship/      # Relationship definitions between models
├── pyproject.toml     # Project dependencies and metadata
└── poetry.lock        # Locked dependencies
```

## Setup and Installation

1. Ensure you have Python 3.x installed
2. Install Poetry (dependency management)
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Set up your environment variables in a `.env` file:
   ```
   DATABASE_URL=postgresql://postgres:pass@localhost:5432/new
   ```

## Database Configuration

The project uses PostgreSQL as the database. The connection string is configured in `config.py` and can be overridden using environment variables.

## API Endpoints

### Base Endpoints
- `GET /`: Welcome message
- `GET /api/tables`: List all available tables
- `GET /api/{table_name}`: Get data from a specific table
- `GET /api/{table_name}/columns`: Get column information for a specific table

### Azure Resource Endpoints

#### Tenant Management
- `GET /api/tenants/{tenant_id}/subscriptions`: Get subscriptions for a tenant
- `GET /api/tenants/{tenant_id}/datasource`: Get datasource for a tenant

#### Subscription Management
- `GET /api/subscriptions/{subscription_id}/tenant`: Get tenant for a subscription

#### DataSource Management
- `GET /api/datasources/{datasource_id}/tenants`: Get tenants for a datasource

#### Resource Group Management
- `GET /api/resource_groups/{group_id}/integration_accounts`: Get integration accounts for a resource group

#### Integration Account Management
- `GET /api/integration_accounts/{account_id}/sessions`: Get sessions for an integration account
- `GET /api/integration_accounts/{account_id}/agreements`: Get agreements for an integration account
- `GET /api/integration_accounts/{account_id}/certificates`: Get certificates for an integration account
- `GET /api/integration_accounts/{account_id}/schemas`: Get schemas for an integration account
- `GET /api/integration_accounts/{account_id}/maps`: Get maps for an integration account
- `GET /api/integration_accounts/{account_id}/partners`: Get partners for an integration account
- `GET /api/integration_accounts/{account_id}/partner_metadata`: Get partner metadata for an integration account
- `GET /api/integration_accounts/{account_id}/partner_identities`: Get partner identities for an integration account

#### Workflow Management
- `GET /api/workflows/{workflow_id}/versions`: Get versions for a workflow
- `GET /api/standard_apps/{app_id}/workflows`: Get workflows for a standard app

#### API Management
- `GET /api/api_management_services/{service_id}/apis`: Get APIs for a service
- `GET /api/apis/{api_id}/service`: Get service for an API

## Models

The project uses SQLAlchemy models defined in `models.py`. Key models include:

- AzureTenants
- DataSources
- AzureSubscription
- AzureResourceGroup
- AzureLogicAppIntegrationAccount
- AzureLogicAppWorkflow
- AzureStandardApp
- AzureApiManagementService
- AzureApiManagementApi

## Development

1. Start the development server:
   ```bash
   poetry run uvicorn main:app --reload
   ```

2. Access the API documentation at:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## Error Handling

The API implements proper error handling with HTTP exceptions for:
- Resource not found (404)
- Server errors (500)
- Invalid requests (400)

## CORS Configuration

The API is configured to allow CORS requests from any origin, with support for:
- All methods
- All headers
- Credentials

## Dependencies

Key dependencies include:
- FastAPI
- SQLAlchemy
- Pydantic
- Poetry (for dependency management)
- PostgreSQL (database)

## Testing Endpoints

### Using Swagger UI
1. Start the development server:
   ```bash
   poetry run uvicorn main:app --reload
   ```
2. Open `http://localhost:8000/docs` in your browser
3. Click on any endpoint to expand it
4. Click "Try it out" button
5. Fill in the required parameters
6. Click "Execute" to test the endpoint

### Using Postman
1. **Setup**
   - Download and install [Postman](https://www.postman.com/downloads/)
   - Create a new collection named "Interface Data API"

2. **Environment Setup**
   - Click on "Environments" in the sidebar
   - Create a new environment (e.g., "Local Development")
   - Add these variables:
     ```
     base_url: http://localhost:8000
     tenant_id: your_tenant_id
     account_id: your_account_id
     ```

   **How to Get tenant_id and account_id:**
   
   1. First, get all tables to see available data:
      ```
      GET {{base_url}}/api/tables
      ```
      This will return a list of all available tables in the database.

   2. To get tenant_id:
      - Look for tables containing tenant information (e.g., "azure_tenants")
      - Query the table:
        ```
        GET {{base_url}}/api/azure_tenants
        ```
      - The response will contain tenant records with their IDs
      - Copy an existing tenant_id from the response

   3. To get account_id:
      - Look for tables containing integration account information (e.g., "azure_logic_app_integration_accounts")
      - Query the table:
        ```
        GET {{base_url}}/api/azure_logic_app_integration_accounts
        ```
      - The response will contain integration account records with their IDs
      - Copy an existing account_id from the response

   4. Update your Postman environment:
      - Replace `your_tenant_id` with the actual tenant ID you copied
      - Replace `your_account_id` with the actual account ID you copied

   **Note:** If you don't see any data in these tables, you'll need to:
   1. Ensure your database is properly set up
   2. Check if you have the correct database connection string in your `.env` file
   3. Verify that data has been imported into these tables

3. **Creating Requests**
   Here are some example requests to add to your collection:

   a. **Get All Tables**
   - Method: GET
   - URL: {{base_url}}/api/tables
   - Headers: None required

   b. **Get Table Data**
   - Method: GET
   - URL: {{base_url}}/api/{{table_name}}
   - Headers: None required

   c. **Get Tenant Subscriptions**
   - Method: GET
   - URL: {{base_url}}/api/tenants/{{tenant_id}}/subscriptions
   - Headers: None required

   d. **Get Integration Account Sessions**
   - Method: GET
   - URL: {{base_url}}/api/integration_accounts/{{account_id}}/sessions
   - Headers: None required

4. **Running Tests in Postman**
   - Select the environment you created
   - Click "Send" to execute the request
   - View the response in the lower panel
   - Check the status code, response body, and headers

5. **Automated Testing in Postman**
   Add test scripts to your requests:
   ```javascript
   // Example test script for Get All Tables
   pm.test("Status code is 200", function () {
       pm.response.to.have.status(200);
   });

   pm.test("Response is an array", function () {
       var jsonData = pm.response.json();
       pm.expect(Array.isArray(jsonData)).to.be.true;
   });

   pm.test("Response contains expected tables", function () {
       var jsonData = pm.response.json();
       pm.expect(jsonData).to.include("your_expected_table");
   });
   ```

6. **Collection Runner**
   - Click "Runner" in Postman
   - Select your collection
   - Choose the environment
   - Set iterations and delay
   - Click "Run" to execute all requests

7. **Export/Import**
   - Export your collection: Click the three dots next to your collection → Export
   - Share with team: Click "Share Collection" → Generate a link
   - Import collection: Click "Import" → Paste the shared link

8. **Best Practices for Postman Testing**
   - Use environment variables for different configurations
   - Create test scripts for each request
   - Use collection variables for shared data
   - Set up pre-request scripts if needed
   - Use the collection runner for automated testing
   - Save example responses for documentation
   - Use folders to organize related requests

### Using cURL
Here are some example cURL commands for testing key endpoints:

1. Get all tables:
   ```bash
   curl -X GET "http://localhost:8000/api/tables"
   ```

2. Get data from a specific table:
   ```bash
   curl -X GET "http://localhost:8000/api/your_table_name"
   ```

3. Get tenant subscriptions:
   ```bash
   curl -X GET "http://localhost:8000/api/tenants/{tenant_id}/subscriptions"
   ```

4. Get integration account sessions:
   ```bash
   curl -X GET "http://localhost:8000/api/integration_accounts/{account_id}/sessions"
   ```

### Using Python Requests
Here's an example of how to test endpoints using Python:

```python
import requests

BASE_URL = "http://localhost:8000/api"

# Test getting all tables
response = requests.get(f"{BASE_URL}/tables")
print("Tables:", response.json())

# Test getting tenant subscriptions
tenant_id = "your_tenant_id"
response = requests.get(f"{BASE_URL}/tenants/{tenant_id}/subscriptions")
print("Subscriptions:", response.json())

# Test getting integration account data
account_id = "your_account_id"
response = requests.get(f"{BASE_URL}/integration_accounts/{account_id}/sessions")
print("Sessions:", response.json())
```

### Automated Testing
For automated testing, you can use pytest. Create a `tests` directory and add test files:

```python
# tests/test_endpoints.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tables():
    response = client.get("/api/tables")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_tenant_subscriptions():
    tenant_id = "test_tenant_id"
    response = client.get(f"/api/tenants/{tenant_id}/subscriptions")
    assert response.status_code in [200, 404]  # 404 if tenant doesn't exist

def test_get_integration_account_sessions():
    account_id = "test_account_id"
    response = client.get(f"/api/integration_accounts/{account_id}/sessions")
    assert response.status_code in [200, 404]  # 404 if account doesn't exist
```

Run the tests using:
```bash
poetry run pytest
```

### Testing Best Practices
1. Always test both successful and error cases
2. Test with valid and invalid input data
3. Verify response status codes and data structures
4. Test rate limiting if implemented
5. Test authentication if required
6. Use environment variables for test configuration
7. Mock external services when appropriate

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here] 