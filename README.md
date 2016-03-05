baiji
=====

High-level Python abstraction layer for Amazon S3.


Features
--------

- An `open`-like context handler which allows using S3 keys and local
  files interchangeably.
- When reading or writing S3, contents are first written to a temporary local
  file. When writing, contents are uploaded on close.
- A CLI for listing, copying, syncing, and other common activities.
- When accessing local files, works without an S3 connection.
- Tested and production-hardened.
- Supports OS X, Linux, and Windows.
- Support Python 2.7 and uses boto2.


Examples
--------

```py
with s3.open('s3://example/info.txt', 'w') as f:
    f.write('hello')

with s3.open('s3://example/info.txt', 'r') as f:
    contents = f.readlines()
```

```sh
s3 cp foo.txt s3://example/bar.txt
s3 cp s3://example/bar.txt s3://another-example/bazinga.txt
s3 rm s3://example/bar.txt
```
