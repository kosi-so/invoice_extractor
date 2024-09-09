## Multi-Language Invoice Extractor (Gemini Pro Demo)
### Overview
This project demonstrates a simple invoice extraction application using Streamlit and Google's Gemini Pro model. 
The application allows users to upload an invoice image (in formats like .jpg, .jpeg, .png) and enter a text prompt for analysis. 
The uploaded image is sent to the Gemini Pro model, which responds with relevant content based on the image and the provided prompt.

### Features
Upload invoice images in various formats (JPG, PNG, PDF).
Extract information from uploaded invoices using the Gemini Pro model.
Gemini Pro (Gemini 1.5 Flash) responds based on a prompt and the image data.
The interface is user-friendly, built with Streamlit for easy interaction.

### Requirements
Python 3.8+
A .env file containing the following environment variable:
GOOGLE_API_KEY: API key for accessing Google Generative AI services.
### Dependencies
streamlit: Used for building the web app interface.
Pillow (PIL): For handling image uploads and display.
python-dotenv: To load environment variables from a .env file.
google-generativeai: For integrating with Google's Gemini Pro model.

### Future Improvements
Add support for multiple image uploads.
Improve error handling and display more detailed error messages for invalid inputs.
Enhance the response display by showing structured data extracted from invoices.
