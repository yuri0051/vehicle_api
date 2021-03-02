#!/bin/bash

source image.profile

docker build -t ${IMAGE}:${TAG} -f Dockerfile ../