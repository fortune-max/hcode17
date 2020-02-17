from collections import defaultdict as d

V, E, R, C, X = map(int,raw_input().split())
video_sizes = map(int,raw_input().split())
endpoints = d(list)
for idx in xrange(E):
    DC_latency, caches = map(int, raw_input().split())
    endpoints[idx].append((DC_latency, caches))
    for idx2 in xrange(caches):
        cache_idx, latency = map(int, raw_input().split())
        endpoints[idx].append((cache_idx, latency))

requests = [0] * R
for req in xrange(R):
    vid_id, endpoint, amt = map(int, raw_input().split())
    requests[req] = (vid_id, endpoint, amt)

# Process the answer
video_store = d(list)
for idx in xrange(input()):
    arr = map(int, raw_input().split())
    cache_idx, cache_vids = arr[0], arr[1:]
    for vid in cache_vids:
        video_store[vid].append(cache_idx)

# Now process the requests in question
ans = [];amt_total = 0
for request in requests:
    vid_id, endpoint, amt = request
    default_latency = endpoints[endpoint][0][0]
    pre_cached = set(video_store[vid_id])
    avail_cache = set([x[0] for x in endpoints[0][1:]])
    options = pre_cached & avail_cache
    endpoint_options = [x[1] for x in endpoints[endpoint] if x[0] in [y for y in (pre_cached & avail_cache)]]
    mn = 9999999999999
    if endpoint_options:
        mn = min(endpoint_options)
    tmp_ans = default_latency - min(mn, default_latency)
    ans.append(amt*tmp_ans)
    amt_total += amt
print int(1000*(sum(ans)*1./amt_total))
