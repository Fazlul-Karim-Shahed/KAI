
from flask import request, jsonify, make_response
from transformers import AutoTokenizer, AutoModelForCausalLM, LlamaForCausalLM
import transformers
import torch

async def chat_generator_llama():
    try:
        print(request.get_json()['prompt'])
        

        # tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-hf")
        # model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-hf")

        # model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
        # tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

        # prompt = request.get_json()['prompt']
        # inputs = tokenizer(prompt, return_tensors="pt")

        # # Generate
        # generate_ids = model.generate(inputs.input_ids, max_length=30)
        # print(tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])
        
        # return jsonify({"message": tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0], "error": False })

        

        model = "meta-llama/Llama-2-7b-chat-hf"

        tokenizer = AutoTokenizer.from_pretrained(model)
        pipeline = transformers.pipeline(
            "text-generation",
            model=model,
            torch_dtype=torch.float16,
            device_map="auto",
        )

        sequences = pipeline(
            request.get_json()['prompt'],
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
            max_length=200,
        )
        for seq in sequences:
            print(f"Result: {seq['generated_text']}")

        return 'ok'


    except Exception as err:
        return jsonify({"message": str(err), "error": True })