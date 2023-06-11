from googleapiclient import discovery
import json

API_KEY = 'your api key'

def get_toxicity_value(sentence):
  client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
  )

  analyze_request = {
    'comment': { 'text': '{}'.format(sentence) },
    'requestedAttributes': {'TOXICITY': {}}
  }
  response = client.comments().analyze(body=analyze_request).execute()
  return response['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']