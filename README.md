# FBT Enforcement Application

## Description
The FBT Enforcement Application is an application that simulates components of a traffic enforcement application. 

It has the following features:
- License plate recognition
- Custom PDF creations 
    - Speeding fine collection
    - Driver address update notifications
- Retrieves mock car data via API
- Full logging
- Pytest Suite
- GitHub Actions on PR creation and push
    - Build
    - Automated Testing
    - Code Formatting Checks  

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

To run the formatter, use the following command:
```
black .
```
#### Note: The formatter will automatically run during the build process, and you must address any issues locally or the build will fail.
