
from flask import request, jsonify, make_response
from transformers import AutoTokenizer, AutoModelForCausalLM

async def chat_generator_llama():
    try:
        print(request.get_json()['prompt'])
        

        tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-hf")
        model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-hf")

        prompt = "Hey, are you conscious? Can you talk to me?"
        inputs = tokenizer(prompt, return_tensors="pt")

        # Generate
        generate_ids = model.generate(inputs.input_ids, max_length=30)
        print(tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])
        
        return jsonify({"message": tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0], "error": False })

    except Exception as err:
        return jsonify({"message": str(err), "error": True })