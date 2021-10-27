def paginate_queryset(queryset, page_size: int = 50, page_num: int = 1):
    offset = (page_num - 1) * page_size
    queryset = queryset.offset(offset).limit(page_size)
    return queryset
