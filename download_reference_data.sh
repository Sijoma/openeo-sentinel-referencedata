#!/bin/bash
while IFS='' read -r uid || [[ -n "$uid" ]]; do
    echo "UID: $uid"
    product_uids=$product_uids$uid','
done < "$1"
echo $product_uids
sentinelsat -u $2 -p $3 --uuid $product_uids -d 