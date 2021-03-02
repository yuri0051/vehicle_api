#!/bin/bash

source image.profile

docker run --rm -d -p ${PORT}:${PORT} ${IMAGE}:${TAG}