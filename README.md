# MarbleAI-assignment

## Background Prompt Generator
This code allows users to automatically generate prompts for marketing campaign backgrounds. It leverages the Gemini model for creative prompt generation and for generating backgrounds based on the provided prompts I used PhotoRoom AI editor. Users can input images of products, and the system will extract information from the images to create unique prompts for marketing campaigns.

## Workflow
1. Input Images: Provide paths to images of products you want to create marketing campaign backgrounds for.
2. Extract Information: The system extracts information from each image using a predefined prompt.
3. Generate Prompts: Using the extracted information, the system generates prompts for marketing campaign backgrounds.
4.Prompt Generation: Each prompt is passed through the Gemini model to enhance its creativity and uniqueness.
5. Edit in PhotoRoom: Utilize the generated prompts as input within the PhotRoom editing application, to craft polished and captivating backgrounds using prompts.
6. Output: The application delivers the generated backgrounds corresponding to each input image, offering the flexibility to customize them according to our specific requirements. Additionally, the prompts can be refined or adjusted as needed to achieve the desired outcome.

## Performance
The application efficiently provides the generated backgrounds for each input image, with each image processing task completed in under 10 seconds. Additionally, prompt generation for all 25 prompts is completed swiftly, taking less than 30 seconds in total, ensuring a seamless user experience. Moreover, users have the option to refine the prompts or adjust the backgrounds according to their preferences, further enhancing customization possibilities.

## Installation
To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage
To use the project, run the following command:

```bash
python generate_prompts.py
```

## Credits
Google GenerativeAI and
PhotRoom
