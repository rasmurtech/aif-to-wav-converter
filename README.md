# AIFF to WAV Converter

A Python script to convert AIFF (Audio Interchange File Format) files to WAV format. The script uses the soundfile and wavio libraries to read AIFF files and write WAV files. It can be used to convert a directory of AIFF files to WAV format with just a few lines of code.

## Usage

1. Place your AIFF files in an input folder.
2. Create an output folder for the converted WAV files.
3. Run the script with the input and output folder paths as command-line arguments:

```bash
python aif_to_wav.py <input_folder> <output_folder>
The script will process all AIFF files in the input folder and save the converted WAV files in the output folder.

## Requirements

. Python 3
. soundfile
. wavio

## Installation

1. Clone the repository or download the aif_to_wav.py script.
2. Install the required libraries using pip:


pip install soundfile wavio

## Code Overview

The script contains a main function, convert_aif_to_wav, that takes two arguments: input_folder and output_folder. The function iterates through the files in the input folder, reads AIFF files using the soundfile library, converts the audio data to 16-bit integers, and writes the data as WAV files using the wavio library.

The dtype_to_sampwidth function is a helper function that converts a NumPy data type string to the corresponding sample width in bytes. This value is used by the wavio library when writing the WAV files.

The script can be run as a standalone script or imported as a module in other Python code.

## License

```bash
With this change, the "Usage" section now appears before the "Requirements" and "Installation" sections in the README.md file.


