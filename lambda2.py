
def foo():
	return 1

bar = lambda: 1
quux = lambda x: x


quux2 = lambda x: bar() + foo()

# return lambda doc: \
#             (doc['udid'] == _filters.get('udid') if _filters.has_key("udid") else doc['udid']).default(True) & \
#             (doc['deviceOs'] == _filters.get('deviceOS') if _filters.has_key("deviceOs") else doc['deviceOs']).default(True) & \
#             (doc['statusId'] == _filters.get('statusId') if _filters.has_key("statusId") else doc['statusId']).default(True) & \
#             (doc['ownerId'] == _filters.get('ownerId') if _filters.has_key("ownerId") else doc['ownerId']).default(True) & \
#             (doc['typeId'] == _filters.get('typeId') if _filters.has_key("typeId") else doc['typeId']).default(True) & \
#             (doc['clientId'] == _filters.get('clientId') if _filters.has_key("clientId") else doc['clientId']).default(True) & \
#             (get_datefilter_span(doc, _filters.get("createdAt")) if _filters.has_key("createdAt") else doc['createdAt']).default(True) & \
#             (get_datefilter_span(doc, _filters.get("updatedAt")) if _filters.has_key("updatedAt") else doc['updatedAt']).default(True)

# print foo
# print quux(2)
print quux2(1)