import google.generativeai as genai

# Define the Gemini API key
GEMINI_API_KEY = "*************************************"

# Configure Google GenerativeAI with API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate content using Gemini model
def generate_content(prompt):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text.strip()  # Return the text of the response, not the response object

# List of image paths
image_paths = [
    "/content/product1.jpg",
    "/content/product2.jpg",
    "/content/product3.jpg",
    "/content/product4.jpg",
    "/content/product5.jpg"
]

Generated_Prompts = []

# Example data, you can modify according to your requirements
for path in image_paths:
    # Prompt to extract information from the image
    information_prompt = "Describe the product in the image."

    # Generate content using the Gemini model with the extracted information as prompt
    extracted_information = generate_content([information_prompt, path])

    # Prompt
    for _ in range(5):  # Generate five prompts for each image
        prompt = f"Provide a prompt for the AI to craft backgrounds that embody professionalism and realism, while also incorporating unique and sophisticated viewpoints. {extracted_information}"
        Generated_Prompts.append(prompt)

# Print or use the Generated_Prompts list as needed
print(Generated_Prompts)
