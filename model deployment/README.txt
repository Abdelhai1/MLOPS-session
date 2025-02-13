
install requirements
pip install -r requirements.txt

run the model
uvicorn app:app --reload

build the container
docker build -t regression-api .

run the container
docker run -p 80:80 regression-api