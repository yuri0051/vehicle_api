#bin/bash

source image.profile

docker tag ${IMAGE}:${TAG} ${DOCKER_REPO}/${IMAGE}:${TAG}

docker push ${DOCKER_REPO}/${IMAGE}:${TAG}