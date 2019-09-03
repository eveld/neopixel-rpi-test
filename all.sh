#!/bin/bash
tiles=("consul" "nomad" "vault" "terraform" "packer" "vagrant")

# Turn on hashicorp tile.
echo "turn on hashicorp"
curl -XPOST localhost:5000/led/hashicorp

# Loop over the tiles.
for tile in ${tiles[*]}; do
    # Turn them on for 5 seconds, then turn them off.
    echo "turn on $tile"
    curl -XPOST localhost:5000/led/$tile
done