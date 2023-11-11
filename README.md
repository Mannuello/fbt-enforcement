# FBT Enforcement Application

## Description
The FBT Enforcement Application is an application that simulates components of a traffic enforcement application. 

## Team and Roles: 
- https://github.com/BrettskiPy - Engineer Lead | QA | DevOps
- https://github.com/Mannuello - Engineer | Researcher

### Features:
- License plate recognition
- Custom mailer PDF generation
    - Speeding fine collection letter
    - Driver address update letter
- Retrieves mock car data via API
- Full logging
- Pytest Suite
- GitHub Actions on PR creation and push
    - Build
    - Automated Testing
    - Code Formatting Checks  

### App Operational Order
1. Generate app fake data
2. Use fake image path to retrieve image
3. Read text from plate image using the OCR
4. Find match and return a single car record within the fake care data
5. Issue PDF tickets to drivers who violate the speed limit
6. Issue PDF notifications to drivers who have incomplete car records

## Running
To run this script, navigate to the top level of this repo and run the main module as seen below:

```
python -m fbt_enforcement
```

## Tests
This project runs tests using pytest.

To run the tests, use the following command:
```
pytest
```
#### Note: The tests will automatically launch during the build process, and you must address any issues locally or the build will fail.

## Formatter
This project uses the black formatter.

To run the formatter and linter use the following:

#### Bash
```
ruff check --fix && ruff format .
```
#### Powershell
```
ruff check --fix . ; if ($?) { ruff format . }
```
#### Note: The formatter will automatically run during the build process, and you must address any issues locally or the build will fail.
