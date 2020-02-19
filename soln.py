from collections import defaultdict as d

V, E, R, C, X = map(int,raw_input().split())
video_sizes = map(int,raw_input().split())
min_vid_size = min(video_sizes)
endpoints = d(list)
for idx in xrange(E):
    DC_latency, caches = map(int, raw_input().split())
    endpoints[idx].append((DC_latency, caches))
    for idx2 in xrange(caches):
        cache_idx, latency = map(int, raw_input().split())
        endpoints[idx].append((cache_idx, latency))

matrix = [[[x,0] for x in range(V)] for _ in range(C)] #index with matrix[C][V]
placed = [0] * V

for req in xrange(R):
    req_score = 1
    vid_id, endpoint, amt = map(int, raw_input().split())
    cache_remainder = (X - video_sizes[vid_id]) * 1000
    if cache_remainder < 0:
        req_score *= -1
    pass # req_score *= cache_remainder
    avail_cache = endpoints[endpoint][0][1] * 1
    if avail_cache:
        pass #req_score /= avail_cache
    else:
        req_score *= -1
    dc_lat = endpoints[endpoint][0][0]
    cache_save = [(x[0], 10 * amt * (dc_lat - x[1])) for x in endpoints[endpoint][1:]]
    for cache_idx, save_val in cache_save:
        matrix[cache_idx][vid_id] = [matrix[cache_idx][vid_id][0], req_score * save_val]

ans = d(list)
for cache_idx in xrange(C):
    cache = matrix[cache_idx]
    cache_bal = X
    for vid_id, score in sorted(cache, key = lambda x: -x[1]):
        if not placed[vid_id] and cache_bal >= video_sizes[vid_id] and matrix[cache_idx][vid_id][1] > 0:
            placed[vid_id] = 1
            cache_bal -= video_sizes[vid_id]
            ans[cache_idx].append(vid_id)
        if min_vid_size > cache_bal:
            break

print len(ans)
for x in ans:
    print x, " ".join(map(str,ans[x]))
