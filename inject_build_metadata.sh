#!/bin/bash

sed "s|BUILD_VERSION|${BUILD_VERSION:-defaultBuild}|g" -i build_metadata.json
sed "s|COMMIT_SHA|${COMMIT_SHA:-randomSHA}|g" -i build_metadata.json