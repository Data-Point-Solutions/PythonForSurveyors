# DMS to DD Coordinate Converter

This application provides a graphical interface for converting geographic
coordinates (latitude and longitude) from Degrees, Minutes, Seconds (DMS) to
Decimal Degrees (DD) formats. It supports simultaneous conversion of both
latitude and longitude values with high precision, matching the standards of NGS
datasheets.

## Features

- Convert Degrees, Minutes, and Seconds (DMS), and Direction (N/S/E/W) for both
  latitude and logitude to Decimal Degrees (DD).
- Convert Decimal Degrees (DD) to Degrees, Minutes, and Seconds (DMS), and
  Direction (N/S/E/W) for both latitude and logitude.
- Outputs Decimal Degrees (DD) to 9 decimal places, and Degrees, Minutes, and
  Seconds (DMS) to 6 decimal places.

## Setup

### Requirements

- Python 3.x
- Tkinter (usually included with Python)

### Installation

1. Ensure Python is installed on your system. You can download Python from
   [python.org](https://www.python.org/downloads/).
2. Clone this repository or download the script file DMS.py.
3. Run the script using the command: (if you cloned the repository)

   ```bash
   python python/calculators/DMS.py
   ```

## Usage

1. Select Conversion Mode:

   - Use the radio buttons at the top of the interface to select either "DMS to
     DD" or "DD to DMS" conversion mode.

2. Input fields:

   - DMS to DD:
     - Enter the Degrees, Minutes, and Seconds for both Latitude and Longitude
       in the corresponding fields.
     - Enter the Direction (N/S for Latitude and E/W for Longitude) in the
       corresponding field.
   - DD to DMS:
     - Enter the Decimal Degrees for both Latitude and Longitude in the
       corresponding fields.

3. Conversion:

   - Click the "Convert to DD" button when in DMS to DD mode.
   - Click the "Convert to DMS" button when in DD to DMS mode.

4. Result:
   - The results will be displayed below the input fields.
     - Decimal Degrees are shown to the 9th decimal place.
     - Degrees, Minutes, and Seconds are shown to the 6th decimal place.

## GUI Elements

- Radio Buttons: Select either "DMS to DD" or "DD to DMS" conversion mode.
- DMS Input Fields: Enter the Degrees, Minutes, and Seconds for both Latitude
  and Longitude.
- DD Input Fields: Enter the Decimal Degrees for both Latitude and Longitude.
- Convert Buttons: Click the "Convert to DD" button when in DMS to DD mode.
  Click the "Convert to DMS" button when in DD to DMS mode.
- Result: The results will be displayed below the input fields.

## Error Handling

- If invalid or incomplete inputs are detected, an error message will be
  displayed.
- Ensure that all input fields are filled correctly:
  - Use numeric values for degrees, minutes, and seconds.
  - Use N/S for latitude and E/W for longitude.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are highly encouraged. Please open an issue or submit a pull
request for any improvements or bug fixes.
