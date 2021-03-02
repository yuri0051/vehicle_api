# vehicle_api

### install application
sudo apt-get update
sudo apt-get install sqlite3

source venv/bin/activate
pip install -r requirements.txt

### test application
python -m pytest

### build image
cd docker/
./create_image.sh

### connect to cluster
source cluster.profile

gcloud container clusters get-credentials ${CLUSTER_NAME} --zone ${CLUSTER_ZONE}

### deploy deployment

kubectl apply -f deployment.yaml
kubectl get pods