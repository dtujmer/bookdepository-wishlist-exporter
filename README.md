# bookdepository-wishlist-exporter
A simple exporter for BookDepository wishlists

I wanted to export all my books but I didn't want to provide any credentials, so here's an exporter that works without any creds.


How to run:

```
python3 wishlist.py <url_of_your_wishlist>
```

## TODO:

- [ ] need to add a better paging system, for now, edit the script - line 8 (`for...in range(1, x)`: **x should be the number of pages you have on your wishlist + 1!**)
