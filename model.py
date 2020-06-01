import sys

from google.api_core.client_options import ClientOptions
from google.cloud.automl_v1 import PredictionServiceClient
from google.cloud.automl_v1.proto import service_pb2
from common import credentials

def inline_text_payload(file_path):
  with open(file_path, 'rb') as ff:
    content = ff.read()
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def pdf_payload(file_path):
  return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }

def get_prediction(file_path, model_name):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = PredictionServiceClient(client_options=options)

  payload = inline_text_payload(file_path)
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  # payload = pdf_payload(file_path)

  print(payload)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned

if __name__ == '__main__':
  file_path = "predict_data/" + sys.argv[1]
  model_name = credentials()['model_name']

  print(get_prediction(file_path, model_name))
