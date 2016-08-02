#! /bin/bash

INPUT_DIR="/home/maxime/Desktop/WordCountPipe/combine/outbox/processed"
cd "/home/maxime/Desktop/WordCountPipe/shuffle&sort"
function block_for_change {
  inotifywait -r \
	-e moved_to,create \
	$INPUT_DIR
}

BUILD_SCRIPT=main.py   

function build {
  bash python3 $BUILD_SCRIPT -i $INPUT_DIR -o "/home/maxime/Desktop/WordCountPipe/suffle&sort/outbox"
}


while block_for_change; do
  build
done