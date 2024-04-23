
# Speech To Code

This project integrates speech-to-text conversion, text-to-code generation, and Streamlit presentation to facilitate the seamless transformation of spoken programming instructions into code snippets with an interactive user interface.


## Authors

- [@Santhoshcv19](https://github.com/Santhoshcv19)
- [@bharat0901](https://github.com/bharat0901)
- [@jefferson0511](https://github.com/jefferson0511)



## Features

- **Speech-to-Text Conversion**: Converts spoken input into text using the Python `speech_recognition` library.
- **Text-to-Code Generation**: Leverages the capabilities of Code Llama to interpret textual commands and generate corresponding code snippets.
- **Streamlit Presentation**: Utilizes Streamlit to display the generated code snippets in an interactive and user-friendly interface.


## Installation

Before you can use this tool, you'll need to install several dependencies. This guide assumes you have Python installed on your system.

```bash
git clone https://github.com/Santhoshcv19/Speech_To_Code
cd Speech_To_Code
pip install -r requirements.txt
```
    
## Usage

To use the tool, follow these steps:

1. Run the provided Colab code blocks to generate a public URL for your speech-to-code services.

2. Replace the placeholder URL in the `stream.py` file with the URLs generated from Colab

3. Start the Streamlit application:
    ```bash
   streamlit run stream.py
    ```
