#!/bin/bash

cwd=$(pwd)

cd "to_resize"

if [ ! -d "out" ]; then
	mkdir -p "out"
fi


if [ ! -d "resized" ]; then
	mkdir -p "resized"
fi

for img in *.JPG; do
	convert "$img" -resize 1024 -quality 95 "out/${img}"
done

mv *.JPG resized/

for img in *.jpg; do
	convert "$img" -resize 1024 -quality 95 "out/${img}"
done

mv *.jpg resized/

exit 0
