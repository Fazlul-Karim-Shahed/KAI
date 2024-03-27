
from flask import request, jsonify, make_response
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

async def chat_generator():
    try:

        model = "tiiuae/falcon-7b"

        data = request.get_json()
        print(data['prompt'])

        tokenizer = AutoTokenizer.from_pretrained(model)
        pipeline = transformers.pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto",
        )
        sequences = pipeline(
        "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
            max_length=200,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
        )

        arr = []
        for seq in sequences:
            arr.append(seq['generated_text'])
            # print(f"Result: {seq['generated_text']}")

        return  jsonify({"message": "Ok", "error": False, "data": arr })



    except Exception as err:
        return jsonify({"message": str(err), "error": True })