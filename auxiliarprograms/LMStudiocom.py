from openai import OpenAI
import time

client = OpenAI(base_url="http://localhost:1234", api_key="not-needed") 

def get_llm_response(prompt):
    """
    Function to send a single prompt to the LLM and get the response.
    """
    try:
        completion = client.chat.completions.create(
            model="DeepSeek-R1-Distill-Qwen-7B-GGUF/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf", 
                               
            messages=[
                {"role": "system", "content": "Init"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  
            max_tokens=500,   
            stream=False      
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error getting response from LLM: {e}")
        return None

def process_multiple_inputs(input_list):
    """
    Processes a list of inputs and gets an LLM response for each.
    """
    results = {}
    for i, user_input in enumerate(input_list):
        print(f"\n--- Processing input {i+1} ---")
        print(f"Input: {user_input}")
        response = get_llm_response(user_input)
        if response:
            print(f"LLM Response: {response}")
            results[user_input] = response
        else:
            print("Could not get response.")
        time.sleep(1) 

    return results

if __name__ == "__main__":
    

    my_inputs = [
        "Example1",
        "Example2",
        "Example3",
        "Example4"
    ]

    print("Starting to process multiple inputs via LM Studio...")
    all_responses = process_multiple_inputs(my_inputs)

    print("\n--- Summary of All Responses ---")
    for input_text, output_text in all_responses.items():
        print(f"Input: {input_text}\nOutput: {output_text}\n---")