#!/bin/bash

source cluster.profile

gcloud container clusters create ${CLUSTER_NAME} --zone ${CLUSTER_ZONE}