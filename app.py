import os
import gradio as gr
from openai import OpenAI
import base64
import json
from dotenv import load_dotenv

# Load environment variables from .env file for local development
# (On Hugging Face Spaces, secrets are set in the UI)
load_dotenv()

# 1. CONFIGURE OPENAI CLIENT
# ---------------------------
# The API key is fetched from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Please set it in your environment variables or Hugging Face Spaces secrets."
    )

client = OpenAI(api_key=api_key)

# 2. DEFINE THE AI SYSTEM PROMPT
# This is the "brain" of the operation.
# It instructs the AI on its role, criteria, and output format (JSON).
SYSTEM_PROMPT = """You are an AI quality control inspector for Snoonu Operations. Your task is to analyze an image of a courier's thermal bag and determine if it is 'Acceptable' or 'Not Acceptable' for delivery shifts.

**REFERENCE STANDARDS:**

**ACCEPTABLE BAG EXAMPLE:**
- Clean, silver/metallic reflective thermal insulation material
- Pristine condition with no visible damage
- Proper thermal bag structure (can be simple insulated bag or branded delivery bag)
- No stains, dirt, or food residue
- All materials intact and functional

**NOT ACCEPTABLE BAG EXAMPLE:**
- Visible dirt, grime, or discoloration on thermal lining
- Stains or food residue (especially inside thermal lining)
- Torn, ripped, or damaged insulation material
- Worn-out or degraded thermal lining
- Broken zippers, handles, or structural components
- Compromised insulation that could affect food temperature

**DETAILED INSPECTION CRITERIA:**

1. **Cleanliness (CRITICAL):**
   - Inside thermal lining must be clean and free from stains
   - No visible food residue, grease marks, or spills
   - No dirt accumulation or discoloration
   - Reflective thermal material should maintain its appearance
   - Check corners and seams for hidden dirt buildup

2. **Structural Integrity (CRITICAL):**
   - Thermal insulation material must be intact (no rips, tears, or holes)
   - No delamination or peeling of thermal lining
   - Bag structure must be stable and not collapsing
   - Seams and stitching must be secure
   - No exposed foam or insulation material

3. **Functional Components:**
   - Zippers must be intact and functional (not broken or missing teeth)
   - Handles must be secure and not frayed or torn
   - Velcro or magnetic closures must work properly
   - Bag must be able to close completely to maintain temperature

**DECISION LOGIC:**
- If ANY critical criterion fails (cleanliness or structural integrity), the bag is NOT ACCEPTABLE
- Minor cosmetic wear on external fabric is acceptable if thermal function is maintained
- When in doubt about borderline cases, prioritize food safety and customer perception

**RESPONSE FORMAT:**
You MUST respond *only* with a JSON object. Do not add any explanatory text
before or after the JSON. The JSON format must be:

{
  "is_acceptable": boolean,
  "reason": "A single, clear sentence explaining the decision."
}

**ANALYSIS APPROACH:**
1. First identify the type of bag (simple thermal bag vs branded delivery bag)
2. Examine the thermal lining condition carefully (this is most critical)
3. Check for any visible damage or wear
4. Assess cleanliness inside and outside
5. Evaluate functional components
6. Make final determination based on food safety and professional standards

Remember: Food safety is paramount. When analyzing, think about whether you would be comfortable receiving your own food delivery in this bag.
"""


# 3. HELPER FUNCTION: ENCODE IMAGE
# --------------------------------
def encode_image(image_pil):
    """Encodes a PIL image to a base64 string."""
    try:
        # Gradio provides the image as a PIL object.
        from io import BytesIO
        buffered = BytesIO()
        image_pil.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

# 4. CORE FUNCTION: ANALYZE BAG QUALITY
# -------------------------------------
def analyze_bag_quality(image_upload):
    """
    This is the main function called by the Gradio interface.
    It takes an image, sends it to GPT-4o, and returns a formatted analysis.
    """
    if image_upload is None:
        return "Please upload an image."

    try:
        # 1. Encode the uploaded image
        base64_image = encode_image(image_upload)
        if not base64_image:
            return "Error: Could not process image."

        # 2. Prepare the payload for the OpenAI API
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Please analyze this thermal bag image."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]

        # 3. Call the API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=300,  # <-- ****MODIFIED: Reduced max_tokens****
            response_format={"type": "json_object"}  # Enforce JSON output
        )

        # 4. Parse the JSON response
        analysis_data = json.loads(response.choices[0].message.content)

        # 5. Format the output for the user
        
        if analysis_data["is_acceptable"]:
            status = "✅ ACCEPTABLE"
            output = f"## **{status}**\n\n**Reason:** {analysis_data['reason']}"
        else:
            status = "❌ NOT ACCEPTABLE"
            output = f"## **{status}**\n\n**Reason:** {analysis_data['reason']}"
            
        return output

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Raw response content: {response.choices[0].message.content}")
        return "Error: Failed to parse AI response. The response may be malformed or truncated. Please try again."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return f"An error occurred: {e}"

# 5. CREATE THE GRADIO INTERFACE
# We use 'gr.Blocks' for a custom layout.
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        ## Snoonu Thermal Bag Quality Checker
        Upload a photo of a courier's thermal bag to check if it's in
        acceptable condition for a shift.
        """
    )
    
    with gr.Row():
        # Input column
        with gr.Column(scale=1):
            image_input = gr.Image(
                type="pil", 
                label="Upload Bag Photo",
                sources=["upload", "webcam"]
            )
            submit_btn = gr.Button("Analyze Bag", variant="primary")

        # Output column
        with gr.Column(scale=1):
            analysis_output = gr.Markdown(label="Analysis Result")
            

    # Connect the button to the function
    submit_btn.click(
        fn=analyze_bag_quality,
        inputs=image_input,
        outputs=analysis_output
    )

# 6. LAUNCH THE APP
if __name__ == "__main__":
    # share=True creates a public link for easy sharing
    demo.launch(share=True)