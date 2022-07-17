# Progress Notes

* successfully streamed a song!
  * Involved setting up `libopus`. For mac, I had to `brew install opus` and symlink it to the python environment's `/lib` folder:
    
    ```{code-block}
    brew install opus
    ln -s $HOMEBREW_CELLAR/opus/1.3.1/lib/libopus.0.dylib $CONDA_PREFIX/lib/libopus.dylib
    ```

    and then add this before the streaming code is run.
    ```python
    disnake.opus.load_opus(name="libopus.dylib")
    ```

## To Do

* Simplify playing and joining.
* Make `!play` the default streaming command
* Make `!play` automatically join the bot to the voice channel
* Implement a queue
  * Queue itself
  * Queue management
  * Queue display
* Long term: spotify integration
  * Simpler maybe: keep record of the streams