baiji
=====

High-level Python abstraction layer for Amazon S3:

1. An [`open`][open]-like context handler which allows using S3 keys and
   local files interchangeably.
     - When reading S3, contents are first written to a temporary local
       file.
     - When writing S3, contents are written to a temporary local file,
       and uploaded on close.
2. An `s3` CLI for listing, copying, syncing, and other common activities.


Features
--------

- Works without an S3 connection (with local files).
- Supports multiprocess parallelism for copying lots of files.
- Support Python 2.7 and uses boto2.
- Supports OS X, Linux, and Windows.
- Tested and production-hardened.

[open]: https://docs.python.org/2/library/functions.html#open


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


TODO
----

1. Decide on the name.
2. Decide whether there is anything in `baiji.util` we want to duplicate in
   core. (Seems like, for the most part, these are totally reasonable functions
3. Decide whether we want to bother removing the bodylabs-specific stuff: the
   `~/.bodylabs` file, and the reference to the guts TransientError class.
   I don't like having these references in the library, and it doesn't feel
   like a high priority to unwind those things, however if we _are_ going to
   unwind them, it's easier to do before we update the references to
   `bodylabs.cloud.s3`. If we did move the bodylabs-specific config handling
   back into core, I imagine we could accomplish it using a wrapper, and
   possibly a monkey patch.
4. Decide whether any of the util code should be moved into another library.
   The decorators feel particularly out of place -- feels like it would be
   a little weird to import them in core from here. I can imagine someday
   having a library of low-level utils like that (as much as I dislike
   random utils collections). But I don't think now is the time. Best bet,
   perhaps, is to simply rewrite this code so it does not require the
   decorators, as they are used so lightly and sparingly here.
5. Check if `requirements.txt` is being handled okay, and think about how and
   whether we will declare any of these dependencies in core.
