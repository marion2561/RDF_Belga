docker network create rdf_network
docker build -t rdf-gateway .       
docker run --network rdf_network -d --name rdf-gateway -p 81:81 rdf-gateway
