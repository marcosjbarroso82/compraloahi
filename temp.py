def _getAdListJson(tags=None, lat=None, lng=None, radius=None):
    object_response = []
    queryset = Ad.objects.all()

    if tags:
        tags = tags.split()
        queryset = queryset.filter(tags__name__in=tags).distinct()
    if lat and lng and radius:
        print("lat" + str(lat))
        print("lng" + str(lng))
        queryset = queryset.filter(locations__lat__range=(lat - radius, lat + radius))
        queryset = queryset.filter(locations__lng__range=(lng - radius, lng + radius))

    for ad in queryset:
        thumbnail = get_thumbnail(ad.images.first().image, '100x100', crop='center', quality=99).url
        object_response.append( {"title": ad.title + " " + str(datetime.now().strftime('%M:%S')), "body":ad.body, "thumbnail": thumbnail} )
    return json.dumps(object_response)