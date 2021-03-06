#!/usr/bin/python

import hashlib
from collections import OrderedDict

# block hash
block_hash = bytes.fromhex('0000000000000000003729bfa376e4148ee0643ce834053d885af5699440d6d3')
# total lottery num
total_lottery = 100000


def lucky_num_from_block_hash(h):
    hash_names = ['md5', 'md4', 'whirlpool', 'RIPEMD160', 'DSA', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    print(str(len(hash_names)) + ": " + str(hash_names))

    repeat = 10000 * 400 * 20
    r = h
    for i in range(repeat):
        if i % 100000 == 0:
            print(str(i) + ":...")
        for n in hash_names:
            h = hashlib.new(n)
            h.update(r)
            r = h.digest()

    return r


def score_for_each_lottery(lucky_num, lottery_id):
    # print(result_hash.hex())
    h = hashlib.sha256()
    h.update(lucky_num)
    h.update(bytes(lottery_id))

    base = 10**11
    score = int(h.hexdigest(), 16) % base
    return score


def compute_airdrop_reward():
    r = {}
    lucky_num = lucky_num_from_block_hash(block_hash)

    for lottery_id in range(total_lottery):
        s = score_for_each_lottery(lucky_num, lottery_id)
        r[lottery_id] = s
    return r



reward_map = compute_airdrop_reward()
reward_sorted = OrderedDict(sorted(reward_map.items(), key=lambda t: t[1], reverse = True))
print("=======================Rewards================================")
for item in reward_sorted:
    print(str(item) + ": " + str(reward_map[item]))
