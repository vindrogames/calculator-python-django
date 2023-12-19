## Fly.io

deployment

```
fly auth login
fly deploy
```

## HTMX

CSRF error when using Django with HTMX in a post
Error:
```
Forbidden (CSRF cookie not set.): /clicked/
```
https://django-htmx.readthedocs.io/en/latest/tips.html#make-htmx-pass-the-csrf-token

Error:
```
RuntimeError: You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining POST data. Change your form to point to localhost:4000/clicked/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.
```
You have to also close the url in a post like clicked/