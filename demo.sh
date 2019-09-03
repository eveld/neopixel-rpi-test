#!/bin/bash
tiles=("vagrant" "packer" "terraform" "vault" "nomad" "consul")

# Turn on hashicorp tile.
echo "turn on hashicorp"
curl -XPOST localhost:5000/led/hashicorp

# Keep looping until we exit.
while true; do
    # Loop over the tiles.
    for tile in ${tiles[*]}; do
        # Turn them on for 5 seconds, then turn them off.
        echo "turn on $tile"
        curl -XPOST localhost:5000/led/$tile
        sleep 5
        echo "turn off $tile"
        curl -XDELETE localhost:5000/led/$tile
    done
done