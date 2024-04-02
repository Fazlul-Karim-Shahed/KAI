
from flask import request, jsonify, make_response
import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri

async def chat_generator():
    try:
        print(request.get_json()['prompt'])
        try:
            role = sagemaker.get_execution_role()
        except ValueError:
            iam = boto3.client('iam')
            role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']

        # Hub Model configuration. https://huggingface.co/models
        hub = {
            'HF_MODEL_ID':'TheBloke/Falcon-180B-Chat-GGUF',
            'SM_NUM_GPUS': json.dumps(8)
        }



        # create Hugging Face Model Class
        huggingface_model = HuggingFaceModel(
            image_uri=get_huggingface_llm_image_uri("huggingface",version="1.4.2"),
            env=hub,
            role=role, 
        )

        # deploy model to SageMaker Inference
        predictor = huggingface_model.deploy(
            initial_instance_count=1,
            instance_type="ml.p4d.24xlarge",
            container_startup_health_check_timeout=2100,
        )
        
        # send request
        predictor.predict({
            "inputs": "My name is Clara and I am",
        })

        



    except Exception as err:
        return jsonify({"message": str(err), "error": True })