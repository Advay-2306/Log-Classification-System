import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq = Groq()

def classify_with_llm(log_msg):
    """
    Classify a log message using the DeepSeek LLM.
    Returns one of: Workflow Error, Deprecation Warning, or Unclassified.
    """
    # Prompt the LLM, requesting output wrapped in <category> tags
    prompt = f'''Classify the log messages into one of these categories: 
    (1) Workflow Error, (2) Deprecation Warning. 
    If you cannot figure out a category, use 'Unclassified' instead.' 
    Directly put the category inside <category> </category> tags. No preamble.
    Log Message: {log_msg}'''

    # Send request to DeepSeek LLM
    chat_completion = groq.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="deepseek-r1-distill-llama-70b",
        temperature=0.5
    )

    # Extract the LLM's response content
    content = chat_completion.choices[0].message.content

    # Parse category from <category> tags using regex
    match = re.search(r'<category>(.*)</category>', content, flags=re.DOTALL)
    category = "Unclassified"  # default if tags not found
    if match:
        category = match.group(1)

    return category

if __name__ == '__main__':
    # Example usage
    print(classify_with_llm("User User123 logged in."))  # Expected: Unclassified
    print(classify_with_llm("Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))  # Expected: Workflow Error
