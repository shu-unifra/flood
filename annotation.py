import datetime
import json
import requests


HOST="https://grafana.unifra.xyz/"
dashboardUID="r1m-inuIk"

def get_annotation(file_path)->list[str]:
  URL=HOST+"api/annotations"
  response = requests.get(url = URL)
  if response.status_code != 200:
      raise Exception(f"Failed to get annotations: {response.status_code} {response.text}")
  
  data = response.json()
  print(data)
  json_data = json.loads(data)
  ids=[]
  for item in json_data:
    if "shutest" in item["text"]:
        ids.append(item["id"])
  return ids

def delete_annotation(id):
  URL=HOST+"api/annotations/"+id
  response = requests.delete(url = URL)
  if response.status_code != 200:
      raise Exception(f"Failed to delete annotation: {response.status_code} {response.text}")
  print(response.json())

def delete_all_annotations():
  ids = get_annotation("./results.json")
  for id in ids:
    delete_annotation(id)

def create_annotation(annotation_json):
  URL=HOST+"api/annotations"
  print(annotation_json)
  response = requests.post(url = URL, json=annotation_json)
  if response.status_code != 200:
      raise Exception(f"Failed to create annotation: {response.status_code} {response.text}")

def create_all_annotations(resultFile):
  panel_ids=get_all_panel_id(dashboardUID)
  with open(resultFile, "r") as f:
    data = json.load(f)
    for nodeName in data:
        nodeData = data[nodeName]
        rateLen=len(nodeData["target_rate"])
        for i in range(rateLen):
          tags=[]
          for key in nodeData:
            tag=key+"="+str(nodeData[key][i])
            if len(tag) > 100:
                tag=tag[:100]
            tags.append(tag)
          for panel_id in panel_ids:
            annotation_json = {
            "dashboardUID":dashboardUID,
            "panelId":panel_id,
            "time":int(datetime.fromisoformat(nodeData["first_request_timestamp"][i]).timestamp()*1000), 
            "timeEnd": int(datetime.fromisoformat(nodeData["last_response_timestamp"][i]).timestamp()*1000),
            "tags":tags,
            "text":nodeName+" "+nodeData["target_rate"][i]+" rps"
          }
          create_annotation(annotation_json)

def get_all_panel_id(dashboardUID):
    URL=HOST+"api/search?dashboardUID="+dashboardUID
    response = requests.get(url = URL)
    if response.status_code != 200:
        raise Exception(f"Failed to get panel id: {response.status_code} {response.text}")
    data = response.json()
    panel_ids=[]
    for item in data:
        panel_ids.append(item["id"])
    return panel_ids

if __name__ == "__main__":
  ids = get_annotation("./results.json")
  