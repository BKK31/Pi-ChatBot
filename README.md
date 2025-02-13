# AIChatBot.py

This Flask web application provides a simple interface for uploading and analyzing wound images.

## Installation

Install the required dependencies:

```shell
pip install flask google-generativeai pillow
```

## Usage

1. Set the `GOOGLE_GENERATIVEAI_API_KEY` environment variable to your Google Generative AI API key.

2. Run the application:

```shell
python AIChatBot.py
```

## Features

- Upload an image of a wound and get a detailed description of the wound and the recommended first-aid treatment.
- Images must be in JPG or PNG format.

## Limitations

- This application is for informational purposes only and should not be used for medical diagnosis or treatment. Always consult a medical professional for wound assessment and treatment.

## Credits

- The image analysis functionality is powered by the Google Generative AI API.

## License

MIT License

Copyright (c) 2024 Achyuth S, Ashwin S, Bharadwaj M, Bhargava K K

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
